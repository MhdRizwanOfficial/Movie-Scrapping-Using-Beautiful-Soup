import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = 'https://www.themoviedb.org/movie?page='
all_page_data=[]

for num in range(1,51):
    
    resp1 = requests.get(base_url + str(num)).text
    soup_data = BeautifulSoup(resp1,'lxml')
    all_div = soup_data.find_all('div',class_='card style_1')
    
    for items in all_div:
                            
        inner_div= items.find('div',class_='content')
        inner_link = inner_div.find('a')['href']
        full_link = 'https://www.themoviedb.org' + inner_link
            
        inner_data_req = requests.get(full_link).text
        new_soup_data = BeautifulSoup(inner_data_req,'lxml')
            
        movie_name = inner_div.find('h2').text.strip()
            
        movie_date = inner_div.find('p').text.strip()
        
        
        rating_div = new_soup_data.find('div','user_score_chart')
        if rating_div:
            rating = rating_div["data-percent"]
        else:
            rating = 'N/A'
    
            
        genre_class = new_soup_data.find('span',class_='genres') 
        genre = genre_class.findAll('a')
        genre_list = [i.text for i in genre]
        genrees = ', '.join(genre_list).strip()   
            
            
        run_time_find = new_soup_data.find('span',class_='runtime')
        if run_time_find:
            run_time = run_time_find.text.strip()
        else:
            run_time = "N/A"
            
            
        ovr_view = new_soup_data.find('div',class_='overview')
        overview = ovr_view.find('p').text
            
            
        ol_profile = new_soup_data.find('ol',class_='people no_image')
        li_profile = ol_profile.findAll('li',class_='profile')
        director = set()
        for i in range(0,len(li_profile)): #0,4
                if 'Director' in li_profile[i].find('p',class_="character").text:
                    direct = li_profile[i].find('a').text
                    director.add(direct)
        directors = ', '.join(director)
            
            
        first_page_data = {
            
        'Movie_name' : movie_name,
        'Release_date' : movie_date,
        'Rating' : rating,
        'Genre' : genrees,
        'Run_time' : run_time,
        'Overview' : overview,
        'Director' : directors
            
        }   
        
        all_page_data.append(first_page_data)
        
  
df = pd.DataFrame(all_page_data)
df.index = df.index+1
df.to_excel('all_movies_datas.xlsx',index=True)  


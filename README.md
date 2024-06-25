# TMDb-Movie-Data-Scraper

## Description

TMDb-Movie-Data-Scraper is a Python-based web scraping tool that extracts detailed information about movies from The Movie Database (TMDb). The tool collects data such as movie name, release date, rating, genre, runtime, overview, and director for movies across multiple pages, and saves the data into an Excel file for easy analysis.

## Features

- Scrapes movie information from multiple pages of TMDb
- Extracts details including movie name, release date, rating, genre, runtime, overview, and director
- Saves the collected data into an Excel file

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `lxml` parser

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/TMDb-Movie-Data-Scraper.git
    cd TMDb-Movie-Data-Scraper
    ```

2. Install the required libraries:

    ```sh
    pip install requests beautifulsoup4 pandas lxml
    ```

## Usage

1. Run the script to start scraping data:

    ```sh
    python scrape_movies.py
    ```

2. The script will generate an Excel file named `all_movies_datas.xlsx` containing the scraped movie data.

## License

This project is licensed under the MIT License.

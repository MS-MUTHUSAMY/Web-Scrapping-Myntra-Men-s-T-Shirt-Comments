# Web-Scrapping-Myntra-T-Shirt-Reviews-Data-Harvesting

Below is a step-by-step guide for your Python web scraping project aimed at harvesting T-shirt review data from Myntra. This README will provide users with clear instructions on how to set up, run, and understand your code.

# Myntra T-Shirt Review Data Scraper

This Python script enables users to scrape T-shirt review data from Myntra's website. It utilizes Selenium for web scraping and provides functionality to extract product details and user reviews.

# Table of Contents

* Overview
* Dependencies
* Usage
* Output


## Overview

Web scraping is the process of extracting data from websites. This script uses Selenium, a powerful automation tool, to navigate Myntra's web pages, extract relevant information such as product details, ratings, reviews, and save it in a structured format.


## Dependencies

* Python 3.x
* Pandas
* Selenium
* Chrome web browser
  
# Usage

Open the main.py file in a text editor.

Customize the get_product_link() and over_all_details() functions if necessary.

## Run the script:

python main.py

* The script will start scraping T-shirt details and reviews from Myntra's website.
* In first step to scarpe the T-shirt links of give page range and save to product_links.csv.
* Next step to get the one by one T-shirt link from product_links.csv, Using selenium, chrome web driver to get the necessary details which we want.
* Go to review section to scrape the ratings, reviews, user names, review dates, and image links.
* These data are saved as myntra_mens_t_shirt_details.csv.


# Output

The script will generate two CSV files:

**product_links.csv:** Contains the links to individual T-shirt product pages.

**myntra_mens_t_shirt_details.csv:** Contains the extracted T-shirt details including product name, description, prices, ratings, reviews, user names, review dates, and image links.


# Links 

* **LinkedIn Link :** https://www.linkedin.com/in/ms-mgr-agri/
* **YouTube Link  :**


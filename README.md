# Web-Scrapping-Myntra-T-Shirt-Reviews-Data-Harvesting

Below is a step-by-step guide for your Python web scraping project aimed at harvesting T-shirt review data from Myntra. This README will provide users with clear instructions on how to set up, run, and understand your code.

# Myntra T-Shirt Review Data Scraper

This Python script enables users to scrape T-shirt review data from Myntra's website. It utilizes Selenium for web scraping and provides functionality to extract product details and user reviews.

# Table of Contents

* Overview
* Setup
* Dependencies
* Usage
* Output
* License

## Overview

Web scraping is the process of extracting data from websites. This script uses Selenium, a powerful automation tool, to navigate Myntra's web pages, extract relevant information such as product details, ratings, reviews, and save it in a structured format.

## Setup

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/myntra-tshirt-scraper.git
Navigate to the project directory:
bash
Copy code
cd myntra-tshirt-scraper
Install the required dependencies:
bash
Copy code
pip install pandas selenium
Ensure you have the Chrome web browser installed.

## Dependencies

* Python 3.x
* Pandas
* Selenium
* Chrome web browser
  
# Usage

Open the myntra_scraper.py file in a text editor.

Customize the get_product_link() and over_all_details() functions if necessary.

## Run the script:

bash
Copy code
python myntra_scraper.py
The script will start scraping T-shirt details and reviews from Myntra's website.

# Output

The script will generate two CSV files:

**product_links.csv:** Contains the links to individual T-shirt product pages.
**myntra_mens_t_shirt_details.csv:** Contains the extracted T-shirt details including product name, description, prices, ratings, reviews, user names, review dates, and image links.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Links 

* **LinkedIn Link :** https://www.linkedin.com/in/ms-mgr-agri/
* **YouTube Link  :**


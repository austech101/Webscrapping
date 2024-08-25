
This script extracts headlines and summaries from the NTV Kenya news website.

Requirements
Python 3.x,
requests library,
beautifulsoup4 library,

You can install the necessary libraries using pip:
pip install requests beautifulsoup4Code Explanation

Import Libraries
import requests using from bs4 import BeautifulSoup
requests is used to make HTTP requests to the web page.
BeautifulSoup is used for parsing HTML content.
Send a GET request to the NTV Kenya news page and the HTTP status code of the response to ensure the request was successful.
	
Parse HTML Content and Extract Headlines: headline = soup.find_all(id="video-card_title no_shadow")

Finds all elements with the specified ID (note: IDs should be unique per HTML standard; ensure this ID is correct or change to class).
Prints the text of each headline.

Extract Summaries using and find all paragraph elements.
Ensure the IDs and class names used in the code match those on the website, as they may change over time.

This script is designed to work with the current structure of the NTV Kenya news page; modifications may be required for different pages or structures.

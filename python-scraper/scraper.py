#! /usr/bin/env python3
import re, os, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(output_dir):
    """
    This is where you write your scraping scripts. Belowe are some commented
    out sections that have example scripts to get started for various types of
    situations. Just uncomment the section that you need and start coding!
    """

    #######################################
    ## Html parsing using beautifulsoup4 ##
    #######################################
    """
    # Open a webpage
    resp = requests.get("https://www.example.com")

    # Parse out the links content
    bs = BeautifulSoup(resp.content, "lxml")
    href = bs.select("div > p > a")[0]['href']

    # Save the linked page
    with open(os.path.join(output_dir, "output.html"), "wb") as out:
        out.write(requests.get(href).content)
    """

    ##########################################
    ## Full browser scraping using Selenium ##
    ##########################################
    """
    # Open a webpage using Firefox (default) or Chrome (uncomment to use)
    driver = webdriver.Firefox() # needs geckodriver in PATH
    #driver = webdriver.Chrome() # needs chromedriver in PATH
    driver.get("https://www.example.com/")

    # Wait for the link to load
    link_selector = "div > p > a"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, link_selector)))

    # Click on a link via css selector
    driver.find_elements_by_css_selector(link_selector)[0].click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header")))

    # Save the page source
    with open(os.path.join(output_dir, "output.html"), "wb") as out:
        out.write(driver.page_source.encode("utf-8"))

    # Close the browser
    driver.quit()
    """

    print("Done!")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="""
This is diafygi's scraping script for the 2017 DataRescueSFBay event.
Example Usage: python3 scraper.py --output ../data/
""")
    parser.add_argument('--output', required=True, help='output directory')
    args = parser.parse_args()
    main(args.output)


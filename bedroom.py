from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import csv
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import json
from selenium import webdriver

OUTPUT_FILE_NAME = 'BEDROOM_DATA.csv'
HEADER_FILE = ['product name', 'product price']

# CSS Selectors for product name and price
PRODUCT_NAME_SELECTOR = "h3[class*='product-card__title product-title']"
PRODUCT_PRICE_SELECTOR = ".price__last .price-item--regular"
VIEWMORE_BUTTON_SELECTOR = "button[class*='btn btn--light-3']"

def configure_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")  # removes error/warning/info messages displayed on the console
    chrome_options.add_argument("--disable-notifications")  # disable notifications
    chrome_options.add_argument("--disable-infobars")  # disable infobars "Chrome is being controlled by automated test software"
    chrome_options.add_argument('--disable-gpu')  # disable GPU (not load pictures fully)
    #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")  # Connect to existing Chrome
    chrome_options.add_argument("--disable-extensions")  # will disable developer mode extensions
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_all_product_details(driver, url):
    driver.get(url)

    # Initial wait for the page to load
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, PRODUCT_NAME_SELECTOR))
    )

    # Click on "View More" button until it's no longer visible
    while True:
        try:
            view_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, VIEWMORE_BUTTON_SELECTOR))
            )
            view_more_button.click()
            time.sleep(2)  # Wait for new content to load
        except:
            break

    # Scroll to the bottom of the page to load all content
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the HTML content after JavaScript execution
    html_content = driver.page_source
    return html_content

def extract_product_details(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    product_names = soup.select(PRODUCT_NAME_SELECTOR)
    product_prices = soup.select(PRODUCT_PRICE_SELECTOR)

    output_results = set()  # Use a set to remove duplicates
    for name, price in zip(product_names, product_prices):
        product_name = name.get_text(strip=True)
        product_price = price.get_text(strip=True)
        output_results.add((product_name, product_price))


    return list(output_results)

def write_to_file(rows):
    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8-sig', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER_FILE)  # Write the header
        writer.writerows(rows)

def RunScrapper(driver):
    links = ["https://essopshome.co.za/collections/bedroom-suites"]
             # "https://essopshome.co.za/collections/base-boxes",
             # "https://essopshome.co.za/collections/storage-box",
             # "https://essopshome.co.za/collections/night-stands",
             # "https://essopshome.co.za/collections/chest-of-drawers",
             # "https://essopshome.co.za/collections/wardrobes",
             # "https://essopshome.co.za/collections/pillows-protectors",
             # "https://essopshome.co.za/collections/mattresses",
             # "https://essopshome.co.za/collections/lounge-collection",
             # "https://essopshome.co.za/collections/couches",
             # "https://essopshome.co.za/collections/recliner-suites",
             # "https://essopshome.co.za/collections/daybed-couches",
             # "https://essopshome.co.za/collections/leisure-chairs",
             # "https://essopshome.co.za/collections/coffee-tables","https://essopshome.co.za/collections/side-tables","https://essopshome.co.za/collections/bar-tables","https://essopshome.co.za/collections/tv-units",
             # "https://essopshome.co.za/collections/bar-chairs",
             # "https://essopshome.co.za/collections/dining-chairs",
             # "https://essopshome.co.za/collections/bar-tables",
             # "https://essopshome.co.za/collections/dining-room-suites",
             # "https://essopshome.co.za/collections/dining-tables",
             # "https://essopshome.co.za/collections/buffets",
             # "https://essopshome.co.za/collections/console-tables",
             # "https://essopshome.co.za/collections/desks",
             # "https://essopshome.co.za/collections/office-chairs",
             # "https://essopshome.co.za/collections/outdoor-lounge",
             # "https://essopshome.co.za/collections/outdoor-coffee-tables",
             # "https://essopshome.co.za/collections/outdoor-swings",
             # "https://essopshome.co.za/collections/outdoor-dining",
             # "https://essopshome.co.za/collections/rugs",
             # "https://essopshome.co.za/collections/frames-mirrors",
             # "https://essopshome.co.za/collections/table-lamps",
             # "https://essopshome.co.za/collections/chandeliers",
             # "https://essopshome.co.za/collections/flowers-pots",
             # "https://essopshome.co.za/collections/ornaments",
             # "https://essopshome.co.za/collections/scatters"]
    all_results = set()  # Use a set to collect all results and remove duplicates

    for link in links:
        html_content = get_all_product_details(driver, link)
        product_details = extract_product_details(html_content)
        all_results.update(product_details)  # Add the unique results to the set

    write_to_file(list(all_results))

if __name__ == '__main__':
    driver = configure_driver()
    RunScrapper(driver)
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from PIL import Image
import matplotlib.pyplot as plt
import json
import os
import time

# Set up paths
BASE_URL = "https://iticket.az/events/concerts"
COMPLETE_URLS_PATH = 'assets/complete_urls.txt'
CONCERT_DATA_PATH = 'assets/concert_data.json'

# Function to scrape event links
def scrape_event_links(base_url=BASE_URL, num_pages=9):
    driver = webdriver.Chrome()
    event_links = []

    for page_num in range(1, num_pages + 1):
        link = f"{base_url}?page={page_num}"
        driver.get(link)
        time.sleep(2)
        
        # Wait for the page to load completely
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'event-list-item')))

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        event_elements = soup.find_all('a', class_='event-list-item')

        # Extract event URLs
        for event in event_elements:
            event_links.append(event['href'])

    driver.quit()
    
    # Save links to a file
    with open(COMPLETE_URLS_PATH, 'w') as file:
        for link in event_links:
            file.write(link + '\n')

    print(f"Event links have been written to '{COMPLETE_URLS_PATH}'")

# Function to scrape concert data from event pages
def scrape_concert_data(urls_file=COMPLETE_URLS_PATH, output_json=CONCERT_DATA_PATH):
    if not os.path.exists(urls_file):
        print(f"File '{urls_file}' not found.")
        return

    driver = webdriver.Chrome()
    concert_data = []

    with open(urls_file, 'r') as file:
        for url in file:
            url = url.strip()
            if not url.startswith('https'):
                url = f"https://iticket.az{url}"
            driver.get(url)

            try:
                wait = WebDriverWait(driver, 10)
                info_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icalendar"]/div/div/div[1]')))
                driver.execute_script("window.scrollTo(0, 4000)")

                concert_name = info_div.find_element(By.XPATH, '//*[@id="icalendar"]/div/div/div[1]/div[1]/div[1]').text.strip()
                place = info_div.find_element(By.XPATH, '//*[@id="icalendar"]/div/div/div[1]/div[1]/div[2]').text.strip()
                time = info_div.find_element(By.XPATH, '//*[@id="icalendar"]/div/div/div[1]/div[2]/div[2]').text.strip()
                price = info_div.find_element(By.XPATH, '//*[@id="icalendar"]/div/div/div[1]/div[3]/div[2]').text.strip()
                text = info_div.find_element(By.XPATH, '//*[@id="tab-0"]/div[2]').text.strip()

                # Attempt to extract the second image link
                try:
                    second_image = info_div.find_element(By.XPATH, '//*[@id="event-detail"]/div[2]/div/img[2]').get_attribute('data-src')
                except Exception:
                    second_image = None

                concert_data.append({
                    'Concert Name': concert_name,
                    'Place': place,
                    'Time': time,
                    'Price': price,
                    'Additional Text': text,
                    'Image': second_image if second_image else "No image available",
                    'Web Page URL': url
                })

    

            except Exception as e:
                print(f"Error processing {url}: {str(e)}")

    driver.quit()

    # Save concert data to a JSON file
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(concert_data, json_file, indent=2, ensure_ascii=False)

    print(f"Concert data has been written to '{output_json}'")

# Run the scraper functions
if __name__ == "__main__":
    scrape_event_links()
    scrape_concert_data()

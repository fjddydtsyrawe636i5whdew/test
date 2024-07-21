import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Replace these with your actual Microsoft account credentials
username = "your_email@example.com"
password = "your_password"

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to log in to Bing
def login_to_bing():
    driver.get("https://login.live.com/")
    time.sleep(random.uniform(2, 4))
    driver.find_element(By.NAME, "loginfmt").send_keys(username)
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(random.uniform(2, 4))
    driver.find_element(By.NAME, "passwd").send_keys(password)
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(random.uniform(2, 4))
    driver.find_element(By.ID, "idSIButton9").click()  # Stay signed in

# Function to perform a search
def perform_search(query):
    driver.get("https://www.bing.com/")
    time.sleep(random.uniform(2, 4))
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    time.sleep(random.uniform(1, 3))
    search_box.send_keys(Keys.RETURN)
    time.sleep(random.uniform(5, 7))  # Wait for search results to load

    # Function to scroll the page smoothly
    def smooth_scroll():
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(random.uniform(2, 4))

    # Scroll at specific intervals
    time.sleep(15)
    smooth_scroll()
    time.sleep(15)
    smooth_scroll()
    time.sleep(70)
    smooth_scroll()

# Function to get trending search words from Google Trends
def get_trending_searches():
    url = "https://trends.google.co.in/trends/trendingsearches/daily?geo=IN"
    response = requests.get(url)
    trends_data = response.json()
    search_queries = [trend['title']['query'] for trend in trends_data['trendingSearchesDays'][0]['trendingSearches']]
    return search_queries[:35]  # Limit to top 35 trending searches

# Main script
login_to_bing()
search_queries = get_trending_searches()

for query in search_queries:
    time.sleep(15)  # Pause before each search
    perform_search(query)
    time.sleep(15)  # Pause after each search
    time.sleep(random.uniform(170, 190))  # Wait for 170-190 seconds before the next search

driver.quit()

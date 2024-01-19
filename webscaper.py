from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
import re
from datetime import datetime
import subprocess

FLIGHT_URL= 'https://www.flighthub.com/flight/search?num_adults=1&num_children=0&num_infants=0&num_infants_lap=0&seat_class=Economy&seg0_date=2024-05-01&seg0_from=NYC&seg0_to=MOW&seg1_date=2024-05-31&seg1_from=MOW&seg1_to=NYC&type=roundtrip'
# Path to the WebDriver executable
driver_path = '/home/toppk/apps/chrome-linux64'

# Initialize WebDriver
driver = uc.Chrome()

# Open the website
driver.get(FLIGHT_URL)

# Wait for the page to load
time.sleep(20)

# TODO: Add any necessary steps to navigate to the specific page containing the table

# Locate the table (example: using XPath)
# Note: You need to replace '//path_to_table' with the actual path to the table
table = driver.find_element(By.XPATH, '//*[@id="fares-search-package-list"]')

# Read data from the table
# This is a simple example. You'll need to adjust it based on the actual table structure
rows = table.find_elements(By.TAG_NAME, 'ul')

cells = rows[0].find_elements(By.TAG_NAME, 'li')
lines = cells[0].text.splitlines()
value = float(re.sub(r'[^\d.]', '', lines[4]))
if value < 1000 :
    message=f"price {value}"
    recipient="+16465268677"
    subprocess.run(["signal-cli", "-a", "+13479036038", "send", "-m", message, recipient])
    #send email here 

print(f"Time: {datetime.now()} Price :{value}")

 
#for row in rows:
#    cells = row.find_elements(By.TAG_NAME, 'li')
#    for cell in cells:
        #print(cell.text)
    

# Close the browser
driver.quit()
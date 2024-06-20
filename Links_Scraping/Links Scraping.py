from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

browser = webdriver.Firefox()

url = 'https://www.hespress.com/tamazight'
browser.get(url)

def scroll_down():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

for _ in range(300):
    scroll_down()

contents = []

# Find all elements that contain either the title and link information or the date and time information
title_elements = browser.find_elements(By.CLASS_NAME, 'stretched-link')
date_time_elements = browser.find_elements(By.CLASS_NAME, 'date-card')

# Match title and link elements with date and time elements based on their positions
for i in range(len(title_elements)):
    title_element = title_elements[i]
    date_time_element = date_time_elements[i]

    title = title_element.get_attribute('title')
    links = title_element.get_attribute('href')
    page_id = links.split('/')[-1].split('.')[0]
    date_time = date_time_element.find_element(By.CLASS_NAME, 'time').text

    items = {
        'title': title,
        'category':'تمازيغت',
        'date_time': date_time,
        'links': links,
        'page_id': page_id
    }
    contents.append(items)

df = pd.DataFrame(contents)
df.to_excel('tamazight_links.xlsx', index=False)

browser.quit()

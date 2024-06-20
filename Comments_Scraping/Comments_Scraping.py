from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

browser = webdriver.Firefox()

df_links = pd.read_excel('tamazight_links.xlsx')

all_data = []   

for index, row in df_links.iterrows():
    url = row['links']
    title = row['title']
    category = 'تمازيغت'
    browser.get(url)
    comments = browser.find_elements(By.CLASS_NAME, 'comment-text')
    reacts = browser.find_elements(By.CLASS_NAME, 'comment-recat-number')
    time.sleep(2)
    
    for comment, react in zip(comments, reacts):
        data = {
            'title': title,
            'comment': comment.text,
            'reacts': react.text,
            'category': category,
        }
        
        all_data.append(data)

browser.quit()

df_combined = pd.DataFrame(all_data)
df_combined.to_excel('tamazight.xlsx', index=False)

print(df_combined)

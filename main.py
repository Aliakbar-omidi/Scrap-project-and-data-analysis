import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

all_news_dict = []

url = "https://akharinkhabar.ir/"

for group in ["sport", "social", "money"]:
    driver = webdriver.Chrome()
    driver.get(f"{url}/{group}")

    news_list = driver.find_elements(By.CSS_SELECTOR, ".rectangle_container__rBE5L")

    for news in news_list:
        my_list = news.text.split("\n")
        news_dict = {
            "group": my_list[0],
            "time": my_list[2],
            "title": my_list[3],
            "like": my_list[4],
            "comments": my_list[5],
            "views": my_list[6],
        }
        all_news_dict.append(news_dict)

driver.close()

df = pd.DataFrame(all_news_dict)
df.to_excel("news.xlsx", index=False)

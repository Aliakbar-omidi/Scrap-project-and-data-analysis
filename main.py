import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


all_news_dict = []

url = "https://akharinkhabar.ir/"

for group in ["sport", "social", "money"]:
    driver = webdriver.Chrome()
    driver.get(f"{url}/{group}")

    news_list = driver.find_elements(By.CSS_SELECTOR, ".rectangle_container__rBE5L")

    # for link in driver.find_elements(By.CSS_SELECTOR, ".rectangle_image_container__OCyhG a"):
    #     try:
    #         link = link.get_attribute("href")
    #         driver.get(link)
    #     except:
    #         pass

    for news in news_list:
        my_list = news.text.split("\n")
        # print(my_list)
        news_dict = {
            "group": my_list[0],
            "time": my_list[2],
            "title": my_list[3],
            "like": my_list[4],
            "comments": my_list[5],
            "views": my_list[6],
        }
        all_news_dict.append(news_dict)
        print(all_news_dict)

driver.close()


import pandas as pd

df = pd.DataFrame(all_news_dict)
df.to_excel("news.xlsx", index=False)
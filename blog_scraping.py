# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:41:06 2019

@author: Kubus
"""
import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        title = article.find("a").get_text()
        href = article.find("a")["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, href, date])
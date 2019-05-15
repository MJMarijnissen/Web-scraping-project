# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:03:23 2019

Goes to books.toscrape.com and scrapes book title, price and rating to SQL database

@author: Kubus
"""

import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books= soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    print(all_books)
    return(all_books)
    
def create_book_table():
    """call only once to initiate table in .db"""
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute("CREATE TABLE books (title TEXT, price REAL, rating INT);")
    connection.commit()
    connection.close()

def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
   # c.execute("CREATE TABLE books (title TEXT, price REAL, rating INT);")
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()
    
def convert(str):
    conv = {"One": 1, 
            "Two": 2, 
            "Three": 3, 
            "Four": 4, 
            "Five": 5
            }
    return conv[str]

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    price = float(price[2:])
    return price

def get_rating(book):
    paragraph = book.select(".star-rating")[0]
    return convert(paragraph.get_attribute_list("class")[1])
    
#    
all_books = scrape_books("http://books.toscrape.com/")
#create_book_table() # run only first time to create database!!
save_books(all_books)

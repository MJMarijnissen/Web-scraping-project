# -*- coding: utf-8 -*-
"""
Created on Wed May  7 21:05:18 2019

@author: Kubus
"""
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import randint

url = "https://icanhazdadjoke.com/search"


title = figlet_format("DAD JOKE RETRIEVER!")
title = colored(title, color="blue")
print(title)

print(f"Source: icanhazdadjoke.com")

user_input = input("Give me a topic: ")
#response = requests.get(url, headers = {"Accept":"text/plain"})
while user_input != "q":
    response = requests.get(
            url, 
            headers = {"Accept":"application/json"},
            params={"term": user_input,
                    #"limit":20
                    }
)

    data = response.json()
    jokes = len(data['results'])

    if jokes:
        print(f"I've found {jokes} jokes! Picking one random.")
        pick = randint(0,jokes-1)
        #print(f"Your request to {url} came back with status code {response.status_code}")
        #print(response.text)
        #print(response.json())

        print(f"ID: {data['results'][pick]['id']}")
        print(data['results'][pick]['joke'])
        user_input = input("Another topic, or press q to quit: ")
    else:
        user_input = input("Couldn't find any, please pick something else (press q to quit): ")
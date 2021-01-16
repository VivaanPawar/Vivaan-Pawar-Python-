import requests
import base64

import tkinter as tk

def get_html_data(url):
    data= requests.get(url)
    return data

def get_covid_data():
    url("https://www.worldometers.info/coronavirus/")
    html_data = get_html_data(url)
    bs=base64(html_data.text,"html.parser")
    print(bs)



get_covid_data()

        
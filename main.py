import requests

from pickle import dump, load

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get("https://funpay.com/account/login")



# Вход на funpay

elem = browser.find_element(By.NAME, "login")
elem.send_keys("momojaja337@gmail.com")
elem = browser.find_element(By.NAME, "password")
elem.send_keys("AndroidDinamo")
sleep(4)


# Заходим на "мои продажи и ждем покупки"
def parcer_chats():
    funpay_url_chat = "https://funpay.com/chat/"
    sleep(2)
    browser.get(funpay_url_chat)

    full_html = browser.page_source

    soup = BeautifulSoup(full_html, "lxml")
    return soup

soup = parcer_chats()

all_chats = soup.find("div", class_="contact-list custom-scroll")
with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
    f.write(str(all_chats))
sleep(2)
while True:
    sleep(2)
    all_chats = soup.find("div", class_="contact-list custom-scroll")
    with open("C:\\vscodepj\\funpay_bot\\html_file2.txt", "w", encoding="utf-8") as f:
        f.write(str(all_chats))
    with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", 'r', encoding='utf-8') as f1, open("C:\\vscodepj\\funpay_bot\\html_file2.txt", 'r', encoding='utf-8') as f2:
        if f1.read() == f2.read():
            print("Все четенько")
            continue
        else:
            soup = parcer_chats()
            print("mamakriminal")
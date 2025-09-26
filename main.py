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
input()


# Заходим на "мои продажи и ждем покупки"
def parcer_chats():
    sleep(2)
    browser.refresh
    full_html = browser.page_source
    soup = BeautifulSoup(full_html, "lxml")
    return soup
browser.get("https://funpay.com/chat/")
soup = parcer_chats()
all_chats = soup.find("div", class_="contact-list custom-scroll")

with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
    f.write(str(all_chats.text))
sleep(2)
while True:
    sleep(2)
    soup = parcer_chats()
    sleep(1)
    all_chats = soup.find("div", class_="contact-list custom-scroll")
    with open("C:\\vscodepj\\funpay_bot\\html_file2.txt", "w", encoding="utf-8") as f:
        f.write(str(all_chats.text))
    with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", 'r', encoding='utf-8') as f1, open("C:\\vscodepj\\funpay_bot\\html_file2.txt", 'r', encoding='utf-8') as f2:
        if f1.read() == f2.read():
            print("Все четенько")
            content2 = all_chats.text
            content2 = str(content2).split()
            if content2[1] == "/help":
                print("Нужна помощь!")
            sleep(2)
            
            continue
        else:
            soup = parcer_chats()
            browser.refresh()
            sleep(2)
            print("не четенько")
            
            with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
                f.write(str(all_chats.text))
            content2 = all_chats.text
            content2 = str(content2).split()
    #         if content2[1] == "/people":
    #             chat_find = all_chats.find("a").get("href")
    #             elem = browser.find_element(By.NAME, "content")
    #             elem.send_keys("Понял! Сейчас отправлю уведомление продавцу, и если он не спит, то сразу ответит.")
    #             elem.send_keys(Keys.RETURN)
    #         else:
    #             chat_find = all_chats.find("a").get("href")
                
    #             elem = browser.find_element(By.NAME, "content")
    #             elem.send_keys("""Привет. Я - бот созданный KiWlide и хочу помочь тебе, мой дорогой покупатель.
    # Если хочешь позвать человека, то напиши /people
    # Если у тебя нет вопросов, то и писать ничего не нужно).""")
    #             elem.send_keys(Keys.RETURN)
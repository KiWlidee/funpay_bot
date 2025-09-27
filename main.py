from datetime import datetime

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


def first_file_w():
    global content2
    soup = parcer_chats()
    browser.refresh()
    sleep(1.5)
    all_chats = soup.find("div", class_="contact-list custom-scroll")
    with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
        f.write(str(all_chats.text))

    content2 = all_chats.text
    content2 = str(content2).split()

def chat_link_logs(word):
    chat_find = all_chats.find("a").get("href")
    if word == "/people":
        with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Позвали человека. Ссылка на чат - {chat_find}\n")  #  Записываем логи
    elif word == "/new_message":
        with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Пришло новое сообщение. Ссылка на чат - {chat_find}\n")  #  Записываем логи
    elif word == "/rent":
        with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Купили аренду. Ссылка на чат - {chat_find}\n")  #  Записываем логи
    return chat_find


def parcer_chats():  #  Парсим html код со страницы чатов
    sleep(1.5)
    browser.get("https://funpay.com/chat/")
    full_html = browser.page_source
    soup = BeautifulSoup(full_html, "lxml")
    return soup

# Заходим в чаты
browser.get("https://funpay.com/chat/")
soup = parcer_chats()
all_chats = soup.find("div", class_="contact-list custom-scroll")  #  Снова парсим отдельно чаты

with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
    f.write(str(all_chats.text))
sleep(1.5)  #  Записываем в первый файл наши только что скрепенные данные
while True:
    sleep(1.5)
    soup = parcer_chats()
    sleep(1.5)
    all_chats = soup.find("div", class_="contact-list custom-scroll")
    with open("C:\\vscodepj\\funpay_bot\\html_file2.txt", "w", encoding="utf-8") as f:
        f.write(str(all_chats.text))
    with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", 'r', encoding='utf-8') as f1, open("C:\\vscodepj\\funpay_bot\\html_file2.txt", 'r', encoding='utf-8') as f2:
        if f1.read() == f2.read():  #  Сравниваем данные с первого файла и с самого нового. Смотрим на изменения.
            content2 = all_chats.text
            content2 = str(content2).split()
            continue
        else:
            soup = parcer_chats()
            browser.refresh()
            sleep(1.5)

            first_file_w()
            if content2[1] == "/people":
                chat_find = chat_link_logs("/people")

                browser.get(chat_find)
                
                elem = browser.find_element(By.NAME, "content")
                elem.send_keys("Понял! Сейчас отправлю уведомление продавцу, и если он не спит, то сразу ответит. " \
                "Больше ничего писать не нужно.")
                with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - Позвали человека. Ссылка на чат - {chat_find}\n")  #  Записываем логи
                elem.send_keys(Keys.RETURN)
                soup = parcer_chats()
                browser.refresh()
                #
                first_file_w()
                #
            elif content2[1] == "/rent":
                chat_find = chat_link_logs("/rent")
            else:
                chat_find = chat_link_logs("/new_message")

                browser.get(chat_find)
                sleep(1.5)
                elem = browser.find_element(By.NAME, "content")
                elem.send_keys("""Привет. Я - бот созданный KiWlide и хочу помочь тебе, мой дорогой покупатель.
    Вот список команда, для управления:
    Позвать человека - /people
    Вы купили у меня аренду аккаунта? - /rent
    Если у Вас нет вопросов, то и писать ничего не нужно. Не стоит мне спамить, быстрее я не отвечу.""")

                elem.send_keys(Keys.RETURN)
                first_file_w()
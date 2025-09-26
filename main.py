import requests

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


# Заходим в чаты
def parcer_chats():  #  Парсим html код со страницы чатов
    sleep(2)
    browser.get("https://funpay.com/chat/")
    full_html = browser.page_source
    soup = BeautifulSoup(full_html, "lxml")
    return soup
browser.get("https://funpay.com/chat/")
soup = parcer_chats()
all_chats = soup.find("div", class_="contact-list custom-scroll")  #  Снова парсим отдельно чаты

with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
    f.write(str(all_chats.text))
sleep(2)  #  Записываем в первый файл наши только что скрепенные данные
while True:
    sleep(2)
    soup = parcer_chats()
    sleep(1)
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
            sleep(2)
            with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} - Пришло новое сообщение. Ссылка на чат - {chat_find}\n")  #  Записываем логи
            
            with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
                f.write(str(all_chats.text))

            content2 = all_chats.text
            content2 = str(content2).split()

            if content2[1] == "/people":
                chat_find = all_chats.find("a").get("href")
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
                sleep(2)
                all_chats = soup.find("div", class_="contact-list custom-scroll")
                with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
                    f.write(str(all_chats.text))

                content2 = all_chats.text
                content2 = str(content2).split()
                #
            elif content2[1] == '/error':
                chat_find = all_chats.find("a").get("href")
                browser.get(chat_find)
                elem = browser.find_element(By.NAME, "content")
                elem.send_keys("""Вот самые распрастраненные ошибки:
Ошибка 0x8007003B

Пробуйте:
1) Включить впн
2) Перезаходить в microsoft store, до тех пор, пока не исчезнет ошибка
3) Перезагрузить роутер или зайти в cmd от имени администратора и эту команду ввести ipconfig /flushdns, потом перезагрузить пк.

0x80190001
(Обычно помогает просто сбросить кэш(2) и включил впн)

1. Проверьте интернет-соединение: Убедитесь, что ваше интернет-соединение стабильно и работает правильно. 
2. Сбросьте кэш Microsoft Store: Нажмите Win + R, введите wsreset.exe и нажмите Enter. 
3. Проверьте настройки сети: Убедитесь, что настройки DNS-сервера установлены правильно или попробуйте сбросить сетевые настройки. 
4. Перезапустите службу обновлений Windows: В поиске введите "Службы" и найдите службу "Центр обновления Windows". Перезапустите ее. 
5. Проверьте настройки брандмауэра и антивируса: Убедитесь, что они не блокируют доступ к приложениям Microsoft. 
6. Перезагрузите компьютер: Простая перезагрузка может решить временные проблемы. 
7. Проверьте настройки времени и даты: Неправильные настройки времени и даты могут привести к проблемам с подключением к серверам Microsoft.
Ссылка на решение большенства проблем и ошибок - https://teletype.in/@shiski/vWbPBDa6l1m""")
                elem.send_keys(Keys.RETURN)

                with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - Xbox Error. Ссылка на чат - {chat_find}\n")  #  Записываем логи

                sleep(1)
                all_chats = soup.find("div", class_="contact-list custom-scroll")
                with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
                    f.write(str(all_chats.text))

                content2 = all_chats.text
                content2 = str(content2).split()
                sleep(1)
            else:
                chat_find = all_chats.find("a").get("href")
                browser.get(chat_find)
                sleep(2.5)
                elem = browser.find_element(By.NAME, "content")
                elem.send_keys("""Привет. Я - бот созданный KiWlide и хочу помочь тебе, мой дорогой покупатель.
    Вот список команда, для управления:
    Позвать человека - /people
    Если ты купил у меня подписку xbox и у тебя появились ошибки - /error
    Если у тебя нет вопросов, то и писать ничего не нужно.""")
                with open("C:\\vscodepj\\funpay_bot\\logs.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - Стартовое сообщение. Ссылка на чат - {chat_find}\n")  #  Записываем логи
                elem.send_keys(Keys.RETURN)
                #
                soup = parcer_chats()
                browser.refresh()
                sleep(2)
                all_chats = soup.find("div", class_="contact-list custom-scroll")
                with open("C:\\vscodepj\\funpay_bot\\html_file1.txt", "w", encoding="utf-8") as f:
                    f.write(str(all_chats.text))

                content2 = all_chats.text
                content2 = str(content2).split()
                #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import pytest
import time
import math



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_buttton(browser):
    browser.get(link)
    time.sleep(15)
    btn = browser.find_element(By.CLASS_NAME, 'btn, btn-lg, btn-primary, btn-add-to-basket')
    assert btn != None, "Кнопка добавления в корзину отсутствует"
    # Ниже строчка для запуска через терминал. Не забудьте выбрать необходимый язык (ru, en, fr, es)
    # py -m pytest -s -v --language=ru test_items.py
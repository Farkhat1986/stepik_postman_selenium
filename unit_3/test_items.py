from selenium.webdriver.common.by import By
import pytest
import time




link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_buttton(browser):
    browser.get(link)
    time.sleep(15)
    btn = browser.find_element(By.CLASS_NAME, 'btn, btn-lg, btn-primary, btn-add-to-basket')
    assert btn != None, "Кнопка добавления в корзину отсутствует"
    # Ниже строчка для запуска через терминал. Не забудьте выбрать необходимый язык (ru, en, fr, es)
    # py -m pytest -s -v --language=ru test_items.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn= browser.find_element(By.CLASS_NAME, 'trollface, btn, btn-primary').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    print (browser.window_handles)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    btn = browser.find_element(By.CLASS_NAME, 'btn, btn-primary').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# go to main page
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

# locators
    MGCL_BTN = "button.btn.btn-primary"; NMBR = "span.nowrap#input_value"
    RSLT_FLD = "input#answer[type='text']"; SBMT_BTN = "button[type='submit'].btn.btn-primary"

# click on the magical button
    button = browser.find_element(By.CSS_SELECTOR, MGCL_BTN)
    button.click()

# accept the alert  and click on the magical button
    confirm = browser.switch_to.alert
    confirm.accept()

# count the number to send as a result
    def calc(x):
        res = math.log(abs(12 * math.sin(int(x))))
        return str(res)

# extract the number from the page and count the result to send to field
    nmbr = browser.find_element(By.CSS_SELECTOR, NMBR)
    x = float(nmbr.text)
    y = calc(x)

# send result to the field
    result = browser.find_element(By.CSS_SELECTOR, RSLT_FLD)
    result.clear(); result.send_keys(y)

# submit the form
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
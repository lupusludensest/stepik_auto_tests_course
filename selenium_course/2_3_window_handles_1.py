import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# go to main page
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    wait = WebDriverWait(browser, 15)

# locators
    FLYN_BTN = "button[type='submit'].trollface.btn.btn-primary"; NMBR = "span.nowrap#input_value"
    RSLT_FLD = "input#answer[type='text']"; SBMT_BTN = "button[type='submit'].btn.btn-primary"

# click on the flying button
    button = browser.find_element(By.CSS_SELECTOR, FLYN_BTN)
    button.click()

# switch to new window using window_handles, since we know for sure we have two windows we choose 2d with index 1
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# count the number to send as a result
    def calc(x):
        res = math.log(abs(12 * math.sin(int(x))))
        return str(res)

# extract the number from the page and count the result to send to field
    nmbr = browser.find_element(By.CSS_SELECTOR, NMBR)
    x = float(nmbr.text)
    y = calc(x)
    print(y)

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
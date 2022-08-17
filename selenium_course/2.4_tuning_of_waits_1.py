import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# go to main page
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

# locators
    PRC_ICN = "h5#price[style='display:inline;float:right']"; BK_BTN = "button#book"
    NMBR = "span.nowrap#input_value"; RSLT_FLD = "input#answer[type='text']";
    SBMT_BTN = "button[type='submit'].btn.btn-primary"

    # wait for the price to be displayed would be $100, wait <= 12 sec
    prc_icn = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, PRC_ICN), '100'))

# click on the book button
    button = browser.find_element(By.CSS_SELECTOR, BK_BTN)
    button.click()

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
    # browser.quit()
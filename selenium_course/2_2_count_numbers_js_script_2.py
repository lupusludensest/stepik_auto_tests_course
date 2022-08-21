from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# go to main page
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

# locators
    NMBR = "span.nowrap#input_value"; RSLT_FLD = "input#answer[type='text']"
    IM_RBT_CHK_BX = "input.form-check-input#robotCheckbox"; RBT_RL = "input.form-check-input#robotsRule"
    SBMT_BTN = "button[type='submit'].btn.btn-primary"


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

# scroll page down to the submit button to make it ready to click
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# mark checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, IM_RBT_CHK_BX)
    checkbox.click()

# mark radio button "Robots rule"
    radio = browser.find_element(By.CSS_SELECTOR, RBT_RL)
    radio.click()

# submit the form
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
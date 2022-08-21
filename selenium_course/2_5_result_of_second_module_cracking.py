from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://stepik.org/learn?auth=login"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Логинимся
time.sleep(30)
browser.find_element(By.ID, "id_login_email").send_keys('gurovvic@gmail.com')
browser.find_element(By.ID, "id_login_password").send_keys('MyUSA2016!@')
browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

# переходим на страницу теста
time.sleep(8)
browser.get('https://stepik.org/lesson/236205/step/2?unit=208637')
time.sleep(12)

# Кликаем чек-боксы отправляем результат
browser.find_element(By.CSS_SELECTOR, ".ember-view[data-type='choice-quiz'] .s-checkbox:nth-child(1)").click()
browser.find_element(By.CSS_SELECTOR, ".ember-view[data-type='choice-quiz'] .s-checkbox:nth-child(2)").click()
browser.find_element(By.CSS_SELECTOR, ".ember-view[data-type='choice-quiz'] .s-checkbox:nth-child(3)").click()
browser.find_element(By.CSS_SELECTOR, ".ember-view[data-type='choice-quiz'] .s-checkbox:nth-child(4)").click()
time.sleep(8)
browser.find_element(By.CSS_SELECTOR, "button.submit-submission[type='button']").click()

# Тест выполнен неверно что 99%, делаем условие и цикл
browser.find_element(By.CLASS_NAME, "again-btn").text == 'Solve again'
browser.find_element(By.CLASS_NAME, "again-btn").click()
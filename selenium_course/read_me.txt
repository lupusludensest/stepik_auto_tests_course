# Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
# Три способа задать путь к файлу:

# 1. вбить руками
element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

# 2. задать с помощью переменных
# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)

# отправляем файл
element.send_keys(file_path)

# 3.путь автоматизатора.
#если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os

# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)

# отправляем файл
element.send_keys(file_path)

# итоговый код:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

# Общее

http://chromedriver.chromium.org/getting-started
https://www.guru99.com/selenium-tutorial.html
# — Туториал на английском, ориентирован на Java.
https://www.guru99.com/live-selenium-project.html
# — Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
http://barancev.github.io/good-locators/
# — что такое хорошие селекторы
http://barancev.github.io/what-is-path-env-var/
# — что за PATH переменная?

# Ожидания в Selenium WebDriver

https://www.selenium.dev/documentation/webdriver/waits/
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://blog.codeship.com/get-selenium-to-wait-for-page-load/
http://barancev.github.io/slow-loading-pages/
http://barancev.github.io/page-loading-complete/

# Хороший репо

https://github.com/ElenaProkorym/stepik_auto_tests_course

# Полезные ссылки по Гиту
# Настоятельно советуем самостоятельно прочитать про ветки (бранчи) и пулл-реквесты — это основной инструмент
# коллективной работы в Git.

https://learngitbranching.js.org/
# — отличный интерактивный туториал

https://git-scm.com/book/ru/v2/
# — лучшая книга вообще

https://hyperskill.org/learn/topic/257/

https://stepik.org/course/4138/

https://stepik.org/course/3145/

http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html

https://habr.com/company/intel/blog/344962/

https://githowto.com/ru

# Руководство про написание юнит-тестов в Python:

https://realpython.com/python-testing/

# PyTest: правила запуска тестов
# В этом шаге мы коротко обсудим важные особенности запуска тестов с помощью PyTest.
# Когда мы выполняем команду pytest, тест-раннер собирает все тесты для запуска по
# определенным правилам:
# * если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер
# начнёт поиск в текущей директории
# * как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например:

pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

pytest test_user_interface.py
# найти и выполнить все тесты в файле

pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

# Если запустить PyTest с параметром -v (verbose, то есть подробный),
# то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:
# Другие полезные команды для манипуляции выводом тестов PyTest можно найти по ссылке: https://gist.github.com/amatellanes/12136508b816469678c2.
# настроить запуск тестов, чтобы информация не выводилась можно например добавить флаг --tb=line
# параметр -s, чтобы увидеть текст, который выводится командой print()
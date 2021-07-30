# Запуск автотестов для разных языков интерфейса
from selenium.webdriver.chrome.options import Options
from Stepik.Nlo.conftest import *

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)
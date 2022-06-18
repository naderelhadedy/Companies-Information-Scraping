from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import sys

COMP_NAME = sys.argv[1]

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.linkedin.com/login')

browser.find_element_by_css_selector("#username").send_keys("user_name-OR-mobile_phone")
browser.find_element_by_css_selector("#password").send_keys("password")
browser.implicitly_wait(3)

browser.find_element_by_css_selector(".login__form_action_container button").click()
browser.implicitly_wait(5)

# search_input = browser.find_element_by_css_selector
# ("#global-nav-typeahead .search-global-typeahead__input always-show-placeholder")
# search_input.send_keys("paymob")
# search_input.submit()
# browser.implicitly_wait(3)

browser.get(f'https://www.linkedin.com/company/{COMP_NAME}/people/')
browser.implicitly_wait(20)
browser.find_element_by_css_selector("#people-search-keywords").send_keys("We are here")
browser.implicitly_wait(3)

src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

with open(f"{COMP_NAME}_soup.html", "w", encoding='utf-8') as file:
    file.write(str(soup))

browser.close()

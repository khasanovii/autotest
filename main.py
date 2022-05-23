import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get('https://www.yandex.ru/')
# closing modal window
modal_close = driver.find_element(By.CLASS_NAME, 'modal__close')
# wait time for loading data
time.sleep(15)
webdriver.ActionChains(driver).click(modal_close).perform()
# end closing modal window
# begin search input for search information
input = driver.find_element(By.CLASS_NAME, 'input__input')
# input word for search
input.send_keys('тензор')
# search suggest table
suggest = driver.find_element(By.CLASS_NAME, 'mini-suggest__popup_visible')
# check visible or hidden suggest table
if(suggest.text != '') : 
	print(suggest.text)
	print('suggest visible')
else : 
	print('suggest not visible')
# press enter button on keyboard for begin search
input.send_keys(Keys.ENTER)
# after opening begin search first link, first we find content table with result url 
content_left = driver.find_element(By.CLASS_NAME, 'content__left')
# get list ul
ul = content_left.find_element(By.TAG_NAME, 'ul')
# get list element li with data-attribute
li = ul.find_element(By.CSS_SELECTOR, 'li[data-cid="1"]')
# get link a
a = li.find_element(By.TAG_NAME, 'a')
# get href for check url 
url = a.get_attribute("href")
# check url
if(url == 'https://tensor.ru/'):
	print("First link ", url)
else :
	print("Another link")

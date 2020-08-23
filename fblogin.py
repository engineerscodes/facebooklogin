from selenium import webdriver
from time import sleep
username='enter your email adrress'#plz enter ur username in name eg ="sudha123@gmail.com"
password='enter your password'#plz enter ur passowrd in password eg ="12345@qweerr"
url='https://www.facebook.com'
driver=webdriver.Chrome("C:\\Users\\HP\\PycharmProjects\\facebooklogin\\chromedriver.exe")
driver.get(url)
sleep(1)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name('login').click()

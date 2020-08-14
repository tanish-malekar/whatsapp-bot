from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

contact_name="name"
driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Desktop\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
a = input("Press enter after scaning QR code")
inp_xpath_search = " //div[@class='_3FRCZ copyable-text selectable-text']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact_name)
time.sleep(2)
user = driver.find_element_by_xpath("//span[@title='{}']".format(contact_name))
user.click()
chat = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(500):
    chat.send_keys("Guess who learned to automate whatsapp using Python")
    chat.send_keys(Keys.RETURN)
import Tkinter
import tkMessageBox
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



top = Tkinter.Tk()

def StartSpam():
	driver.get(URL)
	link = driver.find_elements_by_class_name("voteDo")
	button = link[0]

B = Tkinter.Button(top, text ="Start", command = StartSpam)

B.pack()
top.mainloop()

def get_clear_browsing_button(driver):
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_data(driver):
	driver.get('chrome://settings/clearBrowserData')
	timeout = 500	
	wait = WebDriverWait(driver, timeout)
	wait.until(get_clear_browsing_button)
	btn = get_clear_browsing_button(driver)
	btn.click()
	wait.until_not(get_clear_browsing_button)

PATH = "(path to chromedriver)/chromedriver" #chromedriver.exe if you are running windows
driver = webdriver.Chrome(PATH)


URL = "http://bagsh.mn/?t=5fd73a0057f8a9b3e582920b&fbclid=IwAR1Vvdj_GEdK039h9IfXZoW1slkhMM5B9sw2tV2Okb9wj89cs3at8PeNZsk"



while start:
	button.click()
	driver.delete_all_cookies()
	#there are 2 options
	#delete entire browser data *clear_data()* (but this method is slow)
	#or delete all cookies. (faster)



from tkinter import *   
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = False
button = None



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

PATH = "C:\\Users\\Batsukh\\Desktop\\chromedriver.exe"
#chromedriver.exe if you are running windows
driver = webdriver.Chrome(PATH)

URL = "http://bagsh.mn/?t=5fd73a0057f8a9b3e582920b&fbclid=IwAR1Vvdj_GEdK039h9IfXZoW1slkhMM5B9sw2tV2Okb9wj89cs3at8PeNZsk"

def START():
    start = True
    driver.get(URL)
    link = driver.find_elements_by_class_name("voteDo")
    button = link[0]
    
    while start:
        button.click()
        driver.delete_all_cookies()
        #there are 2 options
        #delete entire browser data *clear_data()* (but this method is slow)
        #or delete all cookies. (faster)

top = Tk()  
  
top.geometry("200x100")  
  

b = Button(top,command = START,text = "Start")  
b.pack(side=BOTTOM)  


top.mainloop()

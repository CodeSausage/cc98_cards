# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def time_delay(a):
	# --------延时模块----------
	driver.implicitly_wait(10)
	time.sleep(a)
	#--------------------

driver = webdriver.Chrome()
driver.get("https://card.cc98.org/")
On_Internet = 1

elem = driver.find_element_by_xpath("/html/body/nav[@class='navbar fixed-top navbar-expand-lg navbar-dark bg-dark']/div[@class='container']/div[@id='navbar-collapse-content']/ul[@class='navbar-nav']/li[@class='nav-item']/a[@class='nav-link']")
elem.click()
user_name = driver.find_element_by_id("UserName")
user_name.clear()
user_name.send_keys("Uninstall")
pass_word = driver.find_element_by_id("Password")
pass_word.clear()
pass_word.send_keys("123456grc")
login_btn = driver.find_element_by_class_name("btn-primary")
login_btn.click()
auth_btn = driver.find_element_by_class_name("btn-success")
auth_btn.click()
cards_btn = driver.find_element_by_xpath("/html/body/nav[@class='navbar fixed-top navbar-expand-lg navbar-dark bg-dark']/div[@class='container']/div[@id='navbar-collapse-content']/ul[@class='navbar-nav mr-auto']/li[@class='nav-item'][2]/a[@class='nav-link']")
cards_btn.click()
takeCards_btn = driver.find_element_by_xpath("/html/body/div[@class='container body-content']/div[@class='row justify-content-center']/div[@class='col-md-3 col-sm-4  text-center'][1]/div[@class='card']/div[@class='card-body']/a[@class='btn btn-primary']")
takeCards_btn.click()
begin_btn = driver.find_element_by_class_name("btn-primary")
begin_btn.click()
# 处理confirm弹窗
driver.switch_to_alert().accept()
time_delay(1)
while(1):
	# 全部翻开
	turnCards_btn = driver.find_element_by_class_name("btn-primary")
	turnCards_btn.click()
	# turnCards_btn = driver.find_element_by_xpath("/html/body/div[@class='container body-content']/div[@id='result-panel']/div[@class='text-center']/button[@class='btn btn-primary'][1]")
	# turnCards_btn.click()
	# 延时3秒，观察一下
	time_delay(3)
	# 再来一次
	onceMore_btn = driver.find_element_by_xpath("/html/body/div[@class='container body-content']/div[@id='result-panel']/div[@class='text-center']/button[@class='btn btn-primary'][2]")
	onceMore_btn.click()
	# 处理confirm弹窗
	driver.switch_to_alert().accept()
	time_delay(1)

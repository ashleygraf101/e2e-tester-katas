#!/usr/bin/env python

import pytest
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys,time,os
	
@pytest.mark.usefixtures("browser")
def test_add_user(browser):
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://thedemosite.co.uk/addauser.php') 
	#Check 1: Is the page title correct?
	
	#log in 
	username_field = browser.find_element_by_xpath("//input[@name='username']")
	username_field.send_keys('hello')
	password_field = browser.find_element_by_xpath("//input[@type='password']")
	password_field.send_keys('blank')
	submit_button = browser.find_element_by_xpath("//input[@type='button']") #Click on the Click me button
	submit_button.click()
	time.sleep(5)
	
	
	print (browser.current_url)
	
	if "savedata" in browser.current_url:
		print ("Success")
		pass_check_counter += 1
	else:
		print ("Failure")
	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter 

@pytest.mark.usefixtures("browser")
def test_no_login_attempt_alert(browser):	
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://thedemosite.co.uk/login.php') 
	#Check 1: Is the page title correct?
	
	status = browser.find_element_by_xpath("//font/center/b").text
	if (status == "**No login attempted**"):
		print ("Success")
		pass_check_counter += 1
	else:
		print ("Failure")
	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter 
	
@pytest.mark.usefixtures("browser")
def test_username_login_help_alert(browser):	
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://thedemosite.co.uk/login.php') 
	#Check 1: Is the page title correct?
	
	find_alert = browser.find_element_by_xpath("//a/small/small").click()
	ale = browser.switch_to.alert
	help_alert = ale.text;
	if (ale.text == "The username must be between 4 and 16 characters long."):
		print ("Success")
		pass_check_counter += 1
	else:
		print ("Failure")
	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter 
	
@pytest.mark.usefixtures("browser")
def test_login(browser):
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://thedemosite.co.uk/login.php') 
	#Check 1: Is the page title correct?

	username_field = browser.find_element_by_xpath("//input[@name='username']")
	username_field.send_keys('hello')
	password_field = browser.find_element_by_xpath("//input[@type='password']")
	password_field.send_keys('blank')
	submit_button = browser.find_element_by_xpath("//input[@type='button']") #Click on the Click me button
	submit_button.click()
	time.sleep(5)
	
	#status changes on login attempt
	status = browser.find_element_by_xpath("//font/center/b").text
	#assert status == ("**No login attempted**")
	print(status)
	
	#accomodate for someone trying to login with a different correct set of details after me
	if (status == "**Successful Login**" or status == "**Failed Login**"): 
		print ("Success")
		pass_check_counter += 1
	else:
		print ("Failure")
	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter 
	
if __name__=='__main__':
	browser = sys.argv[1] #Note:using sys.argv to keep this example short. We use OptionParser with all our clients
	test_add_user(browser)
	test_login(browser)
	test_username_login_help_alert(browser)
	test_no_login_attempt_alert(browser)
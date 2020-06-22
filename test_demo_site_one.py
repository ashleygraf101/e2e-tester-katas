#!/usr/bin/env python

import pytest
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys,time,os


@pytest.mark.usefixtures("browser")
def test_full_example_form(browser):
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://qxf2.com/selenium-tutorial-main') 
	#Check 1: Is the page title correct?
	if(browser.title == "Qxf2 Services: Selenium training main"):
		print ("Success: Title of the Qxf2 Tutorial page is correct")
		pass_check_counter += 1
	else:
		print ("Failed: Qxf2 Tutorial page Title is incorrect")
	total_checks += 1
 
	#Fill name, email and phone in the example form
	name_field = browser.find_element_by_xpath("//input[@type='name']")
	name_field.send_keys('Ashley')
	email_field = browser.find_element_by_xpath("//input[@type='email']")
	email_field.send_keys('test@example.com')
	phone_field = browser.find_element_by_xpath("//input[@type='phone']")
	phone_field.send_keys('89065034043569845')
	terms_field = browser.find_element_by_xpath("//input[@type='checkbox']")
	terms_field.click()
	gender_field = browser.find_element_by_xpath("//button[@type='button']")
	gender_field.send_keys('Female')
	submit_button = browser.find_element_by_xpath("//button[@type='submit']") #Click on the Click me button
	submit_button.click()
	
	#Check 2: Is the page title correct?
	if(browser.title == "Qxf2 Services: Selenium training redirect"):
		pass_check_counter += 1
		print ("Success: The example form was submitted. Automation is not on the redirect page")
	else:
		print ("Failure: The example form was not submitted")


	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter

@pytest.mark.usefixtures("browser")
def test_empty_example_form(browser):
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://qxf2.com/selenium-tutorial-main') 
	#Check 1: Is the page title correct?
	if(browser.title == "Qxf2 Services: Selenium training main"):
		print ("Success: Title of the Qxf2 Tutorial page is correct")
		pass_check_counter += 1
	else:
		print ("Failed: Qxf2 Tutorial page Title is incorrect")
	total_checks += 1
 
	#Fill name, email and phone in the example form
	name_field = browser.find_element_by_xpath("//input[@type='name']")
	name_field.send_keys('')
	email_field = browser.find_element_by_xpath("//input[@type='email']")
	email_field.send_keys('')
	phone_field = browser.find_element_by_xpath("//input[@type='phone']")
	phone_field.send_keys('')
	terms_field = browser.find_element_by_xpath("//input[@type='checkbox']")
	terms_field.click()
	gender_field = browser.find_element_by_xpath("//button[@type='button']")
	gender_field.send_keys('')
	submit_button = browser.find_element_by_xpath("//button[@type='submit']") #Click on the Click me button
	submit_button.click()
	
	name_error = browser.find_element_by_css_selector("label.error").text
	print (name_error)
	assert name_error == ("Please enter your name")
	
	#Check 2: Is the page title correct?
	if(browser.title == "Qxf2 Services: Selenium training redirect"):
		print ("Failure: The example form was submitted. Automation is not on the redirect page")
	else:
		print ("Success: The example form was not submitted")
		pass_check_counter += 1
	
	total_checks += 1
	
	#Quit the browser window
	browser.quit() 
 
	#Assert if the pass and fail check counters are equal
	assert total_checks == pass_check_counter
	
@pytest.mark.usefixtures("browser")
def test_click_from_hover_dropdown(browser):
	"Test example form"
 
	#Create variables to keep count of pass/fail
	pass_check_counter = 0
	total_checks = 0
 
	#Visit the tutorial page
	browser.get('http://qxf2.com/selenium-tutorial-main') 
	#Check 1: Is the page title correct?

	action = ActionChains(browser);

	firstLevelMenu = browser.find_element_by_xpath("/html/body/div[6]/ul/li[3]/a")
	action.move_to_element(firstLevelMenu).click()
	secondLevelMenu = browser.find_element_by_xpath("/html/body/div[6]/ul/li[3]/ul/li[7]/a")
	action.click(secondLevelMenu)
	action.perform()

	if (browser.title == "Qxf2 Services: DIY! GUI automation"):
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
	test_empty_example_form(browser)
	test_full_example_form(browser)
	test_click_from_hover_dropdown(browser)
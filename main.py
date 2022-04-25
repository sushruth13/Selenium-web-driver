#Test written to check if cb app generates output for following sequences - 

#1. Test with DManpa1-OH, because it is quick, and people tend to test with that first, 
#so it can be a test for reusing previous builds, which is important. It also should skip 
#the options page and go straight to downloads. If it takes time while it minimizes, 
#test it again to verify that reusing previous builds happens fast.


#2. Test with DManpa1-6DManpa1-6DManpa1-OH because it provides rotamer options, 
#meaning you will reach the options page. Also tends to be previously built. 
#If in a rush, select down to 2 builds. If being thorough, do more.

#NOTE- following test will only work on chrome

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import page
import os

webtest = "http://172.24.0.2/txt/"
#This class contains the test cases that needs to be performed
#You can create multiple of such classes, but one class should be able to handle one app
class GLYCAM_cb_testSuit(unittest.TestCase):

#this is like init method, whatever you will need in the program later can be 
#added in this method. This method is called before every test method executes, each time.
	#@classmethod
	#def setUpClass(self):
	def setUp(self):
		print("\n")
		print("************************************************************************")
		print("Setting up chrome driver")		
		options = Options()
		options.binary_location = "/usr/bin/google-chrome"
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		#print(os.getcwd())
		params = {'behavior':'allow','downloadPath':os.getcwd()}
		self.driver.execute_cdp_cmd('Page.setDownloadBehavior',params)
		#prefs = {'download.default_directory' : os.getcwd()}
		#options.add_experimental_option('prefs', prefs)
		self.driver.maximize_window()
		self.driver.get(webtest)		#Change this link after every start.sh/restart.sh
		print("\n")


#any method which starts with "test" keyword, will be treated as test

#demo test
	def demo_test_title(self):
		print("Reached:Does title matches")
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()

#The following test checks if cb app generates all the files successfully, skips options page. 
	def test_check_cb_flow1(self):
		print("Reached:CB app test1 | Building with text - DManpa1-OH | goodluck :)")
		mainPage = page.MainPage(self.driver)	
		mainPage.search_text_element = "DManpa1-OH"
		print("Reached:CB app test1 | Setting sequence name")
		mainPage.click_submit_button()
		print("Reached:CB app test1 | After submitting sequence")
		file_download_check = mainPage.click_download_all()
		print("Reached:CB app test1 | Download_all button is ready, all structures are minimized")
		time.sleep(3)
		assert file_download_check

#The following test checks if cb app hits options page and then generates all the files successfully.
	def test_check_cb_flow2(self):
		print("Reached:CB app test2 | Building with text - DManpa1-6DManpa1-6DManpa1-OH | goodluck :)")
		mainPage = page.MainPage(self.driver)	
		mainPage.search_text_element = "DManpa1-6DManpa1-6DManpa1-OH"
		print("Reached:CB app test2 | Setting sequence name")
		mainPage.click_submit_button()
		print("Reached:CB app test2 | Options page, click on generate seq")
		mainPage.check_gg()
		mainPage.check_gt()
		mainPage.check_tg()
		mainPage.click_generate_default_structures()
		print("Reached:CB app test2 | Downloads page")
		file_download_check = mainPage.click_download_all()
		print("Reached:CB app test2 | Download_all button is ready, all structures are minimized")
		time.sleep(3)
		assert file_download_check


#this is cleanup method, Just like setUp, it runs after each test case.
	#@classmethod
	#def tearDownClass(self):
	def tearDown(self):
		print("Bye!")
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()

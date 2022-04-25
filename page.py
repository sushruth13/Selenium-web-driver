from locator import *
from element import BasePageElement
#from selenium.webdriver.common.action_chains import ActionChains
import time


class SearchTextElement(BasePageElement):
	locator = "sequence_input"
#To access each web page, contains more of selenium code


#base class for all of the pages, we need to pass it a driver
class BasePage(object):			#@inheritance object is optional
	def __init__(self,driver):	#constructor that will help initialize driver for all the child pages
		self.driver = driver

class MainPage(BasePage):

	#attribute
	search_text_element = SearchTextElement()		#Creating a descriptor (to hide the functionality of underlying module/specific attribute)
	#every time we access the variable search_text_element (set/get) it will use the methods 
	#from element.py
	#MainPage is passed to the set method as obj, a value with it.   



	def is_title_matches(self):
		return "GLYCAM" in self.driver.title


	def click_submit_button(self):
		element = self.driver.find_element(*MainPageLocator.submit_btn)	#defined in locator.py
		#* stands for unpacking tuple, to separate into objects
		element.click()
	
	def check_gg(self):
		element = self.driver.find_element(*MainPageLocator.gg)	#defined in locator.py
		element.click()
		time.sleep(1)
	def check_gt(self):
		element = self.driver.find_element(*MainPageLocator.gt)	#defined in locator.py
		element.click()
		time.sleep(1)
	def check_tg(self):
		element = self.driver.find_element(*MainPageLocator.tg)	#defined in locator.py
		element.click()
		time.sleep(1)

	def click_generate_default_structures(self):
		element = self.driver.find_element(*MainPageLocator.generate_selected_structures_btn)
		element.click()

	def click_download_all(self):
		element = self.driver.find_element(*MainPageLocator.download_all)
		while True:
			if element.is_enabled():
				#print("Download button is ready ", element.is_enabled())
				element.click()
				#time.sleep(5)
				return True
		
		
		
class SearchResultPage(BasePage):
	def is_result_found(self):
		return "No results found" not in self.driver.page_source	
		
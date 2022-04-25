#This is a test scipt only to test implementation of selenium methods. Does not employ any unit test

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 		#gives access to keyboard keys. eg - we can search something in the search bar and hit enter key
from selenium.webdriver.common.by import By
#For waiting till the element clicked responds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

#driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

#options  = webdriver.ChromeOptions()
#driver = webdriver.Chrome(driver_location)
#options.binary_location =binary_location
#driver = webdriver.Chrome(executable_path = driver_location, chrome_options = options)
#driver.get("https://www.imdb.com")

options = Options() 	#used for customizing the ChromeDriver session
options.add_argument("start-maximized")
options.binary_location = binary_location
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get("https://glycam.org/lib/load/hmlib/")
driver.get("http://172.24.0.2/")
time.sleep(1)
#print(driver.page_source.encode('utf-8'))
print(driver.title)


#locating elements
#search = driver.find_element_by_name("query")  #DEPRECATED
#search = driver.find_element(By.NAME, "query")

#Search HTML elements and use keys on those elements
#Searching the sequence using "search" box field on the page 
# search.send_keys("DManpa1-3[DManpa1-2DManpa1-6DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH")
# search.send_keys(Keys.RETURN) 	#return is enter

#print(driver.page_source)  #to see the entire source code of website
#basically we can access anything


#Navigating through pages V3
#link = driver.find_element_by_link_text("3D Structure Libraries") 			#Deprecated
link = driver.find_element(by=By.LINK_TEXT, value="3D Structure Libraries")
link.click()
time.sleep(1)


#Navigating through pages -- Wait until element responds
try:
	#next page
	libCategory = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.LINK_TEXT,"hmlib"))
	)
	libCategory.click()
	time.sleep(1)
	
	#next page
	search = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.NAME, "query"))
	)
	search.clear()		#clear the text that is already inside the input field. Safe to use it when accessing search fields and sending text ahead with "send keys" because it doesnt replace it appends the keys. 
	search.send_keys("DManpa1-3[DManpa1-2DManpa1-6DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH")
	search.send_keys(Keys.RETURN) 
	time.sleep(1)

	#next page
	select= WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.ID, "680"))
	)
	select.click()
	time.sleep(1)

	#go back by 1 page
	driver.back()
	time.sleep(1)


	#go to home again
	driver.back()
	time.sleep(1)
	driver.back()
	time.sleep(1)
	driver.back()
	time.sleep(1)

	#can also use driver.forward() to go back to next pages
	
except:
	#driver.quit()
	print("I timed out")
	driver.quit()


time.sleep(1)
driver.quit()




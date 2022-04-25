# Selenium-web-driver
Basic selenium scripts with Python for https://glycam.org/ using chrome driver

# About Selenium - Web driver
- An Automated testing tool for web devolopement
- Version in use selenium==4.1.3
- You can directly execute main.py with python3 after cloning the reporsitory if you already have the necessary installations
- sel_test1 is just a mock created to test some of the functionalities offered by selenium

# Installation of selenium web driver for Ubantu | Python 
1. Please make sure your system already has pip3, Python3 installed. Selenium is JAVA based, so you will also need JRE 1.6 or abover installed.(use following to check "pip3 --version", "python3 --version",  "java" or "java --version").

2. Use "pip install selenium" to install python bindings for selenium. In case you run into issues try using command "sudo pip3 -U install selenium"


3. Use "pip3 freeze" and check if you can find selenium with version 4.1.3 or the latest one, in the list. If not use "selenium==4.1.3" to set it, and check again using "pip3 freeze"

# Installation of chrome driver

Next, we will have to install an web driver according to the browser that we need to test the website on. Currently testing on chrome, so we will have to install chrome driver. Note that firefox and other browsers will required separate installations of respective web drivers.

1. Check the version of installed google chrome using "google-chrome --version" 

2. Now you have to download the chrome driver as per your chrome browser version, refer to https://chromedriver.chromium.org/downloads for download. 

3. cd to the location where you your downloaded driver, and unzip the folder using "unzip chromedriver_linux64.zip" 

4. Move the driver to our environment using, "sudo mv chromedriver <your_preferref_directory>" 

5. cd to <your_preferred_directory> and give necessary permission to the driver, "chmod +x chromedriver"

6. Use "whereis google-chrome" to get the binary location of chrome. Create a symbolic link to chrome's binary location - "sudo ln -s chromedriver /usr/bin/google-chrome". Note- the last argument in this command is the binary location that we checked for before. If your location is different, replace it. 

7. Install driver using "sudo apt install chromium-chromedriver"

# Other dependencies
Before you start, execute following commands in order to setup other dependencies 

1. Getting Requests Python Package, "pip3 install --upgrade requests". If you dont have this package you might get the following error while executing selenium script - "urllib3 (1.26.9) or chardet (3.0.4) doesn't match a supported version!"

2. Getting web driver manager "pip3 install webdriver_manager"

# Basic test-script to check if all installations are done successfully
- Program
#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

binary_location = "/usr/bin/google-chrome"

options = Options()
options.binary_location = binary_location
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.uga.edu/")
time.sleep(1)
print(driver.title)
driver.quit()

- Output
Execute using - "python3 program_name.py"
You should be able to see a google chrome browser window launched on your screen with UGA home page. 

# Selenium unittest framework documentation
Useful links
- https://www.techbeamers.com/selenium-python-test-suite-unittest/#h1
- https://www.youtube.com/watch?v=9_5Wqgni_Xw
Official docs
- https://www.selenium.dev/selenium/docs/api/py/index.html
- https://selenium-python.readthedocs.io/installation.html


# Selenium - IDE
- https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started


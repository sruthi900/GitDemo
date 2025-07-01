import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--start-maximized")
#service_obj=Service("C:\\Users\\alsruthi\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
#driver=webdriver.Chrome(service=service_obj,options=chrome_options)

#driver=webdriver.Chrome(executable_path="C:\\Users\\alsruthi\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver=webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(3)
Countries=driver.find_elements(By.CSS_SELECTOR,"li[class= 'ui-menu-item'] a")
print(len(Countries))
for country in Countries:
    if country.text=="India":
        country.click()
        time.sleep(2)
        break

#passed through jave script get attribute as text wont work here for dynamically getting value
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"
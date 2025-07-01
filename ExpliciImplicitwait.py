import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
time.sleep(3)
count=driver.find_elements(By.XPATH,"//div[@class='products']/div") #list

result = len(count)
assert result > 0
for add in count:
    add.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt ='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("Rahulshetty")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
wait=WebDriverWait(driver,10)
msg=wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo"))).text
print(msg)

count=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in count:
    sum= sum+int(price.text)

print(sum)
TotalAmt=int(driver.find_element(By.CLASS_NAME,"totAmt").text)
assert sum==TotalAmt


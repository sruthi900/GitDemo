import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
Products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in Products:
    productName=product.find_element(By.XPATH,"./div/h4/a").text
    if productName == "Blackberry":
        time.sleep(10)
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Success=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success" in Success
driver.close()




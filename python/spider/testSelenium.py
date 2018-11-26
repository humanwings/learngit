from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
 
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
# print(driver.page_source)
driver.quit()
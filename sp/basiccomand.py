from selenium import webdriver
#from selenium.webdriver.common.keys import keys
import time

driver = webdriver.Firefox()
driver.get("https://in.ixl.com/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='qlsubmit']").click()
time.sleep(10)
driver.close()
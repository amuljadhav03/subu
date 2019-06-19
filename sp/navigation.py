from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get("https://in.ixl.com/")
s1= driver.title
s2= driver.current_url

print(s1)
print(s2)

driver.find_element_by_link_text('Membership').click()
print(driver.title)
print(driver.current_url)
driver.find_element_by_link_text('Join IXL').click()
print(driver.title)
print(driver.current_url)

driver.back()
print(driver.title)
print(driver.current_url)


driver.back()

time.sleep(20)

driver.close()
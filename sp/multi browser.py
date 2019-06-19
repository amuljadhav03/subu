from selenium import webdriver
# from selenium.webdriver.common.keys.import keys

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)


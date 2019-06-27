import pytest

@pytest.fixture(scope="class")

def webcontrol(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/amul.kumar.PTW-I/PycharmProjects/subu/Drivers/chromedriver.exe")
    driver.get("https://tt.ptw-i.com/Default")
    driver.implicitly_wait(30)
    request.cls.driver = driver
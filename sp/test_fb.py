from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_login():
    dr = webdriver.Chrome()
    dr.get("https://www.facebook.com/")
    dr.find_element_by_name("firstname").send_keys("Amul")
    dr.find_element_by_xpath('//*[@id="u_0_n"]').send_keys("kumar")
    dr.find_element_by_id('u_0_q').send_keys("amul.jadhav5@gmail.com")
    dr.find_element_by_xpath('//*[@id="u_0_x"]').send_keys('12345678')
    s = dr.find_element_by_name('day')
    day= Select(s)
    day.select_by_value('15')
    m =dr.find_element_by_xpath('//*[@id="month"]')
    month =Select(m)
    month.deselect_by_index('9')
    y = dr.find_element_by_name('birthday_year')
    year =Select(y)
    year.select_by_visible_text('1991')

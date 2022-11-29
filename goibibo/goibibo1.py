import time
from selenium import webdriver
import pytest

path = r'C:\Users\User\Desktop\drivers\chromedriver.exe'
driver_obj = webdriver.Chrome(path)
driver_obj.get(r'https://www.goibibo.com')
driver_obj.maximize_window()
time.sleep(2)


class Flights:
# one way
    def test_route(self):
        driver_obj.find_element_by_xpath('(//div[@class="sc-ieecCq koynXZ fswFld "])[1]').click()
        time.sleep(2)

    # from
    def test_from(self):
        driver_obj.find_element_by_xpath('//input[@type="text"]').send_keys("pune")
        time.sleep(2)
        driver_obj.find_element_by_xpath('(//div[@class="sc-dPiLbb eIvaEJ"])[1]').click()
        time.sleep(2)


    # to
    def test_to(self):
        driver_obj.find_element_by_xpath('//input[@type="text"]').send_keys("mumbai")
        time.sleep(2)
        driver_obj.find_element_by_xpath('(//div[@class="sc-dPiLbb eIvaEJ"])[1]').click()
        time.sleep(2)

    # dept date
    def test_date(self):
        driver_obj.find_element_by_xpath('(//div[@class="gr_fswFld active"])').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('//div[@aria-label="Sun Dec 18 2022"]').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('//span[@class="fswTrvl__done"]').click()
        time.sleep(2)

    # radio
    def test_fare(self):
        driver_obj.find_element_by_xpath('//span[text()="regular"]').click()
        time.sleep(2)

    # t&c
    def test_travellers(self):
        driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[2]').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[4]').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[6]').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('(//li[text()="business"])').click()
        time.sleep(2)
        driver_obj.find_element_by_xpath('//a[text()="Done"]').click()
        time.sleep(2)

    # search
    def test_search(self):
        driver_obj.find_element_by_xpath('//span[@class="sc-dtDOqo iuIbnZ"]').click()
        time.sleep(2)


cls = Flights()
cls.test_route()
cls.test_from()
cls.test_to()
cls.test_date()
cls.test_fare()
cls.test_travellers()
cls.test_search()






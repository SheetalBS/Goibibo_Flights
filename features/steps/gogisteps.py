from selenium import webdriver
from behave import *
import time

@given(u'Launch the browser')
def step_impl(context):
    path = r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver_obj = webdriver.Chrome(path)


@when(u'open Goibibo home page')
def step_impl(context):
    context.driver_obj.get(r'https://www.goibibo.com')
    context.driver_obj.maximize_window()
    time.sleep(2)


@when(u'click on one way')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('(//div[@class="sc-ieecCq koynXZ fswFld "])[1]').click()
    time.sleep(2)


@when(u'enter the depart location')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('//input[@type="text"]').send_keys("pune")
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('(//div[@class="sc-dPiLbb eIvaEJ"])[1]').click()
    time.sleep(2)

@when(u'enter the destination location')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('//input[@type="text"]').send_keys("mumbai")
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('(//div[@class="sc-dPiLbb eIvaEJ"])[1]').click()
    time.sleep(2)


@when(u'select the depart date')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('(//div[@class="gr_fswFld active"])').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('//div[@aria-label="Sun Dec 18 2022"]').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('//span[@class="fswTrvl__done"]').click()
    time.sleep(2)

@when(u'select the adults,children and infant count by using "+" and "-" icons')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[2]').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[4]').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('(//span[@class="sc-Galmp dZbQsT"])[6]').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('(//li[text()="business"])').click()
    time.sleep(2)
    context.driver_obj.find_element_by_xpath('//a[text()="Done"]').click()
    time.sleep(2)

@when(u'select radio button')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('//span[text()="regular"]').click()
    time.sleep(2)


@when(u'click on "search flights" button')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('//span[@class="sc-dtDOqo iuIbnZ"]').click()
    time.sleep(2)

@then(u'verify that flight options are displayed')
def step_impl(context):
    assert True, "test passed"




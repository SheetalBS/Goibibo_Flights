import pytest
import time
from selenium import webdriver
from Library.config_flights import ConfigFlights
from selenium.webdriver.firefox.options import Options




@pytest.fixture(params=["Firefox","Edge","Chrome"])
def _driver(request):
    global driver_obj
    if request.param == "Chrome":
        driver_obj = webdriver.Chrome(ConfigFlights.Chrome_Driver_Path)

    elif request.param == "Edge":
        driver_obj = webdriver.Edge(ConfigFlights.Edge_Driver_path)

    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver_obj = webdriver.Firefox(executable_path= ConfigFlights.Firefox_Driver_Path, options=options)


    driver_obj.get(r'https://www.goibibo.com')
    driver_obj.maximize_window()
    driver_obj.implicitly_wait(30)
    yield driver_obj

    time.sleep(5)
    driver_obj.close()
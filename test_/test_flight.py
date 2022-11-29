from POM.flightpage import Flights
import pytest
import xlrd
from Data import read_objects

data_obj = read_objects.read_data()


class Test_flights:
    @pytest.mark.parametrize("i",data_obj)
    def test_flights(self,_driver,i):
        fl = fl = Flights(_driver)
        fl.test_route()
        fl.test_from(i)
        fl.test_to(i)
        fl.test_date()
        fl.test_fare()
        fl.test_travellers()

        fl.test_search()
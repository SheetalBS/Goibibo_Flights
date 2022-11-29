import pytest
import time
from Data import read_objects


loc_obj = read_objects.read_locators()

class Flights:

    def __init__(self,driver_obj):
        self.driver_obj = driver_obj
# one way
    def test_route(self):
        self.driver_obj.find_element(*loc_obj["oneway_trip_from_textfield_btn"]).click()
        time.sleep(2)

    # from
    def test_from(self,i):
        self.driver_obj.find_element(*loc_obj['from_text_field']).send_keys(i[0])
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['oneway_trip_from_dropdown']).click()
        time.sleep(2)


    # to
    def test_to(self,i):
        self.driver_obj.find_element(*loc_obj['to_text_field']).send_keys(i[1])
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['oneway_trip_To_dropdown']).click()
        time.sleep(2)

    # dept date
    def test_date(self):
        self.driver_obj.find_element(*loc_obj['oneway_trip_deaparture_btn']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['deaparture_date']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['deaparture_date_done_btn']).click()
        time.sleep(2)

    # radio
    def test_fare(self):
        self.driver_obj.find_element(*loc_obj['faretype_regular_btn']).click()
        time.sleep(2)

    # t&c
    def test_travellers(self):
        self.driver_obj.find_element(*loc_obj['adult_increase_btn']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['children_increase_btn']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['infants_increase_btn']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['click_business_btn']).click()
        time.sleep(2)
        self.driver_obj.find_element(*loc_obj['click_done_btn']).click()
        time.sleep(2)

    # search
    def test_search(self):
        self.driver_obj.find_element(*loc_obj['search_flight_btn']).click()
        time.sleep(2)

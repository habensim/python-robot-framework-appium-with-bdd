import logging
import sys 
import os
current_directory = os.getcwd()
sys.path.append(current_directory)

from resources.module.homepage.Selector import *
from resources.helper.Element import *
from utils.Settings import driver
from appium.webdriver.common.mobileby import MobileBy
from robot.api import logger

class Homepage:
    def carousel_usp_swipe(self):
        selanjutnyabtn = get_element_presence_located_by_id(selanjutnya)
        selanjutnyabtn.click()
        lewatibtn = get_element_presence_located_by_id(skiponboarding)
        lewatibtn.click()

    def verify_header_element(self):
        driver.implicitly_wait(10)
        get_element_presence_located_by_id(icon_magnify)
        placeholder_search = get_element_presence_located_by_id(text_searching)
        exp_placeholder="Cari di Tokopedia"
        assert_text(placeholder_search,exp_placeholder)

    def searching_product(self):
        sleep(5)
        product_searching = get_element_presence_located_by_id(element_search)
        product_searching.click()
        search_field = get_element_presence_located_by_id(searching_input)
        search_field.send_keys("topi")

    

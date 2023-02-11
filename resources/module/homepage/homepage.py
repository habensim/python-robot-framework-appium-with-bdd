import logging
import sys 
import os
current_directory = os.getcwd()
sys.path.append(current_directory)

from resources.module.homepage.Selector import *
from resources.helper.Element import *
from utils.Settings import driver

class Homepage:
    def carousel_usp_swipe(self):
        driver.implicitly_wait(5)
        swipe_element_by_id(driver,usp_carousel,"left")
        selanjutnyabtn = get_element_presence_located_by_id(selanjutnya)
        selanjutnyabtn.click()
        lewatibtn = get_element_presence_located_by_id(skiponboarding)
        lewatibtn.click()

    def verify_header_element(self):
        sleep(5)
        get_element_presence_located_by_id(icon_magnify)
        placeholder_search = get_element_presence_located_by_id(text_searching)
        exp_placeholder="Cari di Tokopedia"
        assert_text(placeholder_search,exp_placeholder)
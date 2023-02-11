import logging
import sys 
import os
current_directory = os.getcwd()
sys.path.append(current_directory)

from resources.module.homepage.Selector import *
from resources.helper.Element import *
from utils.Settings import driver
from appium.webdriver.common.mobileby import MobileBy

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

    def get_search_result(driver, search_term):
        # Locate the search field element
        search_field = driver.find_element_by_id(searching_input)

        # Enter the search term into the search field
        search_field.send_keys(search_term)

        # Wait for the search results to be displayed
        # (use an appropriate method for your specific test environment)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, result_searching_ct)))

        # Locate the first result in the search results
        first_result = driver.find_element_by_id(result_searching)

        # Get the text of the first result
        result = first_result.text

        # Print and log the result
        print(f"The result of the search for '{search_term}' is '{result}'")
        logging.info(f"The result of the search for '{search_term}' is '{result}'")

        return result

    def searching_product(self):
        product_searching = get_element_presence_located_by_id(element_search)
        product_searching.click()
        driver.implicitly_wait(10)
        search_term = "topi"
        result = get_search_result(driver, search_term)
        if result == "Expected Result":
            print("The search was successful")
        else:
            print("The search was unsuccessful")

    

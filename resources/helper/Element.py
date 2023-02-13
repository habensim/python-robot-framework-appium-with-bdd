import sys 
import os
import re
import logging
from time import sleep
import time
current_directory = os.getcwd()
sys.path.append(current_directory)

from appium import webdriver
from utils.Settings import driver, desired_caps
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions import interaction 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction
from resources.helper.Element import *
from resources.module.homepage.Selector import *
from robot.api import logger

# Get element by ID
def get_scrollable_element_by_id(element_id):
    try:
        element = driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("{element_id}").instance(0));'
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after scrolling to the entire page")

def get_element_clickable_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_element_presence_located_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((MobileBy.ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_element_visibility_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_element_invisible_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((MobileBy.ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds with this method")

def get_elements_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            driver.find_elements_by_id(element_id)
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_element_clickable_by_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_webview_element_by_id(id):
    element = driver.find_element_by_xpath(f"//*[@data-automation='{id}']")
    return element

# Get element by accessibility ID
def get_element_clickable_by_accessibility_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

def get_element_presence_by_accessibility_id(element_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 10 seconds")

# Get element by Xpath
def get_element_by_xpath(xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((MobileBy, xpath))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with xpath : {xpath} couldn't be found after waiting 10 seconds")

def get_elements_by_xpath(xpath):
    try:
        element = WebDriverWait(driver, 10).until(driver.find_element_by_xpath(xpath))
        return element
    except TimeoutException:
        raise Exception(f"element with xpath : {xpath} couldn't be found after waiting 10 seconds")

# Get element by Text
def get_scrollable_element_by_text(text):
    try:
        element = driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{text}").instance(0))'
        )
        return element
    except:
        raise Exception(f"element with text : {text} couldn't be found after scrolling to the entire page")

def get_element_by_match_text(text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((MobileBy.XPATH, f'//*[contains(@text, "{text}")]'))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with text : {text} couldn't be found after waiting 10 seconds")

def get_invisibility_element_by_text(text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((MobileBy.XPATH, f'//*[contains(@text, "{text}")]'))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with text : {text} couldn't be found after waiting 10 seconds")

def get_element_by_name(text):
    try:
        element = WebDriverWait(driver, 10).until(
            driver.find_element_by_name(text)
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{text}* couldn't be found after waiting 10 seconds")

# Get element by resource ID
def get_element_by_resource_id(self):
    try:
        element = WebDriverWait(driver, 10).until(
            driver.find_element_by_id(("id", "resource-id"))
        )
        return element
    except TimeoutException:
        raise Exception(f"element with xpath couldn't be found after waiting 10 seconds")

def get_element_by_resource_id_and_index(id, index):
    try:
        element = driver.find_element_by_android_uiautomator(f"new UiScrollable(new UiSelector().scrollable(true).resourceId('{id}').index('{index}')")
        return element
    except TimeoutException:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling the entire page")  

def get_element_by_resource_id_and_text(id, text):
    try:
        element = driver.find_element_by_android_uiautomator(f"new UiScrollable(new UiSelector().resourceId('{id}').getChildByText(new UiSelector().text('{text}'))")
        return element
    except TimeoutException:
        raise Exception(f"element with id *{id}* and *{text}* couldn't be found after scrolling the entire page")

# Get scrollable element
def get_scrollable_element_by_pointer(number_of_scroll_needed, from_x, from_y, to_x, to_y):
    for number_of_scroll in range (number_of_scroll_needed):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(from_x, from_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(to_x, to_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        sleep(1)  

# Get element by class name
def get_element_by_class_name(class_name):
    try:
        element = WebDriverWait(driver, 10).until(
            driver.find_element_by_class_name(class_name)
        )
        return element
    except TimeoutException:
        raise Exception(f"element with id *{class_name}* couldn't be found after waiting 10 seconds")

# Get element by Tap
def get_element_by_tap(id_closest_element, x, y):
    try:
        x_point = id_closest_element.location['x'] + x      # x is the difference at point x from the id_closest_element to the element to be selected
        y_point = id_closest_element.location['y'] + y      # y is the difference at point y from the id_closest_element to the element to be selected
        driver.tap([(x_point, y_point)])
    except TimeoutException:
        raise Exception(f"element with id *{id_closest_element}* couldn't be found after scrolling the entire page")

# Get element by recycler view
def get_element_by_recycler_view(xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            driver.find_element_by_xpath((MobileBy.XPATH, xpath)))
        return element
    except TimeoutException:
        raise Exception(f"element with id *{xpath}* couldn't be found after waiting 10 seconds")

def assert_text(element, expected_text):
    actual_text = element.text
    assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"

def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.5
    while True:
        current_size = len(driver.find_elements_by_xpath("//*"))
        driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=100, duration=800)
        time.sleep(SCROLL_PAUSE_TIME)
        new_size = len(driver.find_elements_by_xpath("//*"))
        if new_size == current_size:
            break

def scroll_to_bottom_touch(driver):
    """Scroll to the bottom of the screen."""
    # get the screen size
    screen_size = driver.get_window_size()

    # calculate the start and end points for the swipe gesture
    start_x = screen_size['width'] / 2
    start_y = screen_size['height'] * 0.9
    end_x = screen_size['width'] / 2
    end_y = screen_size['height'] * 0.1

    # create a TouchAction instance
    touch_action = TouchAction(driver)

    # perform the swipe gesture
    touch_action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()

def capture_element_screenshot(driver, folder_name, element_id):
    element = driver.find_element_by_id(element_id)
    if element.is_displayed():
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = "{}/{}.png".format(folder_name, element_id)
        element.screenshot(file_path)
        print("Element screenshot captured and saved to: {}".format(file_path))
    else:
        print("Element is NOT displayed")

def is_element_displayed(driver, locator, locator_value):
    try:
        element = driver.find_element(locator, locator_value)
        return element.is_displayed()
    except:
        return False

def tap_element_by_coordinates(driver, x, y):
    driver.tap([(x, y)])

def is_valid_phone_number(number):
    pattern = re.compile(r'^\d{10}$')
    match = pattern.search(number)
    return True if match else False

def verify_element_state(element,expected_state):
    if expected_state == "enabled":
        assert element.get_attribute("enabled") == 'true'
    else:
        assert element.get_attribute("enabled") == 'false'

def swipe_element_by_id(driver, element_id, direction):
    
    element = driver.find_element(MobileBy.ID,element_id)
    location = element.location
    size = element.size
    x1 = location['x'] + size['width'] * 0.5
    y1 = location['y'] + size['height'] * 0.5
    x2 = x1
    y2 = y1

    if direction == 'left':
        x2 = x1 - size['width']
    elif direction == 'right':
        x2 = x1 + size['width']
    elif direction == 'up':
        y2 = y1 - size['height']
    elif direction == 'down':
        y2 = y1 + size['height']

    driver.swipe(x1, y1, x2, y2, duration=1000)


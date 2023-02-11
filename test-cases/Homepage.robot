*** Settings ***
Documentation     Test Case For Testing Android APP
...               Based on test case at the google sheet below

Resource          ../keywords/Libraries.robot

*** Test Cases ***
Scenario 1 - Open Application To Emulator
    Given Reopen Application
    Then Welcome Carousel Swipe
    And Verify Element Header

*** Settings ***
Documentation     Test Case For Testing Android APP
...               Based on test case at the google sheet below

Resource          ../keywords/Libraries.robot

*** Test Cases ***
Scenario 1 - Verify Header And Searching Product Topi
    Given Reopen Application
    Then Welcome Carousel Swipe
    And Verify Element Header
    And Searching Product Tokped
    

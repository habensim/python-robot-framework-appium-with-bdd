*** Settings ***
Documentation       Resources for all libraries and variables.


Library        ../resources/module/homepage/Homepage.py
Library        ../resources/module/android/Application.py

Variables      ../resources/module/homepage/Selector.py

Resource       ../keywords/Launch.robot
Resource       ../keywords/Homepage.robot
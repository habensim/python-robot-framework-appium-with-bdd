from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "appPackage": "com.tokopedia.tkpd",
    "appActivity": "com.tokopedia.tkpd.ConsumerSplashScreen",
    "deviceName": "emulator-5554",
    "gpsEnabled": "true",
    "appium:newCommandTimeout": "180",
    "automationName": "UiAutomator2",
    "android:keepScreenOn": "true",
    "autoGrantPermissions":"true",
    "autoAcceptAlerts":"true",
    "fullReset":"false",
    "noReset":"true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)








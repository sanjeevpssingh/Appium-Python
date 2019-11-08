#driver declaration and App capabilities


from appium import webdriver
driver = None
def Capabilities():
    capabilities={
    'deviceName': 'Android Emulator',
    'platformName': 'Android',
    'platformVersion': '8.0',
    'appActivity': 'com.example.android.apis.ApiDemos',
    'appPackage': 'com.example.android.apis',
    'path':'App_apk/API.apk'}

    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub',capabilities)
    driver.implicitly_wait(2)





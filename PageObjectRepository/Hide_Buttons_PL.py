from Base_Class import Launch_Class
from Json_Module import json_call as lib
from Base_Class import CommonUtils

#get annimation
def getAnimation():
    try:
      return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Animation"))
    except Exception:
        print("Element not found")
        return None

#get HideShowButton
def getButton_Hide_Show():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Hide&Show"))
    except Exception:
        print("Element not found")
        return None

#get HideGone
def getButton_Hide_Gone():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Hide_GONE"))
    except Exception:
        print("Element not found")
        return  None

#get Button0
def getButton0():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "0"))
    except Exception:
        print("Element not found")
        return None

#get Button1
def getButton1():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "1"))
    except Exception:
     print("Element not found")
     return None

#get Button2
def getButton2():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "2"))
    except Exception:
        print("Element not found")
        return None

#get Button3
def getButton3():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "3"))
    except Exception:
        print("Element not found")
        return None

#verifying Hiding of buttons
def Verify_hide():
    try:
        Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "0"))
        return 'True'
    except Exception:
        return 'False'









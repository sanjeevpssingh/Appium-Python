from Base_Class import Launch_Class
from Json_Module import json_call as lib

#get App
def getApp():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Application"))
    except Exception:
        print("Element not found")
        return None

#get ActionBar
def getActionBar():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Action_Bar"))
    except Exception:
        print("Element not found")
        return None

#get DisplayOptions
def getDisplayOptions():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Display_Option"))
    except Exception:
        print("Element not found")
        return None

#get Display_Show_Title
def getDisplayShowTitle():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Show_Title"))
    except Exception:
     return None


#get DisplayShowTitle
def getDisplayShowTitleAgain():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "Show_Title"))
    except Exception:
     return None


#verifying ShowTitle
def Verify_ShowTitle():
    try:
        if(Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators","Title"))).is_displayed():
            return 'True'
        else:
            return 'False'

    except Exception:
        print(Exception)
        return 'False'





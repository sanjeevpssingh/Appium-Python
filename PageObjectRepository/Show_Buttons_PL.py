from Base_Class import Launch_Class
from Json_Module import json_call as lib

#get ShowButton
def getButtonShowButton():
    try:
     return Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "ShowButton"))
    except Exception:
        print("Element not found")
        return None

#verifying ShowButton
def Verify_ShowButton():
    try:
        Launch_Class.driver.find_element_by_xpath(lib.DataJSON("Locators", "0"))
        return 'True'
    except Exception:
        return 'False'


from PageObjectRepository import Show_Buttons_PL
from Base_Class import CommonUtils


def click_ShowButton():
    try:
     CommonUtils.press(Show_Buttons_PL.getButtonShowButton())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


from PageObjectRepository import Display_Options_PL
from Base_Class import CommonUtils


def click_getApp():
    try:
     CommonUtils.press(Display_Options_PL.getApp())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_getActionBar():
    try:
     CommonUtils.press(Display_Options_PL.getActionBar())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_DisplayOptions():
    try:
     CommonUtils.press(Display_Options_PL.getDisplayOptions())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_ShowTitle():
    try:
     CommonUtils.press(Display_Options_PL.getDisplayShowTitle())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)

def click_ShowTitleAgain():
    try:
     CommonUtils.press(Display_Options_PL.getDisplayShowTitleAgain())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


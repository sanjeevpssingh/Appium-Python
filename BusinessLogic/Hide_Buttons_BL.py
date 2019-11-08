from PageObjectRepository import Hide_Buttons_PL
from Base_Class import CommonUtils


def clickAnimation():
    try:
     CommonUtils.press(Hide_Buttons_PL.getAnimation())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def  click_HideShow():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton_Hide_Show())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_HideGone():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton_Hide_Gone())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_Button0():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton0())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_Button1():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton1())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_Button2():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton2())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)


def click_Button3():
    try:
     CommonUtils.press(Hide_Buttons_PL.getButton3())
     CommonUtils.waitFunction()
    except Exception:
        print("Element not Clicked")
        print(Exception)






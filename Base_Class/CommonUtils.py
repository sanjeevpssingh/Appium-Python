import click
import time


def press(go):
    if go is not None:
        go.click()
        return True

    else:
        print("Something went wrong")
        return False


def waitFunction():
    time.sleep(2)

def isDisplayed(element):
    try:
        if(element!=None):
            if(element.isDisplayed()):
                return True
            else:
                return False
        else:
            return False
    except:
        return False












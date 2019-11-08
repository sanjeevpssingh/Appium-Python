from Base_Class.Launch_Class import driver
from BusinessLogic import Display_Options_BL
from BusinessLogic import Show_Buttons_BL
from BusinessLogic import Hide_Buttons_BL
from PageObjectRepository import Hide_Buttons_PL
from PageObjectRepository import Show_Buttons_PL
from PageObjectRepository import Display_Options_PL
from Base_Class import Launch_Class
import pytest

'''For executing these TextCases along with report generation, please follow this command
pytest -v -s --html=Report.html --self-contained-html Test_Data/test_Call_Module.py
'''

#Test Case for App Launching
@pytest.mark.order1
def test_Launch():
    Launch_Class.Capabilities()

#Test Case for Hiding Buttons and verifying it
@pytest.mark.order2
def test_HideButton():
    Hide_Buttons_BL.clickAnimation()
    Hide_Buttons_BL.click_HideShow()
    Hide_Buttons_BL.click_HideGone()
    Hide_Buttons_BL.click_Button0()
    Hide_Buttons_BL.click_Button1()
    Hide_Buttons_BL.click_Button2()
    Hide_Buttons_BL.click_Button3()
    assert Hide_Buttons_PL.Verify_hide() == 'False'

#Test Case for Show Button and its verification
@pytest.mark.order3
def test_ShowButton():
    Show_Buttons_BL.click_ShowButton()
    Launch_Class.driver.back()
    Launch_Class.driver.back()
    assert Show_Buttons_PL.Verify_ShowButton() == 'False'


#Test Case for Display Options
@pytest.mark.order4
def test_DisplayTitle():
    Display_Options_BL.click_getApp()
    Display_Options_BL.click_getActionBar()
    Display_Options_BL.click_DisplayOptions()
    Display_Options_BL.click_ShowTitle()
    Display_Options_BL.click_ShowTitleAgain()
    assert Display_Options_PL.Verify_ShowTitle() == 'True'


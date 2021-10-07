import uiautomator2 as u2
from appium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.command_method import CommandMethod
import time
from appium import common
from appium.webdriver.extensions.search_context import android, mobile
from appium.webdriver.webdriver import _W3C_CAPABILITY_NAMES
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webelement import By
from appium.webdriver import webelement
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import pytest


desired_caps={
 "appium:udid": "emulator-5554",
  "platformName": "Android",
  "appium:noReset": True,
  "appium:automationName": "UiAutomator2"

}



driver=webdriver.Remote('127.0.0.1:4723/wd/hub',desired_caps)
element=webelement

Number="4849890253"
FirstN="Anton"
LastN="Nemchynov"
Email="anto2h101@gmail.com"
CityInput="Air"
StreetNumber=123
Social=5555


# MUVRTitle=driver.find_element_by_xpath('//android.widget.RelativeLayout[@content-desc="MUVR"]/android.widget.FrameLayout[2]/android.widget.TextView')
# text=MUVRTitle.text
# assert "MUVR" in text
App=driver.find_element_by_accessibility_id(accessibility_id="MUVR").click()
time.sleep(2)
AddlistTitle=driver.find_element_by_accessibility_id(accessibility_id="Add listing")
ProfileTab=driver.find_element_by_accessibility_id(accessibility_id="Profile").click()
time.sleep(2)
MOVRTitle=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
text=MOVRTitle.text
assert "Welcome to MUVR" in text
time.sleep(1)
CheckBox=driver.find_element_by_class_name("android.widget.CheckBox").is_selected()
time.sleep(1)
CheckBox=driver.find_element_by_class_name("android.widget.CheckBox").click()
time.sleep(2)
NumberLine=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt")
NumberLine.click()
NumberLine.send_keys(Number) 
NextButton=driver.find_element_by_id("com.muvr.android:id/welcomeSubmitBtn").click()
print("Number Pass")
time.sleep(1)
Auto=TouchAction(driver).tap(x=448, y=1278).perform()
time.sleep(1)
SMSCode=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
text=SMSCode.text
assert "Enter SMS code" in text
print(text)
smsCode = driver.switch_to.active_element.send_keys("1")
smsCode = driver.switch_to.active_element.send_keys("2")
smsCode = driver.switch_to.active_element.send_keys("3")
smsCode = driver.switch_to.active_element.send_keys("4")
smsCode = driver.switch_to.active_element.send_keys("5")
smsCode = driver.switch_to.active_element.send_keys("6")
time.sleep(1)
NextButton=driver.find_element_by_id("com.muvr.android:id/verifySmsCodeSubmitBtn").click()
print("SMS Pass")
time.sleep(1)
PersonalInfo=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
text=PersonalInfo.text
assert "Add your personal info" in text
PersonalInfo=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[2]")
text=PersonalInfo.text
assert "Should be the same as in the driver’s license" in text
PlaceholderTest=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=PlaceholderTest.text
assert "First name" in text
PlaceholderTest=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=PlaceholderTest.text
assert "Last name" in text
PlaceholderTest=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=PlaceholderTest.text
assert "Date of birth" in text
Back1=driver.find_element_by_accessibility_id(accessibility_id="Navigate up").click()
time.sleep(1)
print("Back1 Pass")
PlaceholderTest=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=PlaceholderTest.text
assert "Email" in text
PlaceholderTest=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=PlaceholderTest.text
assert "About me" in text
FirstName=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
FirstName.click()
FirstName.send_keys(FirstN)
LastName=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
LastName.click()
LastName.send_keys(LastN)
Date=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").click()
time.sleep(2)
TouchAction(driver).tap(x=533, y=1374).perform()
# Date1=driver.find_element_by_accessibility_id(accessibility_id="пн, 10 окт. 2005 г.").click()
DateConfirm=driver.find_element_by_id("com.muvr.android:id/confirm_button").click()
EmailForm=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
EmailForm.click()
EmailForm.send_keys(Email)
NextButton=driver.find_element_by_id("com.muvr.android:id/registrationPersonalInfoSubmitBtn").click()
print("RegForm Pass")
time.sleep(2)
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
text=LocationPlaceholder.text
assert "Add your location info" in text
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=LocationPlaceholder.text
assert "City" in text
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=LocationPlaceholder.text
assert "Postal Code" in text
City=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").click()
driver.implicitly_wait(2)
Back2=driver.find_element_by_accessibility_id(accessibility_id="Navigate up").click()
time.sleep(2)
print("Back2 Pass")
City1=driver.find_element_by_id("com.muvr.android:id/cityInputEt").click()
City2=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.EditText").send_keys(CityInput)
CityChose=driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[2]")[0].click()
NextButton=driver.find_elements_by_id("com.muvr.android:id/registrationLocationSubmitBtn")[0].click()
print("City Pass")
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=LocationPlaceholder.text
assert "Street number" in text
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=LocationPlaceholder.text
assert "Street name" in text
LocationPlaceholder=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=LocationPlaceholder.text
assert "Apartment, floor, suite, bldg#" in text
Address=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(StreetNumber)
Address1=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(StreetNumber)
Address2=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(StreetNumber)
NextButton=driver.find_element_by_id("com.muvr.android:id/registrationAddressSubmitBtn").click()
Back3=driver.find_element_by_accessibility_id(accessibility_id="Navigate up").click()
time.sleep(2)
print("Back3 Pass")
SSNTitle=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
text=SSNTitle.text
assert "Last 4 of social" in text
SSNPlaceholder=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt")
text=SSNPlaceholder.text
assert "SSN" in text
SSN=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").send_keys(Social)
NextButton=driver.find_element_by_id("com.muvr.android:id/registrationSocialSubmitBtn").click()
print("Address Pass")
time.sleep(2)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/registrationAvatarAddContainer").click()
time.sleep(2)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
time.sleep(1)
if driver.find_elements_by_id("com.android.permissioncontroller:id/permission_allow_button"):
  driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
  time.sleep(1)
  driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
if driver.find_elements_by_id("com.android.camera:id/shutter_button"):
  driver.find_element_by_id("com.android.camera:id/shutter_button").click()
driver.press_keycode (27)
driver.implicitly_wait(5)
driver.press_keycode (27)
time.sleep(5)
if driver.find_elements_by_id("com.android.camera:id/done_button"):
 driver.find_element_by_id("com.android.camera:id/done_button").click()
driver.press_keycode (108) 
time.sleep(1)
NextButton=driver.find_element_by_id("com.muvr.android:id/registrationAvatarSubmitBtn").click()
print("Registration Pass")
driver.quit()
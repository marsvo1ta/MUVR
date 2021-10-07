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
import pytest




desired_caps={
 "appium:udid": "4e94ff54",
  "platformName": "Android",
  "appium:noReset": True,
  "appium:automationName": "UiAutomator2"

}
driver=webdriver.Remote('127.0.0.1:4723/wd/hub',desired_caps)
element=webelement


Location="Air"
TitleLine="Box"
DescriptionLine="Big Black Box"
PriceLine="100"
MeaLine=2


AddListing=driver.find_element_by_accessibility_id(accessibility_id="Add listing").click()
time.sleep(2)
if driver.find_elements_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button"):
  driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
time.sleep(2)
SetPickLock=driver.find_element_by_id("com.muvr.android:id/mapTitleTv")
text=SetPickLock.text
assert "Set pickup location" in text
SetPickup=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").click()
time.sleep(2)
SetPickup=driver.find_element_by_id("com.muvr.android:id/autocompleteInputEt").send_keys(Location)
time.sleep(1)
SetPickup=driver.find_element_by_id("com.muvr.android:id/itemAutocompleteAddressTv").click()
time.sleep(1)
SetPickup=driver.find_element_by_id("com.muvr.android:id/mapConfirmBtn").click()
time.sleep(1)
SetDropLock=driver.find_element_by_id("com.muvr.android:id/mapTitleTv")
text=SetDropLock.text
assert "Set drop off location" in text
SetDropoff=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").click()
time.sleep(1)
SetDropoff=driver.find_element_by_id("com.muvr.android:id/autocompleteInputEt").send_keys(Location)
time.sleep(1)
SetDropoff=driver.find_element_by_id("com.muvr.android:id/itemAutocompleteAddressTv").click()
time.sleep(1)
SetDropoff=driver.find_element_by_id("com.muvr.android:id/mapConfirmBtn").click()
time.sleep(1)
print("Location Pass")
SendTitle=driver.find_element_by_id("com.muvr.android:id/itemInfoTitleTv")
text=SendTitle.text
assert "What would you like to send?" in text
SendForm=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=SendForm.text
assert "Title" in text
SendForm=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=SendForm.text
assert "Description" in text
SendForm=driver.find_element_by_id("com.muvr.android:id/itemInfoParcelTypeLabel")
text=SendForm.text
assert "Select the parcel type" in text
SendForm=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView")
text=SendForm.text
assert "Large bulky" in text
SendForm=driver.find_element_by_id("com.muvr.android:id/itemInfoMeasurementsTv")
text=SendForm.text
assert "Add measurement options" in text
SendForm=driver.find_element_by_id("com.muvr.android:id/itemInfoSuggestedPriceValueTv")
text=SendForm.text
assert "10$" in text
Title=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(TitleLine)
Description=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(DescriptionLine)
Price=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(PriceLine)
Parcel=driver.find_element_by_id("com.muvr.android:id/parcelTypeLabelTv").click()
Parcel=driver.find_element_by_id("com.muvr.android:id/parcelTypeIconIv").click()
Measure=driver.find_element_by_id("com.muvr.android:id/itemInfoMeasurementsTv").click()
driver.hide_keyboard()
TouchAction(driver)   .press(x=574, y=1955)   .move_to(x=591, y=530)   .release()   .perform()
Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
NextButton=driver.find_element_by_id("com.muvr.android:id/itemInfoSubmitBtn").click()
print("List Pass")
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/itemPhotoPhotoContainer").click()
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
time.sleep(2)
if driver.find_elements_by_id("com.android.camera:id/shutter_button"):
  time.sleep(2)
  driver.find_element_by_id("com.android.camera:id/shutter_button").click()
time.sleep(2)
if driver.find_elements_by_id("com.android.camera:id/done_button"):
 time.sleep(2)
 driver.find_element_by_id("com.android.camera:id/done_button").click()
driver.press_keycode (27)
driver.implicitly_wait(5)
driver.press_keycode (27).implicitly_wait(10)
time.sleep(3)
driver.press_keycode (108) 
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/itemPhotoPhotoContainer").click()
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
time.sleep(2)
if driver.find_elements_by_id("com.android.camera:id/shutter_button"):
  driver.find_element_by_id("com.android.camera:id/shutter_button").click()
if driver.find_elements_by_id("com.android.camera:id/done_button"):
 driver.find_element_by_id("com.android.camera:id/done_button").click()
driver.press_keycode (27)
driver.implicitly_wait(5)
driver.press_keycode (27).implicitly_wait(10)
time.sleep(3)
driver.press_keycode (108) 
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/itemPhotoPhotoContainer").click()
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
time.sleep(1)
if driver.find_elements_by_id("com.android.camera:id/shutter_button"):
  time.sleep(1)
  driver.find_element_by_id("com.android.camera:id/shutter_button").click()
  time.sleep(1)
if driver.find_elements_by_id("com.android.camera:id/done_button"):
  time.sleep(1)
  driver.find_element_by_id("com.android.camera:id/done_button").click()
  time.sleep(1)
driver.press_keycode (27)
time.sleep(1)
driver.press_keycode (27).implicitly_wait(10)
time.sleep(1)
driver.press_keycode (108) 
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/itemPhotoPhotoContainer").click()
time.sleep(1)
AddPhoto=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
if driver.find_elements_by_id("com.android.camera:id/shutter_button"):
  time.sleep(1)
  driver.find_element_by_id("com.android.camera:id/shutter_button").click()
  time.sleep(1)
if driver.find_elements_by_id("com.android.camera:id/done_button"):
  time.sleep(1)
  driver.find_element_by_id("com.android.camera:id/done_button").click()
  time.sleep(1)
driver.press_keycode (27)
time.sleep(1)
driver.press_keycode (27).implicitly_wait(10)
time.sleep(3)
driver.press_keycode (108) 
time.sleep(1)
PhotoCheck=driver.find_element_by_id("com.muvr.android:id/itemPhotoDescTv")
text=PhotoCheck.text
assert "Don't forget to safely package your parcel before shipping!" in text
NextButton=driver.find_element_by_id("com.muvr.android:id/itemPhotoSubmitBtn").click()
Miles=driver.find_element_by_id("com.muvr.android:id/dropOffDateUrgentDescTv")
text=Miles.text
assert "This icon means that the parcel is within a radius of 300 miles and must be delivered today" in text
Date=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").click()
if driver.find_elements_by_accessibility_id(accessibility_id="нд, 10 жовт."):
  driver.find_element_by_accessibility_id(accessibility_id="нд, 10 жовт.").click()
else:Date=driver.find_element_by_accessibility_id(accessibility_id="сб, 16 окт.").click()
time.sleep(1)
Date=driver.find_element_by_id("com.muvr.android:id/confirm_button").click()
time.sleep(1)
NextButton=driver.find_element_by_id("com.muvr.android:id/dropOffDateSubmitBtn").click()
time.sleep(1)
RecipientPlace=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=RecipientPlace.text
assert "Name" in text
RecipientPlace=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
text=RecipientPlace.text
assert "Phone number" in text
NotRecipient=driver.find_element_by_id("com.muvr.android:id/recipientInfoIAmNotRb").click()
RecInfoName=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").send_keys("John")
RecInfoNumber=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys("484484848212")
PostButton=driver.find_element_by_id("com.muvr.android:id/recipientInfoSubmitBtn").click()
time.sleep(2)
if driver.find_elements_by_accessibility_id(accessibility_id="Перейти вгору"):
  driver.find_element_by_accessibility_id(accessibility_id="Перейти вгору").click()
else:EndClose=driver.find_element_by_accessibility_id(accessibility_id="Перейти вверх").click()
print("Listing Pass")
driver.quit()
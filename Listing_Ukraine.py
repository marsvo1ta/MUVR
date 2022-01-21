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
import random
from random_word import RandomWords
from random_swipe import RandomSwipe


desired_caps={
 "appium:udid": "adb-4e94ff54-idBPVQ._adb-tls-connect._tcp.",
  "platformName": "Android",
  "appActivity": "com.muvr.android.features.splash.SplashActivity",
  "appium:appPackage": "com.muvr.android",
  "appium:noReset": True,
  "appium:automationName": "UiAutomator2"

}

driver = webdriver.Remote('127.0.0.1:4723/wd/hub',desired_caps)
element=webelement
r = RandomWords()



Location="Air"
TitleLine=r.get_random_word(minLength=10)
DescriptionLine=r.get_random_word(minLength=10)
random_price=random.randrange(-53,50)
PriceLine=random.randrange(11,1100)
MeaLine=random.randrange(1,999)

driver.implicitly_wait(3)

for i in range(2):
    AddListing=driver.find_element_by_accessibility_id(accessibility_id="Add listing").click()
    
    if driver.find_elements_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button"):
      driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
    
    SetPickLock=driver.find_element_by_id("com.muvr.android:id/mapTitleTv")
    text=SetPickLock.text
    assert "Set pickup location" in text
    randomSwipe = random.randrange(1,7)
    if randomSwipe == 1:
      driver.swipe(963, 471, 196, 1585)
    elif randomSwipe == 2:
      driver.swipe(139, 347, 979, 1535)
    elif randomSwipe == 3:
      driver.swipe(562, 357, 591, 1661)
    elif randomSwipe == 4:
      driver.swipe(518, 1617, 546, 347)
    elif randomSwipe == 5:
      driver.swipe(92, 913, 865, 922)
    elif randomSwipe == 6:
      driver.swipe(1011, 1023, 79, 1017)
    SetPickup=driver.find_element_by_id("com.muvr.android:id/mapConfirmBtn").click()
    
    SetDropLock=driver.find_element_by_id("com.muvr.android:id/mapTitleTv")
    text=SetDropLock.text
    assert "Set drop off location" in text
    SetDropoff=driver.find_element_by_id("com.muvr.android:id/mapConfirmBtn").click()
    
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

    assert "Large/Bulky" in text
    SendForm=driver.find_element_by_id("com.muvr.android:id/itemInfoMeasurementsTv")
    text=SendForm.text
    assert "Add measurement options" in text
    SendForm=driver.find_element_by_id("com.muvr.android:id/itemInfoSuggestedPriceValueTv")
    text=SendForm.text
    assert "$10" in text
    Title=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(TitleLine)
    Description=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(DescriptionLine)
    Price=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(PriceLine)
    Parcel=driver.find_element_by_id("com.muvr.android:id/parcelTypeLabelTv").click()
    Parcel=driver.find_element_by_id("com.muvr.android:id/parcelTypeIconIv").click()
    Measure=driver.find_element_by_id("com.muvr.android:id/itemInfoMeasurementsTv").click()
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)
    TouchAction(driver)   .press(x=523, y=1671)   .move_to(x=571, y=519)   .release()   .perform()
    Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
    Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
    Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
    Measure=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(MeaLine)
    NextButton=driver.find_element_by_id("com.muvr.android:id/itemInfoSubmitBtn").click()
    print("List Pass")
    time.sleep(1)
    for i in range(2): #Додаємо фото
      add_photo=driver.find_element_by_id("com.muvr.android:id/itemPhotoPhotoContainer").click()
      time.sleep(2)
      if driver.find_elements_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button"):
        driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        time.sleep(2)
      add_photo=driver.find_element_by_id("com.muvr.android:id/bottomSheetAddPhotoCameraBtn").click()
      time.sleep(2)
      keycode1=driver.press_keycode(27)
      time.sleep(3)
      if driver.find_elements_by_id("com.android.camera:id/done_button"):
        driver.find_element_by_id("com.android.camera:id/done_button").click()
      else:
        driver.press_keycode(108)
      time.sleep(2)
    photo_assertion=driver.find_element_by_id("com.muvr.android:id/itemPhotoDescTv")
    text=photo_assertion.text
    assert "Don't forget to safely package your parcel before shipping!" in text
    NextButton=driver.find_element_by_id("com.muvr.android:id/itemPhotoSubmitBtn").click()
    Miles=driver.find_element_by_id("com.muvr.android:id/dropOffDateUrgentDescTv")
    text=Miles.text
    assert "This icon means that the parcel is within a radius of 300 miles and must be delivered today" in text
    Date=driver.find_element_by_id("com.muvr.android:id/inputTextInpEt").click()
    date_picker=driver.find_element_by_id("com.muvr.android:id/mtrl_picker_header_toggle").click()
    date_picker=driver.switch_to.active_element.send_keys("20.12.21")
    date_picker=driver.find_element_by_id("com.muvr.android:id/confirm_button").click()
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
    TouchAction(driver).press(x=550, y=1770).move_to(x=557, y=728).release().perform()
    time.sleep(2)
    driver.find_element_by_id("com.muvr.android:id/orderDetailBackToMainPageBtn").click()
    time.sleep(2)
driver.quit()
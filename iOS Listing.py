from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.command_method import CommandMethod
import time
from appium import common
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.extensions.search_context import android, mobile
from appium.webdriver.webdriver import _W3C_CAPABILITY_NAMES
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webelement import By
from appium.webdriver import webelement
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import random
from random_word import RandomWords
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction



desired_caps={
 "platformName": "iOS",
  "appium:automationName": "XCUITEST",
  "appium:deviceName": "iPhone10,6",
  "appium:deviceVersion": "15.1",
  "appium:udid": "b03bb90b0da683170e2699ec0d43ee55b35a53fd",
  "appium:xcodeOrgId": "13C5066c",
  "appium:xcodeSigningId": "Iphone Developer"
}
driver=webdriver.Remote('127.0.0.1:4723/wd/hub',desired_caps)
element=webelement
r = RandomWords()
action = ActionChains(driver)
Wait = WebDriverWait(driver, 20)


recipientName = r.get_random_word()
recipientNumber = 4840000000 + random.randrange(1111111, 9999999)

Location="Air"
TitleLine=r.get_random_word(minLength=10)
DescriptionLine=r.get_random_word(minLength=10)
random_price=random.randrange(-53,50)
PriceLine=random.randrange(11,1100)
MeaLine=random.randrange(1,999)
eRand = random.randrange(1, 31)
Time = int(driver.get_device_time("DD"))

driver.find_element_by_ios_predicate('label == "Add listing"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Set pickup location"').is_displayed()
for i in range(2):
  driver.find_element_by_ios_predicate('value == "Confirm"').click() #Confirm
  time.sleep(1)
  driver.find_element_by_ios_predicate('value == "Set drop off location"').is_displayed()
  driver.find_element_by_ios_predicate('value == "Confirm"').click()
  time.sleep(1)
  driver.find_element_by_ios_predicate('value == "What would you like to send?"').is_displayed() #Add Info
  driver.find_element_by_ios_predicate('value == "Parcel type"').is_displayed()
  driver.find_element_by_ios_predicate('value == "Title"').click()
  driver.switch_to.active_element.send_keys(TitleLine)
  driver.find_element_by_ios_predicate('value == "Description"').click()
  driver.switch_to.active_element.send_keys(DescriptionLine)
  driver.find_element_by_ios_predicate('name == "packeges"').click()
  driver.find_element_by_ios_predicate('name == "large"').click()
  driver.find_element_by_ios_predicate('name == "documents"').click()
  driver.find_element_by_ios_predicate('value == "Add measurement options"').click()
  driver.find_element_by_accessibility_id("Done").click()
  driver.find_element_by_ios_predicate('value == "Height, inch"').click()
  driver.switch_to.active_element.send_keys(MeaLine)
  driver.find_element_by_ios_predicate('value == "Width, inch"').click()
  driver.switch_to.active_element.send_keys(MeaLine)
  driver.find_element_by_accessibility_id("Done").click()
  driver.find_element_by_ios_predicate('value == "Width, inch" AND type == "XCUIElementTypeTextField"').click()
  driver.switch_to.active_element.send_keys(MeaLine)
  driver.find_element_by_ios_predicate('value == "Weight, lbs"').click()
  driver.switch_to.active_element.send_keys(MeaLine)
  driver.find_element_by_accessibility_id("Done").click()
  driver.find_element_by_ios_predicate('value == "Suggested price"').is_displayed()
  driver.find_element_by_accessibility_id("infoIcon").click()
  driver.find_element_by_ios_predicate('value == "Suggested price info"').is_displayed()
  driver.find_element_by_ios_predicate('value == "You can use the suggested price, set your own price, or leave it blank. You have the option of negotiating directly with the driver."').is_displayed
  driver.find_element_by_ios_predicate('label == "OK"').click()
  driver.find_element_by_ios_predicate('value == "Price"').click()
  driver.switch_to.active_element.send_keys(PriceLine)
  driver.find_element_by_accessibility_id("Done").click()
  driver.find_element_by_ios_predicate('value == "Next"').click()
  time.sleep(2)
  driver.find_element_by_ios_predicate('label == "Add photo"').is_displayed #Add Photo
  driver.find_element_by_accessibility_id("Don't forget to safely package your parcel before shipping!").is_displayed
  driver.find_element_by_ios_predicate('label == "photoCamera"').click()
  time.sleep(1)
  driver.find_element_by_ios_predicate('value == "Camera"').click()
  time.sleep(1)
  driver.find_element_by_accessibility_id("PhotoCapture").click()
  time.sleep(4)
  driver.find_element_by_accessibility_id("Use Photo").click()
  time.sleep(1)
  driver.find_element_by_ios_predicate('name == "deleteIcon"').click()
  time.sleep(2)
  driver.find_element_by_ios_predicate('value == "Next"').click()
  time.sleep(4)
  driver.find_element_by_ios_predicate('label == "Drop off date"').is_displayed #Calendar
  driver.find_element_by_ios_predicate('label == "calendarIcon"').click()
  e = driver.find_elements_by_ios_predicate('type == "XCUIElementTypePickerWheel"')
  if eRand < Time:
    e[0].set_value(eRand + random.randrange(1,5))
  else:
    e[0].set_value(eRand)
  e[1].set_value("November")
  e[2].set_value(2021)
  driver.find_element_by_accessibility_id("Done").click()
  # if eRand == Time:
  #   driver.find_element_by_ios_predicate('label == "This icon means that the parcel is within a radius of 300 miles and must be delivered today"').is_displayed:
  #   print("Next day")
  driver.find_element_by_ios_predicate('value == "Next"').click()
  time.sleep(3)
  driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="MuvrApp"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage').click()
  time.sleep(1)
  driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="MuvrApp"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage').click()
  time.sleep(2)
  driver.find_element_by_ios_predicate('value == "Recipient info"').is_displayed
  driver.find_element_by_ios_predicate('value == "Name"').click()
  driver.switch_to.active_element.send_keys(recipientName)
  time.sleep(1)
  driver.find_element_by_ios_predicate("value == '1' AND type == 'XCUIElementTypeTextField'").send_keys(recipientNumber)
  time.sleep(1)
  # driver.find_element_by_accessibility_id("Done").click()
  time.sleep(1)
  Wait.until(EC.element_to_be_clickable((MobileBy.IOS_PREDICATE, "value == 'Post'"))).click()
  # driver.find_element_by_ios_predicate('value == "Post"').click()
  time.sleep(1)
  driver.find_element_by_accessibility_id("whiteXmarcIcon").click()
  time.sleep(1)
  a=driver.execute_script("mobile: swipe", {"direction": "up"})
  # TouchAction(driver)   .press(x=175, y=648)   .move_to(x=186, y=295)   .release()   .perform()
  addNext = driver.find_element_by_ios_predicate('value == "Add next listing"').click()
  time.sleep(2)

driver.quit()

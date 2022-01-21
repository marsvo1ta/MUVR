from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.command_method import CommandMethod
import time
from appium import common
from appium.webdriver.extensions.search_context import android, mobile
from appium.webdriver.webdriver import _W3C_CAPABILITY_NAMES
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webelement import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import webelement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
from random_word import RandomWords


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
action = ActionChains(driver)

r=RandomWords()

Number=4842000000 + random.randrange(100,499)
FirstN=r.get_random_word()
LastN=r.get_random_word()
Email=r.get_random_word(maxLength=10)+"@"+"gmail"+".com"
CityInput="Air"
StreetNumber=random.randrange(111,999)
Social=random.randrange(1111,9999)
Postal= random.randrange(11111, 99999)
Time = driver.get_device_time("DD")
Time = int(Time)

driver.find_element_by_xpath('//XCUIElementTypeIcon[@name="MuvrApp"]').click()
time.sleep(1)
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Profile").click()
if driver.find_elements_by_ios_predicate('value == "Logout"'):
    driver.find_element_by_ios_predicate('value == "Logout"').click()
    driver.find_element_by_accessibility_id("Logout").click()
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Profile").click()
createText = driver.find_element_by_ios_predicate('value == "Create your account"').is_displayed
smsText = driver.find_element_by_ios_predicate('value == "Add your mobile number for SMS verification"').is_displayed
phoneText = driver.find_element_by_ios_predicate('value == "Phone number"').is_displayed
clearText = driver.find_element_by_ios_predicate('label == "Clear text"').is_displayed
termsText = driver.find_element_by_ios_predicate('value == "I agree with the Terms & Conditions and Privacy Statement"').is_displayed
driver.find_element(MobileBy.ACCESSIBILITY_ID, "+").click()
driver.find_element_by_ios_predicate("value == '1' AND type == 'XCUIElementTypeTextField'").send_keys(Number)
TouchAction(driver).tap(x=196, y=344).perform()
driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='MuvrApp']/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage").click()
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.switch_to.active_element.send_keys(1)
driver.switch_to.active_element.send_keys(2)
driver.switch_to.active_element.send_keys(3)
driver.switch_to.active_element.send_keys(4)
driver.switch_to.active_element.send_keys(5)
driver.switch_to.active_element.send_keys(6)
driver.find_element_by_ios_predicate('value == "Enter SMS code"').is_displayed
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Add your personal info"').is_displayed
driver.find_element_by_ios_predicate('value == "Required for user of secure payment system"')
a1=driver.find_element_by_ios_predicate('value == "First name"').click()
driver.switch_to.active_element.send_keys(FirstN)
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Last name"').click()
driver.switch_to.active_element.send_keys(LastN)
driver.find_element_by_ios_predicate('value == "Date of birth"').click() #Ввід дати
e = driver.find_elements_by_ios_predicate('type == "XCUIElementTypePickerWheel"')
e[0].set_value(17)
e[1].set_value("October")
e[2].set_value(1989)
driver.find_element_by_accessibility_id("Done").click()
driver.find_element_by_ios_predicate('value == "Email"').click()
driver.switch_to.active_element.send_keys(Email)
driver.find_element_by_accessibility_id("Done").click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Brief bio about you"').is_displayed
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Add your location info"').is_displayed
driver.find_element_by_ios_predicate('value == "Required for user of secure payment system"').is_displayed
driver.find_element_by_ios_predicate('value == "City"').click()
driver.find_element_by_ios_predicate('label == "Where are you going?"').click()
driver.find_element_by_ios_predicate('value == "Search by City"').click()
driver.switch_to.active_element.send_keys(CityInput)
time.sleep(1)
driver.find_element_by_accessibility_id("Air Force Academy").click()
driver.find_element_by_ios_predicate('value == "Postal Code"').click()
driver.switch_to.active_element.send_keys(Postal)
time.sleep(1)
driver.find_element_by_accessibility_id("Done").click()
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Add your address info"').is_displayed
driver.find_element_by_ios_predicate('value == "Required for user of secure payment system"').is_displayed
driver.find_element_by_ios_predicate('value == "Street number"').click()
driver.switch_to.active_element.send_keys(StreetNumber)
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Street name"').click()
driver.switch_to.active_element.send_keys(StreetNumber)
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Apartment, floor, suite, bldg#"').click()
driver.switch_to.active_element.send_keys(StreetNumber)
driver.find_element_by_accessibility_id("Done").click()
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Last 4 of social"').is_displayed
driver.find_element_by_ios_predicate('value == "Required for user of secure payment system"').is_displayed
driver.find_element_by_ios_predicate('value == "SSN"').click()
driver.switch_to.active_element.send_keys(Social)
driver.find_element_by_accessibility_id("Done").click()
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Add your photo"').is_displayed
driver.find_element_by_ios_predicate('value == "Will appear in your listing so the customer can recognize you"').is_displayed
driver.find_element_by_accessibility_id("photoCamera").click()
time.sleep(2)
driver.find_element_by_ios_predicate('value == "Camera"').click()
time.sleep(2)
if driver.find_elements_by_ios_predicate('label == "Разрешить"'):
    driver.find_element_by_ios_predicate('label == "Разрешить"').click()
    time.sleep(1)
driver.find_element_by_accessibility_id("PhotoCapture").click()
time.sleep(2)
driver.find_element_by_accessibility_id("Use Photo").click()
time.sleep(1)
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(2)
driver.find_element_by_ios_predicate('value == "Take a photo of your Drivers License"').is_displayed
driver.find_element_by_ios_predicate('value == "Please make sure we can easily read the details"').is_displayed
driver.find_element_by_ios_predicate('value == "Front side"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Camera"').click()
time.sleep(1)
driver.find_element_by_accessibility_id("PhotoCapture").click()
time.sleep(2)
driver.find_element_by_accessibility_id("Use Photo").click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Back side"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Camera"').click()
time.sleep(1)
driver.find_element_by_accessibility_id("PhotoCapture").click()
time.sleep(2)
driver.find_element_by_accessibility_id("Use Photo").click()
time.sleep(2)
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(3)
driver.find_element_by_ios_predicate('value == "Choose parcel types what you can deliver"').is_displayed
driver.find_element_by_ios_predicate('value == "Documents"' and 'value == "Packages"' and 'value == "LargeBulky"').is_displayed
driver.find_element_by_ios_predicate('value == "Boxes weighing up to 20 lbs"' and 'value =="Large boxes/items over 20 Lbs"').is_displayed
driver.find_element_by_accessibility_id("Letters or documents").click()
time.sleep(1)
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Add photo"').click()
time.sleep(1)
driver.find_element_by_ios_predicate('value == "Camera"').click()
time.sleep(1)
driver.find_element_by_accessibility_id("PhotoCapture").click()
time.sleep(2)
driver.find_element_by_accessibility_id("Use Photo").click()
time.sleep(2)
driver.find_element_by_ios_predicate('label == "Next" AND name == "Next" AND value == "Next"').click()
time.sleep(2)
driver.find_element_by_ios_predicate('value == "Insurance"').click()
driver.switch_to.active_element.send_keys(Postal)
driver.find_element_by_ios_predicate('value == "Registration"').click()
driver.switch_to.active_element.send_keys(Postal)
driver.find_element_by_accessibility_id("Done").click()
driver.find_element_by_ios_predicate('value == "Finish"').click()
time.sleep(1)
driver.find_element_by_accessibility_id("whiteXmarcIcon").click()

driver.quit()
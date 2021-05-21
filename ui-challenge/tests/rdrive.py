from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import traceback
from selenium.webdriver.support.ui import Select
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class RemoteDrive():
    def __init__(self, surl, headless = False):
        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.burl = surl
        self.driver.get(self.burl)
        self.zzz = 2

    def handle_alert(self):
        alerto = self.driver.switch_to.alert()
        alerto.accept()

    def teardown(self):
        try:
            self.driver.quit()
            self.handle_alert()
            #self.driver.close()
            print('Closed session cleanly')
        except Exception as exception:
            print('Closed session')

    def holdout(self, x, y, ho = 8):
        ui.WebDriverWait(self.driver, ho).until(EC.presence_of_element_located((x, y)))
        ui.WebDriverWait(self.driver, ho).until(EC.visibility_of_element_located((x, y)))
        ui.WebDriverWait(self.driver, ho).until(EC.element_to_be_clickable((x, y)))

    def get_url(self):
        print('current url: ' + self.driver.current_url)
        return self.driver.current_url

    def click_by_css_selector(self, csss, to = 8):
        print('Clicking ' + csss)
        try:
            self.holdout(By.CSS_SELECTOR, csss, ho = to)
            self.driver.find_element_by_css_selector(csss).click()
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def click_by_xpath(self, xp, to = 8):
        print('Clicking ' + xp)
        try:
            self.holdout(By.XPATH, xp, ho = to)
            self.driver.find_element_by_xpath(xp).click()
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def sign_canvas(self):
        xp = "//canvas[@class=\'mp-sig-pad\']"
        self.driver.find_element_by_xpath(xp).click()
        self.click_by_class_and_text('button', 'mp-button', 'Confirm')
        time.sleep(1)

    def click_by_id(self, id, to = 8):
        print(str('Clicking ' + id))
        try:
            self.holdout(By.ID, id, ho = to)
            self.driver.find_element_by_id(id).click()
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def click_datepicker_day(self, ele, cls, to = 8):
        xp = "//" + ele + "[@class=\'" + cls + "\']"
        self.driver.find_element_by_xpath("//input[@class='mp-datepicker']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(xp).click()

    def edit_value(self, ele, cls, payload, to = 8):
        xp = "//" + ele + "[@class=\'" + cls + "\']"
        element = self.driver.find_element_by_xpath(xp)
        self.driver.execute_script("arguments[0].setAttribute('value',\'" + payload + "\')", element)

    def click_by_class_and_text(self, ele, cls, text, to = 8):
        xp = "//" + ele + "[@class=\'" + cls + "\' and text()=\'" + text +"\']"
        print(str('Clicking element@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            self.driver.find_element_by_xpath(xp).click()
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def type_by_id(self, id, payload, to = 8):
        print(str('Entering ' + payload + ' into ' + id))
        try:
            self.holdout(By.ID, id, ho = to)
            self.driver.find_element_by_id(id).send_keys(payload)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def select_by_id(self, id, payload, to = 8):
        print(str('Selecting ' + payload + ' from ' + id + ' dropdown'))
        try:
            self.holdout(By.ID, id, ho = to)
            select = Select(self.driver.find_element_by_id(id))
            select.select_by_visible_text(payload)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def wait_for_image_by_source(self, src, to = 8):
        xp = '//img[@src=\"' + src + '\"]'
        print(str('Waiting for image@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def click_image_by_source(self, src, to = 8):
        xp = '//img[@src=\"' + src + '\"]'
        print(str('Clicking image@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            self.driver.find_element_by_xpath(xp).click()
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def wait_for_link(self, href, text, to = 8):
        xp = "//a[@href=\'" + href + "\' and text()=\'" + text +"\']"
        print(str('Waiting for element@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def wait_for_text_no_class(self, ele, text, to = 8):
        xp = "//" + ele + "[text()=\'" + text +"\']"
        print(str('Waiting for element@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def wait_for_text(self, ele, cls, text, to = 8):
        xp = "//" + ele + "[@class=\'" + cls + "\' and text()=\'" + text +"\']"
        print(str('Waiting for element@xpath: ' + xp))
        try:
            self.holdout(By.XPATH, xp, ho = to)
            return True
        except Exception as exception:
            traceback.print_exc()
            self.teardown()
            return False

    def wait_for_iframe(self, ho = 8):
        ui.WebDriverWait(self.driver, ho).until(EC.frame_to_be_available_and_switch_to_it(1))
        time.sleep(ho / 2)

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator, field=""):
        try:
            #self.driver.find_element(locator).click()
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            print(field+" is Clicked")
        except TimeoutException as ex:
            pytest.fail(field+ " is Not clickable")


    def send_keys(self, locator, value="", field=""):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)
            print("Entered the Value in "+field)
        except:
            pytest.fail("No able to enter value in the "+field)


    def get_text(self, locator, field=""):
        try:
            element =self.wait.until(EC.visibility_of_element_located(locator))
            value = element.text
            print(value+" is got as a text")
            return value
        except:
            pytest.fail(field+" is not visible")
            return ""

    def find_all_elements(self, xpath, field=""):

        try:
            return self.driver.find_elements(By.XPATH, xpath)
        except Exception as ex:
            print("There is issue in getting all "+ field+str(ex))
            return []

    def wait_until_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            pytest.fail("The Element is not visible")
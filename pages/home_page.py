from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.XPATH, "//input[@name='search_query']")
    SEARCH_CONTENT = (By.XPATH, "//div[@id='scroll-container']//ancestor::div[@id='contents']//preceding-sibling::div[contains(@class,'grid-subheader')]//a/span[@id='title']")
    TAB_BUTTONS ="//iron-selector[@id='chips']//button"
    MENU_ITEMS = (By.XPATH, "//tp-yt-paper-item[@role='link']")
    def enter_search_string(self, search_string=""):
        self.send_keys(self.SEARCH_BOX, search_string, "Search box")
        self.click(locator=(By.XPATH,f"//div[@aria-label='{search_string}']"), field="Search_content")

    def get_search_content(self):
        value = self.get_text(locator=self.SEARCH_CONTENT, field="Search content")
        return value

    def get_home_tabs(self):
        self.wait_until_element_visible(locator=(By.XPATH, self.TAB_BUTTONS))
        value = self.find_all_elements(xpath=self.TAB_BUTTONS, field="Home Tabs")
        return value

    def get_home_menu_item(self):
        return  self.find_all_elements(locator=self.MENU_ITEMS, field="Menu Items")

    def click_menu(self, menu):
        self.click(locator=(By.XPATH, "//tp-yt-paper-item[@role='link']//yt-formatted-string[contains(text(),'"+menu+"')]"), field=menu)

    #read_xpath[user][name]
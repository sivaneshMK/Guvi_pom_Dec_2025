import time

from pages.home_page import HomePage
from utils import menu_utils


def test_search_content_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.enter_search_string("new movies")
    actual_result = home_page.get_search_content()
    assert actual_result == "YouTube Primetime movies", "YT is not displaying exact search content"

def test_home_page_tab(driver):
    home_page = HomePage(driver)
    home_page.click_menu("Shorts")
    time.sleep(5)
    home_page.click_menu("Home")
    time.sleep(5)
    tabs = menu_utils.get_all_the_tab_from_home(driver)
    assert (len(tabs) == 19)or (len(tabs)==21), f"The Tab count is not 21 the actual tab count is {len(tabs)}"


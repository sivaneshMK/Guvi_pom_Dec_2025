import time

import pytest

from conftest import testname
from pages.home_page import HomePage
from utils import menu_utils, test_data_util
from utils.test_data_util import get_test_data


def test_search_content_is_displayed(env_config, driver):
    home_page = HomePage(driver)
    searchstring = get_test_data(env_config, "search_string")
    print(searchstring)
    home_page.enter_search_string(searchstring)
    actual_result = home_page.get_search_content()
    assert actual_result == "YouTube Primetime movies", "YT is not displaying exact search content"

def test_home_page_tab(env_config, driver):
    home_page = HomePage(driver)
    home_page.click_menu(test_data_util.get_data(env_config, "test_home_page_tab", "search_string"))
    print(testname)
    test_data_util.write_data_into_csv(env_config, 'test_home_page_tab', "result", "Pass")
    time.sleep(5)
    home_page.click_menu("Home")
    time.sleep(5)
    tabs = menu_utils.get_all_the_tab_from_home(driver)
    assert (len(tabs) == 19)or (len(tabs)==21), f"The Tab count is not 21 the actual tab count is {len(tabs)}"

@pytest.mark.parametrize("search",[
    ("new movies"),
    ("new movies trailer"),
    ("news"),
    ("latest songs"),
    ("#$(@@#@####"),
    ("v=wftM2K9xmEo")
])
def test_search_content(driver, search):
    home_page = HomePage(driver)
    home_page.enter_search_string(search)

def test_user(get_user_data):
    print(get_user_data["name"])
    print(get_user_data["email"])
    print(get_user_data["mobile"])


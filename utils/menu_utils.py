from pages.home_page import HomePage

def get_all_the_tab_from_home(driver):
    home = HomePage(driver)
    tab_list = []
    for tab in home.get_home_tabs():
        tab_list.append(tab.text)
    return tab_list





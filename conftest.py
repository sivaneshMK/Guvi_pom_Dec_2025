import os
from pathlib import Path

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test")

testname = ""


@pytest.fixture(scope="function")
def driver(env_config, test_name):
    # options = Options()
    # options.add_argument("--disable-notifications")
    # options.add_argument("--start-maximized")
    # options.add_experimental_option("detach", True)
    driver = webdriver.Firefox()
    driver.get(env_config["url"])
    global testname
    testname = test_name
    yield driver
    #driver.quit()

@pytest.fixture(scope="session")
def env_config(request):
    env = request.config.getoption("--env")
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    filepath = os.path.join(root,'config', f"{env}_env_config.yaml")
    # path = os.path.join("config", f"{env}_env_config.yaml")
    # abpath = os.path.abspath(path)
    # print(abpath)
    with open(filepath) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def get_user_data():
    abpath = f"{Path.cwd().parent}\\user_data.yaml"
    print(abpath)
    with open(abpath) as f:
        data = yaml.safe_load(f)
    return data["user"]

@pytest.fixture
def test_name(request):
    return request.node.name
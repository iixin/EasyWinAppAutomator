from typing import Callable
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy as By

APPIUM_PORT = 4723
APPIUM_HOST = "127.0.0.1"

def create_root_driver():
    desktop_driver_options = WindowsOptions()
    desktop_driver_options.load_capabilities(
        {
            "appium:app": "Root"
        }
    )
    desktop_driver = webdriver.Remote(
        f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=desktop_driver_options
    )
    return desktop_driver

def create_running_app_driver(handle):
    driver_options = WindowsOptions()
    driver_options.load_capabilities(
        {
            "appium:appTopLevelWindow": hex(handle)
        }
    )
    driver = webdriver.Remote(
        f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=driver_options
    )
    return driver
    
def find_running_app_by_name(app_name):
    desktop_driver = create_root_driver()
    el = desktop_driver.find_element(By.NAME, app_name)
    handle = el.get_attribute("NativeWindowHandle")
    desktop_driver.quit()
    return int(handle)
    
def main(app_name: str, func: Callable[[webdriver.webdriver.WebDriver], None]):
    try:
        driver = None
        service = AppiumService()
        service.start(
            args=["--address", APPIUM_HOST, "-p", str(APPIUM_PORT)],
            timeout_ms=20000,
        )
        handle = find_running_app_by_name(app_name)
        driver = create_running_app_driver(handle)
        func(driver)
    finally:
        if driver is not None:
            driver.quit()
        if service.is_running:
            service.stop()

def print_xpath(root_node):
    def bfs(node: webdriver.webelement.WebElement, deep, xpath_e):
        nl = node.find_elements(By.XPATH, "/*[1]/*")
        for i, e in enumerate(nl, 1):
            print(" "*deep,xpath_e+f"[{i}]", e.text, e.get_attribute("LocalizedControlType"))
            bfs(e,deep+1, xpath_e + f"[{i}]/*")
    bfs(root_node, 0, "/*[1]/*")
  
def get_all_xpath(driver : webdriver.webdriver.WebDriver):
    root = driver.find_element(By.XPATH, "/*[1]")
    print_xpath(root)
    
def my_task(driver : webdriver.webdriver.WebDriver):
    # TODO: add your task
    node_收藏 = driver.find_element(By.XPATH, "/*[1]/*[2]/*[1]/*[1]/*[4]")
    node_收藏.click()


# main("微信", get_all_xpath)
main("微信", my_task)
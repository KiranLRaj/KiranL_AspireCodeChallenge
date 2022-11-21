
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ChromeBrowserSetup():
    options=Options()
    options.add_argument("--disable-notifications")
    driver=webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe",options=options)
    driver.maximize_window()
    return driver
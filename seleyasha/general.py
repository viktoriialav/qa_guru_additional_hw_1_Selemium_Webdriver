from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait: WebDriverWait = WebDriverWait(driver, timeout=2, poll_frequency=0.25, ignored_exceptions=(WebDriverException, ))

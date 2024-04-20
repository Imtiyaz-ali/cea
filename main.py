from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyperclip
import time


options = Options()
options.add_extension("./extensions/metamask-chrome-10.34.0.crx")
# options.add_argument("--headless")
options.binary_location = "/usr/bin/brave-browser-nightly"

chrome_driver = "./driver/chromedriver"

driver = webdriver.Chrome(options=options, service=Service(chrome_driver))

print("Done")

input("")
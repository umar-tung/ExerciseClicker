from selenium import webdriver
import time

while(True):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--incognito")
    options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=options)
    driver.get('https://pbchealthchallenge.ca/resolutions/5e4ebfd1c075624665/')

    # click submit button
    submit_button = driver.find_element_by_class_name('button')
    submit_button.click()
    driver.close()

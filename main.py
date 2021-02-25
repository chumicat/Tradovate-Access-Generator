import clipboard  # pip install clipboard
import names  # pip install names
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import configform
import tkinter as tk

url = 'https://trader.tradovate.com/register'
last_account_info = 'last_account_info.txt'


def register_account():
    # Dump config
    config_dict = configform.ConfigForm.load_config()
    print(config_dict)

    # Disable pop out ads / screen
    options = Options()
    options.add_argument("--disable-notifications")

    # Launch the page and simulate scroll down for js loading
    print("Fetching form")
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(url)

    # Wait element rendered
    WebDriverWait(chrome, 10,
                  poll_frequency=1,
                  ignored_exceptions=[ElementNotVisibleException,
                                      ElementNotSelectableException,
                                      NoSuchElementException
                                      ])\
        .until(expected_conditions.element_to_be_clickable((By.XPATH, "//input")))
    print('Element found')

    # Fill in form
    counter = f"{int(config_dict['Counter']):04d}"
    chrome.find_element_by_xpath('//a[@class="btn btn-link"]').click()
    input_list = chrome.find_elements_by_xpath("//input")
    input_list[0].send_keys(first_name := names.get_first_name())
    input_list[1].send_keys(last_name := names.get_last_name())
    input_list[2].send_keys(email := "+tradovate{}@".format(counter).join(config_dict['Email'].split('@')))
    input_list[3].send_keys(username := config_dict['User Name'] + counter)
    input_list[4].send_keys(password := config_dict['Password'])
    input_list[5].send_keys(password)

    # Select Describe and checkbox
    chrome.find_element_by_xpath('//span[@class="form-control placeholder"]').click()
    chrome.find_element_by_xpath('//a[text() = "I am New to Trading Futures Online"]').click()
    ActionChains(chrome).move_to_element(chrome.find_element_by_xpath('//label[@class="inline-label"]')).click().perform()

    # Send form
    chrome.find_element_by_xpath('//Button[text() = "Sign up"]').click()

    # Log last account information
    with open(last_account_info, 'w') as file:
        file.write(username + '\n')
        file.write(password)
    clipboard.copy(username)
    time.sleep(1)
    chrome.close()


if __name__ == '__main__':
    # Windows meta
    window = tk.Tk()
    window.title('Tradovate Access Generator')
    window.geometry('500x100')
    window.configure(background='white')
    tk.Button(window, text="Config", command=configform.ConfigForm, width=30, height=5).pack(side=tk.LEFT)
    tk.Button(window, text="Run Automator", command=register_account, width=30, height=5).pack(side=tk.RIGHT)
    window.mainloop()

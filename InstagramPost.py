from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import autoit
import time
import pickle
import os
from xpath_compile import xpath
from config import *
import random


class InstagramPost:

    def __init__(self, username, password, user_data_path=None, headless=False):
        self.username = username
        self.password = password
        # folder where cookie file will be saved
        self.cookie_path = os.path.join(os.getcwd(), "cookies")
        self.user_data_path = user_data_path
        # chromedriver file
        self.driver_path = os.path.join(
            os.getcwd(), "chromedriver\\chromedriver.exe")

        options = Options()

        # Path to your chrome profile
        if user_data_path is not None:
            options.add_argument("--user-data-dir=" + self.user_data_path)
            options.add_argument('--profile-directory=Pessoa 2')

        options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
        if headless == True:
            options.add_argument("--headless")

        self.driver = webdriver.Chrome(
            executable_path=self.driver_path, options=options)

        self.driver.implicitly_wait(5)

    def close_browser(self):
        self.driver.quit()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def do_login(self):
        driver = self.driver

        driver.find_element_by_xpath(
            xpath['first_btn_login_button']).click()

        time.sleep(random.randint(2, 5))

        username_element = driver.find_element_by_xpath(
            xpath['input_username'])
        username_element.clear()
        username_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath(
            xpath['input_password'])
        password_element.clear()
        password_element.send_keys(self.password)

        password_element.send_keys(Keys.ENTER)
        time.sleep(random.randint(2, 5))

        driver.get('https://www.instagram.com/' + username + '/')

    def user_login(self):
        driver = self.driver

        driver.get("https://www.instagram.com/")
        time.sleep(2)

        if self.check_exists_by_xpath(xpath['first_btn_login_button']) == True and os.path.exists(self.get_cookie_path()) == False:
            # do login
            self.do_login()

            # save cookies in file
            self.save_cookies()
        else:
            print("We found cookies file...")

            driver.get("https://www.instagram.com/")

            # set cookies in browser
            self.set_cookies()

            print("Setting cookies to browser...")
            time.sleep(random.randint(3, 5))

            driver.get("https://www.instagram.com/" + self.username + '/')

        print('Username @' + self.username + ' logged in..')

    def get_cookie_path(self):
        return self.cookie_path + '\\' + self.username + "-cookie.pkl"

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(),
                    open(self.get_cookie_path(), "wb"))

    def set_cookies(self):
        for cookie in pickle.load(open(self.get_cookie_path(), "rb")):
            if "sameSite" in cookie and cookie["sameSite"] == "None":
                cookie["sameSite"] = "Strict"
        self.driver.add_cookie(cookie)

    def post_photo_feed(self, photo_full_path, description=None):
        driver = self.driver

        # open file manager to choose the file
        driver.find_element_by_xpath(xpath['xpath_add_photo']).click()

        time.sleep(random.randint(3, 5))

        # select photo from windows file manager
        autoit.win_wait_active("[CLASS:#32770;TITLE:Abrir]", 30)
        autoit.control_send("[CLASS:#32770;TITLE:Abrir]",
                            "Edit1", photo_full_path)
        autoit.control_send(
            "[CLASS:#32770;TITLE:Abrir]", "Edit1", "{ENTER}")

        time.sleep(6)

        # click on next button
        driver.find_element_by_xpath(xpath['xpath_button_avancar']).click()

        time.sleep(2)

        # Add description on post from txt file
        #description_file_name = r"C:\xampp\htdocs\postgenerator\posts\description.txt"
        # self.write_description_from_file(description_file_name)
        self.write_description(description)

        time.sleep(3)

        # click on post
        driver.find_element_by_xpath(xpath['xpath_button_post_action']).click()

        time.sleep(15)

        print('The photo has been posted on feed..')

    def write_description_from_file(self, description_file):
        # get description file content and write into a textbox
        with open(description_file, encoding="utf8") as f:
            lines = f.readlines()

        for l in lines:
            self.send_keys_by_xpath(xpath['xpath_textbox_description'], l)

    def write_description(self, text_description):
        self.send_keys_by_xpath(
            xpath['xpath_textbox_description'], text_description)

    def send_keys_by_xpath(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def get_path(self):
        return os.getcwd()

    def get_path_join(self, file_name):
        return os.path.join(self.get_path(), file_name)


if __name__ == "__main__":

    ip = InstagramPost(username, password, user_chrome_data_path,
                       headless)

    try:
        ip.user_login()

        ip.post_photo_feed(photo_full_path, post_description)

    except Exception as e:
        print("Exception caught: " + str(e))
        # pass
    finally:
        ip.close_browser()

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_visible(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.text_to_be_present_in_element_attribute((how, what), 'style', 'display: none;'))
        except TimeoutException:
            return False
        return True

    def is_not_visible(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element_attribute((how, what), 'style', 'display: none;'))
        except TimeoutException:
            return False
        return True

from .base_page import BasePage
from .locators import RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    def allow_cookies(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(RegisterPageLocators.ALLOW_COOKIES_BUTTON))
        if self.is_element_present(*RegisterPageLocators.ALLOW_COOKIES_BUTTON):
            self.browser.find_element(*RegisterPageLocators.ALLOW_COOKIES_BUTTON).click()

    def click_register_button(self):
        button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        self.browser.execute_script('return arguments[0].scrollIntoView(true);', button)
        button.click()

    def fill_the_email_field(self, email):
        field = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD)
        field.send_keys(email)

    def fill_the_first_name_field(self, first_name):
        field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_FIELD)
        field.send_keys(first_name)

    def fill_the_last_name_field(self, last_name):
        field = self.browser.find_element(*RegisterPageLocators.LAST_NAME_FIELD)
        field.send_keys(last_name)

    def fill_the_phone_field(self, phone):
        field = self.browser.find_element(*RegisterPageLocators.PHONE_FIELD)
        field.send_keys(phone)

    def fill_the_city_field(self, city):
        field = self.browser.find_element(*RegisterPageLocators.CITY_FIELD)
        field.send_keys(city)

    def fill_the_address_field(self, address):
        field = self.browser.find_element(*RegisterPageLocators.ADDRESS_FIELD)
        field.send_keys(address)

    def should_be_invalid_email_message(self):
        assert self.is_visible(*RegisterPageLocators.INVALID_EMAIL_MESSAGE)

    def should_not_be_invalid_email_message(self):
        assert self.is_not_visible(*RegisterPageLocators.INVALID_EMAIL_MESSAGE), 'Message is visible'

    def should_be_correct_invalid_email_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_EMAIL_MESSAGE).text
        assert text == 'Некорректный адрес электронной почты!', "Incorrect email name message's text"

    def should_be_existing_email_message(self):
        assert self.is_visible(*RegisterPageLocators.EXISTING_EMAIL_MESSAGE), 'Message is not visible'

    def should_be_correct_existing_email_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.EXISTING_EMAIL_MESSAGE).text
        assert text == 'Адрес уже зарегистрирован!', "Incorrect existing message's text"

    def should_be_invalid_first_name_message(self):
        assert self.is_visible(
            *RegisterPageLocators.INVALID_FIRST_NAME_LENGTH_MESSAGE), 'Invalid First name message is not presented'

    def should_not_be_invalid_first_name_message(self):
        assert self.is_not_visible(
            *RegisterPageLocators.INVALID_FIRST_NAME_LENGTH_MESSAGE), 'Invalid First name message is presented'

    def should_be_correct_invalid_first_name_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_FIRST_NAME_LENGTH_MESSAGE).text
        assert text == 'Имя должно быть от 1 до 32 символов!', "Incorrect First name message's text"

    def should_be_invalid_last_name_message(self):
        assert self.is_visible(
            *RegisterPageLocators.INVALID_LAST_NAME_LENGTH_MESSAGE), 'Invalid Last name message is not presented'

    def should_not_be_invalid_last_name_message(self):
        assert self.is_not_visible(
            *RegisterPageLocators.INVALID_LAST_NAME_LENGTH_MESSAGE), 'Invalid Last name message is presented'

    def should_be_correct_invalid_last_name_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_LAST_NAME_LENGTH_MESSAGE).text
        assert text == 'Фамилия должна быть от 1 до 32 символов!', "Incorrect Last name message's text"

    def should_be_invalid_phone_message(self):
        assert self.is_visible(
            *RegisterPageLocators.INVALID_PHONE_LENGTH_MESSAGE), 'Invalid Phone message is not presented'

    def should_not_be_invalid_phone_message(self):
        assert self.is_not_visible(
            *RegisterPageLocators.INVALID_PHONE_LENGTH_MESSAGE), 'Invalid Phone message is presented'

    def should_be_correct_invalid_phone_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_PHONE_LENGTH_MESSAGE).text
        assert text == 'Телефон должен быть от 3 до 32 символов!', "Incorrect Phone message's text"

    def should_be_invalid_city_message(self):
        assert self.is_visible(
            *RegisterPageLocators.INVALID_CITY_LENGTH_MESSAGE), 'Invalid City message is not presented'

    def should_not_be_invalid_city_message(self):
        assert self.is_not_visible(
            *RegisterPageLocators.INVALID_CITY_LENGTH_MESSAGE), 'Invalid City message is presented'

    def should_be_correct_invalid_city_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_CITY_LENGTH_MESSAGE).text
        assert text == 'Город должен быть от 2 до 128 символов!', "Incorrect City message's text"

    def should_be_invalid_address_message(self):
        assert self.is_visible(
            *RegisterPageLocators.INVALID_ADDRESS_LENGTH_MESSAGE), 'Invalid Address message is not presented'

    def should_not_be_invalid_address_message(self):
        assert self.is_not_visible(
            *RegisterPageLocators.INVALID_ADDRESS_LENGTH_MESSAGE), 'Invalid Address message is presented'

    def should_be_correct_invalid_address_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.INVALID_ADDRESS_LENGTH_MESSAGE).text
        assert text == 'Заполните поле', "Incorrect Address message's text"

    def should_be_successful_registration_message(self):
        assert self.is_element_present(
            *RegisterPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE), 'Successful registration message is not presented'

    def should_be_correct_registration_message_text(self):
        text = self.browser.find_element(*RegisterPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE).text
        assert text == 'Ваша учетная запись создана!', 'Incorrect registration message'

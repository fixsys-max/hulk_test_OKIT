import pytest
from .pages.register_page import RegisterPage
import time


def get_timestamp():
    timestamp = time.time_ns()
    return str(timestamp)


def generate_new_email():
    email = f'hulk+{get_timestamp()}@test.com'
    return email


class TestRegisterPage:
    link = 'https://hulk.com.ua/index.php?route=account/simpleregister'

    def test_registration_sunshine_scenario(self, browser):
        email = generate_new_email()
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_email_field(email)
        page.fill_the_first_name_field('FirstName')
        page.fill_the_last_name_field('LastName')
        page.fill_the_phone_field('0501234567')
        page.fill_the_city_field('City')
        page.fill_the_address_field('Address')
        page.click_register_button()
        page.should_be_successful_registration_message()
        page.should_be_correct_registration_message_text()

    def test_registration_with_blank_fields_should_not_work(self, browser):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.click_register_button()
        page.should_be_invalid_email_message()
        page.should_be_correct_invalid_email_message_text()
        page.should_be_invalid_first_name_message()
        page.should_be_correct_invalid_first_name_message_text()
        page.should_be_invalid_last_name_message()
        page.should_be_correct_invalid_last_name_message_text()
        page.should_be_invalid_phone_message()
        page.should_be_correct_invalid_phone_message_text()

    @pytest.mark.xfail
    def test_registration_filling_required_fields_works(self, browser):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_email_field(f'hulk+{get_timestamp()}@test.com')
        page.fill_the_first_name_field('FirstName')
        page.fill_the_last_name_field('LastName')
        page.fill_the_phone_field('0501234567')
        page.click_register_button()
        page.should_be_successful_registration_message()
        page.should_be_correct_registration_message_text()

    def test_registration_with_existing_email_should_not_work(self, browser):
        existing_email = 'hulk@test.com'
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_email_field(existing_email)
        page.fill_the_first_name_field('FirstName')
        page.fill_the_last_name_field('LastName')
        page.fill_the_phone_field('0501234567')
        page.fill_the_city_field('City')
        page.fill_the_address_field('Address')
        page.click_register_button()
        page.should_be_existing_email_message()
        page.should_be_correct_existing_email_message_text()

    emails = [
        f'@{get_timestamp()}.com',
        pytest.param(f'{get_timestamp()}@test@com', marks=pytest.mark.xfail),
        f'{get_timestamp()}.test.com',
    ]

    @pytest.mark.parametrize('email', emails)
    def test_registration_with_invalid_email_should_not_work(self, browser, email):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_email_field(email)
        page.click_register_button()
        page.should_be_invalid_email_message()
        page.should_be_correct_invalid_email_message_text()

    first_names = [
        'A',  # 1 character
        'Aswdefrgthyjukzxcvbnmkiuytrewdfr',  # 32 characters
    ]

    @pytest.mark.parametrize('first_name', first_names)
    def test_registration_with_first_name_1_32_chars_long_works(self, browser, first_name):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_first_name_field(first_name)
        page.click_register_button()
        page.should_not_be_invalid_first_name_message()

    first_names = [
        'Sdefrgthyjtgrfedwscvrftgyhnmjuyht',  # 33 characters
        'Bgfdertyuizxcdfrgefrzxcvbgfrthzxcdefrgth',  # 40 characters
    ]

    @pytest.mark.parametrize('first_name', first_names)
    def test_registration_with_first_name_33_and_more_chars_long_should_not_work(self, browser, first_name):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_first_name_field(first_name)
        page.click_register_button()
        page.should_be_invalid_first_name_message()
        page.should_be_correct_invalid_first_name_message_text()

    last_names = [
        'A',  # 1 character
        'Aswdefrgthyjukzxcvbnmkiuytrewdfr',  # 32 characters
    ]

    @pytest.mark.parametrize('last_name', last_names)
    def test_registration_with_last_name_1_32_chars_long_works(self, browser, last_name):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_last_name_field(last_name)
        page.click_register_button()
        page.should_not_be_invalid_last_name_message()

    last_names = [
        'Sdefrgthyjtgrfedwscvrftgyhnmjuyht',  # 33 characters
        'Bgfdertyuizxcdfrgefrzxcvbgfrthzxcdefrgth',  # 40 characters
    ]

    @pytest.mark.parametrize('last_name', first_names)
    def test_registration_with_last_name_33_and_more_chars_long_should_not_work(self, browser, last_name):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_last_name_field(last_name)
        page.click_register_button()
        page.should_be_invalid_last_name_message()
        page.should_be_correct_invalid_last_name_message_text()

    cities = [
        pytest.param('C', marks=pytest.mark.xfail),  # 1 character
        'Aswdefrgthyjukzxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsa',  # 128 characters
    ]

    @pytest.mark.parametrize('city', cities)
    def test_registration_with_normal_city_field_length_works(self, browser, city):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_city_field(city)
        page.click_register_button()
        page.should_not_be_invalid_city_message()

    cities = [
        'Aswdefrgthyjukzxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsat',  # 129 characters
        'Aswdefrgthyjukzderfgthyjukxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsat',  # 140 characters
    ]

    @pytest.mark.parametrize('city', cities)
    def test_registration_with_invalid_long_city_field_should_not_work(self, browser, city):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_city_field(city)
        page.click_register_button()
        page.should_be_invalid_city_message()
        page.should_be_correct_invalid_city_message_text()

    addresses = [
        'C',  # 1 characters
        'Aswdefrgthyjukzxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsa',  # 128 characters
    ]

    @pytest.mark.parametrize('address', addresses)
    def test_registration_with_normal_address_field_length_works(self, browser, address):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_address_field(address)
        page.click_register_button()
        page.should_not_be_invalid_address_message()

    addresses = [
        'Aswdefrgthyjukzxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsat',  # 129 characters
        'Aswdefrgthyjukzderfgthyjukxcvbnmkiuytrewdfrsdfesdfeasdferfdsaasdfrtgfdsgfdsefgfdsgfdsertfgdsdfgrtfgdssdfgrtyhgfdfghtygfdssdferfdesdfwerfdsat',  # 140 characters
    ]

    @pytest.mark.parametrize('address', addresses)
    @pytest.mark.xfail
    def test_registration_with_invalid_long_address_field_should_not_work(self, browser, address):
        page = RegisterPage(browser, self.link)
        page.open()
        page.allow_cookies()
        page.fill_the_address_field(address)
        page.click_register_button()
        page.should_be_invalid_address_message()
        page.should_be_correct_invalid_address_message_text()

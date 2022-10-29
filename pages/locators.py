from selenium.webdriver.common.by import By


class RegisterPageLocators:
    EMAIL_FIELD = (By.ID, 'register_email')
    INVALID_EMAIL_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_email"] [data-rule="regexp"]')
    EXISTING_EMAIL_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_email"] [data-rule="api"]')
    FIRST_NAME_FIELD = (By.ID, 'register_firstname')
    INVALID_FIRST_NAME_LENGTH_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_firstname"] [data-rule="byLength"]')
    LAST_NAME_FIELD = (By.ID, 'register_lastname')
    INVALID_LAST_NAME_LENGTH_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_lastname"] [data-rule="byLength"]')
    PHONE_FIELD = (By.ID, 'register_telephone')
    INVALID_PHONE_LENGTH_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_telephone"] [data-rule="byLength"]')
    CITY_FIELD = (By.ID, 'register_city')
    INVALID_CITY_LENGTH_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_city"] [data-rule="byLength"]')
    ADDRESS_FIELD = (By.ID, 'register_address_1')
    INVALID_ADDRESS_LENGTH_MESSAGE = (By.CSS_SELECTOR, '[data-for="register_address_1"] [data-rule="notEmpty')
    REGISTER_BUTTON = (By.ID, 'simpleregister_button_confirm')
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CLASS_NAME, 'us-main-shop-title')
    ALLOW_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button#oct-policy-btn')

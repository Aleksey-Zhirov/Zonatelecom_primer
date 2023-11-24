import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Replenishment(Base):

    url = 'https://www.zonatelecom.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    payment = "//*[@id='__next']/div[2]/div[2]/div/ul/li[2]/span"
    replenishment = "//*[@id='__next']/div[2]/div[2]/div/ul/li[2]/div/div/ul/li[1]/ul/li[1]/a"
    account_number = "//input[@name='cardNumber']"
    thousand = "//*[@id='__next']/div[2]/div[3]/div/div[1]/div[1]/div/div/form/div[1]/div[3]/div[3]"
    mobile_phone = "//input[@name='phone']"
    choose_zonatelecom = "//*[@id='payment_methods']/div/div/div[1]/div/div[4]"

        # Getters

    def get_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment)))

    def get_replenishment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.replenishment)))

    def get_account_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_number)))

    def get_thousand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.thousand)))

    def get_mobile_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phone)))

    def get_choose_zonatelecom(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_zonatelecom)))

        # Actions

    def click_payment(self):
        self.get_payment().click()
        print("Click payment")

    def click_replenishment(self):
        self.get_replenishment().click()
        print("Click replenishment")

    def input_account_number(self, account_number):
        self.get_account_number().send_keys(account_number)
        print("Input account_number")

    def click_thousand(self):
        self.get_thousand().click()
        print("Click thousand")

    def input_mobile_phone(self, mobile_phone):
        self.get_mobile_phone().send_keys(mobile_phone)
        print("Input mobile_phone")

    def click_choose_zonatelecom(self):
        self.get_choose_zonatelecom().click()
        print("Click choose_zonatelecom")

        # Methods

    def add_replenishment(self):
        with allure.step('Add replenishment'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_payment()
            self.click_replenishment()
            self.input_account_number("1234567890")
            self.click_thousand()
            self.input_mobile_phone("+79876543210")
            self.click_choose_zonatelecom()
            time.sleep(5)
            self.get_screenshot()

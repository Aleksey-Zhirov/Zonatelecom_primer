import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class AudioConversations(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    services = "//*[@id='__next']/div[2]/div[2]/div/ul/li[1]/span"
    audio_conversations = "//*[@id='__next']/div[2]/div[2]/div/ul/li[1]/div/div/ul/li[1]/ul/li[1]/a"
    buy_a_card = "//*[@id='__next']/div[2]/div[3]/div/div[1]/div[3]/div/a[1]/div"
    first_name = "//input[@name='buyerLastname']"
    last_name = "//input[@name='buyerFirstname']"
    email = "//input[@name='buyerEmail']"
    mobile_phone = "//input[@name='buyerPhone']"
    summa = "//input[@name='paymentAmount']"

    # Getters

    def get_services(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.services)))

    def get_audio_conversations(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.audio_conversations)))

    def get_buy_a_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_a_card)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_mobile_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phone)))

    def get_summa(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.summa)))

        # Actions

    def click_services(self):
        self.get_services().click()
        print("Click services")

    def click_audio_conversations(self):
        self.get_audio_conversations().click()
        print("Click audio_conversations")

    def click_buy_a_card(self):
        self.get_buy_a_card().click()
        print("Click buy_a_card")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_mobile_phone(self, mobile_phone):
        self.get_mobile_phone().send_keys(mobile_phone)
        print("Input mobile_phone")

    def input_summa(self, summa):
        self.get_summa().send_keys(summa)
        print("Input summa")

        # Methods

    def audio_conversation(self):
        with allure.step('Add course'):
            self.get_current_url()
            self.click_services()
            self.click_audio_conversations()
            self.click_buy_a_card()
            self.input_first_name("Иван")
            self.input_last_name("Иванов")
            self.input_email("sobaka@sobaka.sob")
            self.input_mobile_phone("89123546596")
            self.input_summa("987654321")
            time.sleep(5)
            self.get_screenshot()

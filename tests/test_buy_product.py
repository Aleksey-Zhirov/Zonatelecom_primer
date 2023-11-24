import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.replenishment import Replenishment
from pages.audio_conversations import AudioConversations
import allure

@allure.description
def test_select_product():
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test")

    reple = Replenishment(driver)
    reple.add_replenishment()

    audio = AudioConversations(driver)
    audio.audio_conversation()

    print("Finish test")

    time.sleep(5)
    driver.quit()

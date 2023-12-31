import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\New\\PycharmProjects\\ZonaTelecom\\screen\\' + name_screenshot)

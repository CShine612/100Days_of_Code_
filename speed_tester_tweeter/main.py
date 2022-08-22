import config
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(config.chrome_driver)
        self.promised_up = config.promised_up
        self.promised_down = config.promised_down
        self.up = None
        self.down = None

    def get_internet_speeds(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)

        consent = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-cookiebutton"]')
        consent.click()

        time.sleep(2)

        pop_up_x = self.driver.find_element_by_xpath('//*[@id="_evidon-l3"]/button')
        pop_up_x.click()

        start = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()

        time.sleep(40)

        close_pop_up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        close_pop_up.click()

        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = down.text

        up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = up.text

        self.driver.quit()

    def tweet_at_provider(self):
        if self.promised_up > float(self.up) and self.promised_down > float(self.down):
            return
        # if False:
            pass
        else:
            tweet_text = f"Why is my internet speed {str(self.down)}mb down and {str(self.up)}mb up " \
                         f"when my contract says I will be served a minimum of " \
                         f"{self.promised_down}mb down and {self.promised_up}mb up"

            # tweet_text = "test"

            self.driver.get("https://twitter.com/i/flow/login")

            # time.sleep(15)
            #
            # click_to_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            # click_to_login.click()

            time.sleep(15)

            email = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
            email.send_keys(config.twitter_email)
            email.send_keys(Keys.ENTER)

            time.sleep(2)

            username = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(config.username)
            username.send_keys(Keys.ENTER)

            time.sleep(2)

            password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(config.twitter_password)
            password.send_keys(Keys.ENTER)

            time.sleep(2)

            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            tweet.send_keys(tweet_text)

            send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
            send_tweet.click()

            time.sleep(10)

            self.driver.quit()



test = InternetSpeedTwitterBot()

test.get_internet_speeds()
time.sleep(2)
test.tweet_at_provider()
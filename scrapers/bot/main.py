from constants import BASE_URL,DRIVER_PATH
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class OpenCollective(webdriver.Chrome):
    def __init__(self, driver_path=DRIVER_PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(OpenCollective, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self):
        if self.teardown:
            self.quit()

    def land_on_home_page(self):
        self.get(BASE_URL)

    def get_info(self):
        try:
            img_elements = self.find_elements(By.CLASS_NAME, 'Table__Avatar-sc-fu01nh-1')
            for i in range(len(img_elements)):
                try:
                    img_xpath = f'//*[@id="__next"]/div/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[1]/div/img'
                    org_url = self.find_element(By.XPATH, img_xpath)
                    parts = org_url.get_attribute('src').split('/')
                    slug = parts[3]
                    print("SLUG", slug)
                    try:
                        with open("org_file.txt", "a") as file:
                            file.write(f"{slug} \n")
                    except:
                        print("writing to the file didnt work")
                except:
                    pass
        except:
            pass
    
    def pagination(self):
        NEXT_PATH = '//*[@id="__next"]/div/main/div/div[2]/div[2]/div[1]/div[4]/div/button[2]'
        try:
            nbtn = self.find_element(
                By.XPATH, NEXT_PATH
            )
            nbtn.click()
        except:
            print('Cant locate Next button')


def run_scraper():
   with OpenCollective(teardown=True) as bot:
    bot.land_on_home_page()
    for x in range(386):
        bot.get_info()
        try:
            bot.pagination()
        except:
            print('No more pages to paginate.')
        # time.sleep(5)

run_scraper()
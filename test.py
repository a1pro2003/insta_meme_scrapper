import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class GoogleOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_google_search_page(self):
         driver = self.driver
         driver.get("http://www.cdot.in")
         window_before = driver.window_handles[0]
        #  print(window_before)
        #  driver.find_element_by_xpath("//a[@href='http://www.cdot.in/home.htm']").click()
        #  window_after = driver.window_handles[1]
        #  driver.switch_to_window(window_after)
        #  print(window_after)
        #  driver.find_element_by_link_text("ATM").click()
         driver.switch_to_window(window_before)
         time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
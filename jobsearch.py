import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class TestLoginMenu(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_job_search(self):
        driver = self.browser
        driver.maximize_window()
        driver.get("https://www.cermati.com/app") #open cermati's website
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='safe-area']/header/div/div[2]/div[2]/div/div[3]/div[2]").click() #click account button
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='identifier']").send_keys("087776604905") #insert phone number
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Cermati123") #insert password
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='safe-area']/div[2]/div[2]/div/button[2]").click() #click login button
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='safe-area']/header/div/div[2]/div[2]/div/div[1]/div[2]").click() #click Beranda button
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll until the bottom of the page
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='safe-area']/footer/div[1]/div/div/nav/div/div[1]/ul/li[4]/a").click() #click Karir
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='job-title']").send_keys("Software Engineer In Test") #fill search bar with "Software Engineer In Test"
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='career-landing']/div/div[4]/div/button").click() #click Find Jobs
        time.sleep(3)
        driver.execute_script("window.scrollTo(750, 355)")
        time.sleep(5)
        driver.save_screenshot("Software Engineer In Test Job Lists.jpg")
        time.sleep(3) 

def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
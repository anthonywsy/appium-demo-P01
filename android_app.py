import os
import unittest
import time
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AndroidAppTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH(
            '../apk/P01_AndroidApp.2.apk'
        )
        #desired_caps['appPackage'] = 'P01_AndroidApp.P01_AndroidApp'
        #desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_androidapp(self):
        el = self.driver.find_element_by_name("Hello World, Click Me!")
        el.click()
        
        e2 = self.driver.find_element_by_name("Click to login page")
        e2.click()
        
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[1].send_keys("someone@appium.io")
       
        e3 = self.driver.find_element_by_name("Login")
        e3.click()
        
        time.sleep(3)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

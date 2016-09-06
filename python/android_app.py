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
        #el.click()
        
        e2 = self.driver.find_element_by_name("Click to login page")
        e2.click()
        
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        #textfields[0].send_keys("Appium User")
        #textfields[1].send_keys("someone@appium.io")
       
        #self.assertEqual('Appium User', textfields[0].text)
        #error:self.assertEqual('someone@appium.io', textfields[1].text)
        
        e3 = self.driver.find_element_by_name("Login")
        e3.click()
        
        gallery1 = self.driver.find_elements_by_class_name("android.widget.Gallery")
        #self.driver.scroll(gallery1[len(gallery1)-1],gallery1[0])
        #error:self.driver.swipe(0,0,100,0,0)
        #error:self.driver.scroll(gallery1[0],gallery1[1])
        #self.driver.execute_script("mobile: scroll", {"direction": 'right'})
        
        #self.driver.execute_script("mobile: scroll", {"direction": 'right', 'element': gallery1})
        #self.driver.execute_script("mobile: scroll", {"direction": "right", element: gallery1})
        #self.driver.execute_script("mobile: scroll", {"direction": "down", element: gallery1.getAttribute("id")})
        img1 = self.driver.find_elements_by_class_name("android.widget.ImageView")
        #img1[0].click()
        gallery1[0].click()
        #self.driver.scroll(img1[0],img1[len(img1)-1])
        #self.driver.scroll(img1[len(img1)-1],img1[0])
        self.driver.scroll(img1[1],img1[0])
        gallery1[0].click()
        #img1[1].click()
        
        time.sleep(3)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

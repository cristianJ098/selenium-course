import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Helloworld(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hellow_world(self):
       driver = self.driver
       driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')


    @classmethod
    def tearDownClass(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
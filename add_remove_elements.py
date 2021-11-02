import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('how many elements will you add: '))
        elements_remove = int(input('How many elements will you remove: '))
        total_elements = elements_added - elements_remove

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except :
                print('your try to delete more elements that exist')
                break
        if total_elements >  0:
            print(f'there are {total_elements} in Screen')

        else:
            print('there are 0 elements on screen ')

        sleep(3)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reports', report_name= 'hello-world-report'))
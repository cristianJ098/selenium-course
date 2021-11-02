import unittest
from selenium import webdriver
from time import sleep

ROWS = 5

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        driver = self.driver
        driver.get('pagina de prueba') #no la pongo porque la IA de comentarios de platzi me la borra
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for _ in range(ROWS)]
        
        for i in range(ROWS):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(ROWS - 1):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

"""
tabla diseñada con prettytable


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class Tables(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'chromedriver')
        driver = self.driver
	#Aquí pongan el enlace, como no es https no me permite añadir mi comentario.
        driver.get()

    def test_table(self):
        driver = self.driver
        rows = []
        ptable = PrettyTable()
        for i in range(5):
            header = driver.find_element(
                By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            for j in range(4):
                row = driver.find_element(
                    By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                rows.append(row.text)
            ptable.add_column(header.text, rows)
            rows.clear()

        print(ptable)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
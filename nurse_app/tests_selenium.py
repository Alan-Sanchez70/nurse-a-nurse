# tests_selenium.py

from selenium import webdriver
import unittest

class SeleniumTests(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (using Chrome)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_open_homepage(self):
        # Open the homepage and check if the title contains "something"
        self.driver.get("http://127.0.0.1:8000/")  # Replace with your local development server URL
        self.assertIn("Home", self.driver.title)

    def test_create_project(self):
        # Open the create project page, fill out a form, submit it, and check the result
        self.driver.get("http://127.0.0.1:8000/createProject/")  

        
        name_input = self.driver.find_element_by_name('name')
        name_input.send_keys("New Scrub")

        size_input = self.driver.find_element_by_name('size')
        size_input.send_keys("L")

        color_input = self.driver.find_element_by_name('color')
        color_input.send_keys("Blue")

        description_input = self.driver.find_element_by_name('description')
        description_input.send_keys("Testing description")

        is_new_checkbox = self.driver.find_element_by_name('is_new')
        is_new_checkbox.click()

        price_input = self.driver.find_element_by_name('price')
        price_input.send_keys("30")

        submit_button = self.driver.find_element_by_name('submit_button')
        submit_button.click()

        # Checking if the form submission redirects to the expected page
        self.assertIn("New Scrub", self.driver.title)

if __name__ == "__main__":
    unittest.main()

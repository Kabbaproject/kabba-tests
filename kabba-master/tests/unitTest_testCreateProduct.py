# Unit test file to determine if the Customer List page is displayed when the user
# clicks the 'Customers' button in the navigation pane of the mfscrm app
# Customer list is shown if the 'summary' button exists on the page
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # Test if Customer list is displayed when Customers is clicked in the Navigation bar
    # Customer list is shown if the 'summary' button exists on the page
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)  # pause to allow screen to load

        # # click the login button - user must be logged in to view the Customer list
        # elem = driver.find_element(By.XPATH, '//*[@id="navbarNavAltMarkup"]/div/a[2]').click()

        # find the username and password input boxes and login
        # user = "testuser"  # must be a valid username for the application
        # pwd = "test!234"  # must be the password for a valid user
        #
        # elem = driver.find_element(By.ID, "id_username")
        # elem.send_keys(user)
        # elem = driver.find_element(By.ID, "id_password")
        # elem.send_keys(pwd)
        # elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to load

        # find products
        elem = driver.find_element(By.XPATH, '//*[@id="navbarNavAltMarkup"]/div/a[4]').click()

        time.sleep(5)  # pause to allow screen to change
        try:
            #test create product button
            elem = driver.find_element(By.XPATH, '/html/body/div/a')
            print("Test passed - products can be added")
            assert True

        except NoSuchElementException:
            self.fail("Products cannot be added")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

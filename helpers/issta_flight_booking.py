from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ISSTAFlightBooking:

    # Initialize the WebDriver and set default wait time
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    # Retrieve an element by XPath and index(for using the asserts)
    def get_element_by_xpath(self, xpath, index):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return elements[index - 1] if len(elements) >= index else None

    # Navigate to the ISSTA homepage and click the flight tab
    def navigate_to_flight_tab(self):
        self.driver.get("https://www.issta.co.il/")
        flight_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='ng-star-inserted'][contains(text(),'טיסות')]"))
        )
        flight_tab.click()
        time.sleep(3)

    # Enter a location in the specified input field and select it from the dropdown (for departure and detination actions)
    def enter_location(self, placeholder, location, select_xpath):
        time.sleep(2)
        input_element = self.driver.find_element(By.XPATH, f"(//input[@placeholder='{placeholder}'])[1]")
        input_element.click()
        input_element.send_keys(location)
        time.sleep(1)
        select_element = self.driver.find_element(By.XPATH, select_xpath)
        select_element.click()
        time.sleep(5)

    # Select start and end dates for the flight
    def select_dates(self, start_date_xpath, end_date_xpath):
        start_date = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, start_date_xpath))
        )
        start_date.click()
        time.sleep(5)
        end_date = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, end_date_xpath))
        )
        end_date.click()
        time.sleep(5)

    # Choose the number of passengers for the flight
    def choose_passengers(self, passenger_button_xpath, select_button_xpath):
        passenger_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, passenger_button_xpath))
        )
        passenger_button.click()
        time.sleep(5)
        select_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, select_button_xpath))
        )
        select_button.click()
        time.sleep(5)

    # Verify that the location entered in the input field matches the expected value
    def assert_location(self, placeholder, expected_value):
        actual_value = self.driver.find_element(By.XPATH, f"(//input[@placeholder='{placeholder}'])[1]").get_attribute(
            'value')
        return actual_value == expected_value

    # Verify that the start and end dates are correctly selected
    def assert_dates(self, start_date_xpath, end_date_xpath):
        start_date_element = self.get_element_by_xpath(start_date_xpath, 3)
        start_date = start_date_element.get_attribute('value') if start_date_element else 'Not found'

        end_date_element = self.get_element_by_xpath(end_date_xpath, 3)
        end_date = end_date_element.get_attribute('value') if end_date_element else 'Not found'

        return start_date != 'Not found' and end_date != 'Not found', start_date, end_date

    # Click the search button to find flights
    def click_search_button(self, button_xpath):
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        search_button.click()
        time.sleep(5)

    # Select the first available flight and switch to the new tab
    def select_first_flight(self, first_flight_xpath):
        first_flight = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, first_flight_xpath))
        )
        first_flight.click()

    def select_first_flight(self, xpath):
        try:
            first_flight = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            first_flight.click()
            time.sleep(10)
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except TimeoutException:
            print("First flight selection timed out or not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Scroll down the page and click the submit button
    def click_submit_button(self, xpath):
        self.driver.execute_script("window.scrollBy(20, window.innerHeight);")
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        submit_button.click()
        time.sleep(5)

    # Close the browser after each test
    def close(self):
        self.driver.quit()

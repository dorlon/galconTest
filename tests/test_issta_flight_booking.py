import unittest
from helpers.issta_flight_booking import ISSTAFlightBooking


class TestISSTAFlightBooking(unittest.TestCase):

    def setUp(self):
        # Initialize the ISSTAFlightBooking instance before each test
        self.flight_booking = ISSTAFlightBooking()

    def test_flight_booking(self):
        # Navigate to the flight tab on the ISSTA website
        self.flight_booking.navigate_to_flight_tab()

        # Enter departure location
        self.flight_booking.enter_location('בחר מוצא', 'אמסטרדם, שדה תעופה ZYA',
                                           "//div[@class='ng-form-row ng-form-row-focus']//i[@class='ng-icon-from ng-star-inserted']")

        # Enter destination location
        self.flight_booking.enter_location('בחירת יעד בארץ או בחו"ל', 'תל אביב, ישראל',
                                           "//div[contains(@class,'ng-form-row ng-form-row-focus')]//div[contains(@class,'ng-dropdown-autocomplete')]")

        # Select the start and end dates for the flight (10-07-24 : 15-07-24)
        self.flight_booking.select_dates("(//span[contains(text(),'10')])[2]", "(//span[contains(text(),'15')])[2]")

        # Choose the number of passengers (1 passenger)
        self.flight_booking.choose_passengers("(//button[contains(@type,'button')][normalize-space()='-'])[5]",
                                              "(//button[contains(@type,'button')][contains(text(),'בחירה')])[1]")

        # Verify the departure location
        self.assertTrue(self.flight_booking.assert_location('בחר מוצא', 'אמסטרדם, שדה תעופה ZYA'))

        # Verify the destination location
        self.assertTrue(self.flight_booking.assert_location('בחירת יעד בארץ או בחו"ל', 'תל אביב, ישראל'))

        # Verify the selected dates
        dates_assertion, start_date, end_date = self.flight_booking.assert_dates("//input[@id='start_date']", "//input[@id='end_date']")
        self.assertTrue(dates_assertion)
        print(f'Start Date (3rd occurrence): {start_date}')
        print(f'End Date (3rd occurrence): {end_date}')

        # Click on the search button to find flights
        self.flight_booking.click_search_button("(//button[contains(text(),'מצאו לי טיסות זולות')])[1]")

        # Select the first available flight
        self.flight_booking.select_first_flight(
            "(//a[@class='btn btn-block btn-primary btn-details'][contains(text(),'פרטי טיסה')])[1]")

        # Click the submit button on the flight details page
        self.flight_booking.click_submit_button("//button[@type='submit']")

    # Close the browser after each test
    def tearDown(self):
        self.flight_booking.close()


if __name__ == "__main__":
    unittest.main()

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Curls
from locators import Locators



class TestTransitionViaMyAccountButton:
    def test_transition_via_my_account_button(self, driver, login):
    #Arrange fixture_login
    #Act
        driver.find_element(*Locators.MY_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.PROFILE))
    # Assert
        assert driver.current_url == Curls.profile_page

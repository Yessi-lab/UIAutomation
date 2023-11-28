import unittest
import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

"""
This is an automated test suite within a functional test plan using Selenium WebDriver and unittest 
to automate tests for an e-commerce site called "La Tienda de Valentina". 

The tests cover various basic scenarios such as checking the title of the main page, navigating to different 
pages, searching for a product, and logging in to a personal account. 
"""

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = self.initialize_driver()
        self.driver.get("https://latiendadevalentina.com/")

    def tearDown(self):
        self.driver.quit()

    def initialize_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class ValentinaMainPageTest(BaseTest):       
    
    def test_main_page_title(self):
        """
        Verify that the title of the main page matches the expected value.
        """       
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches())

    def test_clothes_button(self):
        """
        Verify that clicking the "Clothes" button on the main page navigates to the Clothes page.
        """
        main_page = page.MainPage(self.driver)
        main_page.click_clothes_button()

        clothes_page = page.ClothesPage(self.driver)
        self.assertTrue(clothes_page.is_loaded())

    def test_beauty_button(self):
        """
        Verify that clicking the "Beauty" button on the main page navigates to the Beauty page.
        """
        main_page = page.MainPage(self.driver)
        main_page.click_beauty_button()

        beauty_page = page.BeautyLandingPage(self.driver)
        self.assertTrue(beauty_page.is_loaded())

    def test_footer_link(self):
        """
        Verify that clicking the "Returns" link in the footer of the main page navigates to the Returns page.
        """
        main_page = page.MainPage(self.driver)
        main_page.click_footer_link()

        footer_page = page.ReturnsPage(self.driver)
        self.assertTrue(footer_page.is_loaded())

class ValentinaOrgSearchTest(BaseTest):
    def test_search_results_page(self):
        """
        Verify that a search for a product returns at least one result
        """
        main_page = page.MainPage(self.driver)
        main_page.send_keys()

        results_page = page.SearchResultPage(self.driver)
        self.assertTrue(results_page.is_results_found())

class ValentinaOrgAccountTest(BaseTest):
    def test_login_page_access(self):
        """
        Verify that clicking the "Log In" button takes you to the Login page
        """
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()

        login_page = page.LoginPage(self.driver)
        self.assertTrue(login_page.is_loaded())

    def test_successful_login(self):
        """
        Verify that a user can log in to their personal account
        """
        main_page = page.MainPage(self.driver)
        main_page.accept_cookies()
        main_page.click_login_button()

        login_page = page.LoginPage(self.driver)
        login_page.form_login_to_account()
        login_page.click_login_to_account()

        personal_account = page.PersonalAccountPage(self.driver)
        self.assertTrue(personal_account.is_loaded())

class ValentinaShoppingCartTest(BaseTest):
    def test_add_product_to_cart(self):
        """
        Verify that a user can add a product to their shopping cart
        """
        main_page = page.MainPage(self.driver)
        main_page.accept_cookies()
        main_page.click_clothes_button()

        clothes_page = page.ClothesPage(self.driver)
        clothes_page.click_product()

        product_page = page.ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.accept_cookies()
        product_page.acces_shopping_cart()
        WebDriverWait(self.driver, 10)

        shopping_cart_count = page.ShoppingCartPage(self.driver)
        shopping_cart_count= shopping_cart_count.shopping_cart_count()
        self.assertTrue(shopping_cart_count == "1")

if __name__ == "__main__":
    unittest.main()

from locator import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def accept_cookies(self):
        try:
            cookie_accept = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT))
            cookie_accept.click()
        except:
            pass

    def is_title_matches(self):
        return "VALENTiNA | Tienda de Ropa online para Mujer" in self.driver.title
    
    def send_keys(self):
        search = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        search.clear()
        search.send_keys("Abrigos")
        search.send_keys(Keys.RETURN)
        return SearchResultPage(self.driver)

    def click_clothes_button(self):
        element = self.driver.find_element(*MainPageLocators.CLOTHES_BUTTON)
        element.click()
        return ClothesPage(self.driver)
    
    def click_beauty_button(self):
        element = self.driver.find_element(*MainPageLocators.BEAUTY_BUTTON)
        element.click()
        return BeautyLandingPage(self.driver)
    
    def click_login_button(self):
        element_avatar = self.driver.find_element(*MainPageLocators.LOGIN_AVATAR)
        element_avatar.click()

        element_login_button = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element_login_button.click()

        return LoginPage(self.driver)
    
    def click_footer_link(self):
        footer_element = self.driver.find_element(*MainPageLocators.FOOTER_LINK)
        footer_element.click()

        return ReturnsPage(self.driver)
    
class LoginPage(BasePage):
    def is_loaded(self):
        return "Cuenta" in self.driver.title
    
    def form_login_to_account(self):
        element_mail = self.driver.find_element(*LoginPageLocators.EMAIL_BOX)
        element_mail.clear()
        element_mail.send_keys("test_viu@outlook.com")
        element_mail.send_keys(Keys.RETURN)

        element_password = self.driver.find_element(*LoginPageLocators.PASSWORD_BOX)
        element_password.clear()
        element_password.send_keys("pepe3108!!")
        element_password.send_keys(Keys.RETURN)

    def click_login_to_account(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BOTTON)
        element.click()
        return PersonalAccountPage(self.driver)
    
class PersonalAccountPage(BasePage):
    def is_loaded(self):
        return "Cuenta" in self.driver.title

class BeautyLandingPage(BasePage):
    def is_loaded(self):
        return "Landing cosmetics" in self.driver.title

class ClothesPage(BasePage):
    def is_loaded(self):
        return "Ropa de Mujer" in self.driver.title
    
    def click_product(self):
        element_first_card = self.driver.find_element(*ClothesPageLocators.FIRST_CARD)
        element_link = element_first_card.find_element(*ClothesPageLocators.LINK_CARD)
        
        actions = ActionChains(self.driver)
        actions.move_to_element(element_link).click().perform()

        return ProductPage(self.driver)

class ProductPage(BasePage):
    def get_product_name(self):
        element_title = self.driver.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return element_title.text

    def get_product_price(self):
        element_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return element_price.text
    
    def add_to_cart(self):
        element_size_selector = self.driver.find_element(*ProductPageLocators.SIZE_SELECTOR)
        size_options = element_size_selector.find_elements(*ProductPageLocators.SIZE_OPTION)
        size_options[1].click()

        element_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        element_to_cart_button.click()

    def acces_shopping_cart(self):
        element_cart = self.driver.find_element(*ProductPageLocators.ICON_SHOPPING_CART)
        element_cart.click()
       
        return ShoppingCartPage(self.driver)
    
    def accept_cookies(self):
        try:
            cookie_accept = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT))
            cookie_accept.click()
        except:
            pass

class ShoppingCartPage(BasePage):

    def shopping_cart_count(self):
        element_counter = self.driver.find_element(*ShoppingCartPageLocators.SHOPPING_CART_COUNTER)
        return element_counter.text

    def get_cart_product_name(self):
        element_cart_product_name = self.driver.find_element(*ShoppingCartPageLocators.PRODUCT_TITLE)
        return element_cart_product_name.text
    
    def get_cart_product_price(self):
        element_cart_product_price = self.driver.find_element(*ShoppingCartPageLocators.PRODUCT_PRICE)
        return element_cart_product_price.text
    
class SearchResultPage(BasePage):
    def is_loaded(self):
        return "Abgrigos" in self.driver.title

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
    
class ReturnsPage(BasePage):
    def is_loaded(self):
        return "Devoluciones y cambios" in self.driver.title
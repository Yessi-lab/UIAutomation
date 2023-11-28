from selenium.webdriver.common.by import By

class MainPageLocators(object):  
    MID_SEASON_BUTTON = (By.LINK_TEXT, "Mid Season")
    CLOTHES_BUTTON = (By.LINK_TEXT, "Ropa")
    SHOES_BUTTON = (By.PARTIAL_LINK_TEXT, "Zapatos")
    ACCESSORY_BUTTON = (By.LINK_TEXT, "Complementos")
    BATH_BUTTON = (By.LINK_TEXT, "Baño")
    INTIMI_BUTTON = (By.LINK_TEXT, "Intimi")
    JEWELLERY_BUTTON = (By.LINK_TEXT, "Joyería")
    BEAUTY_BUTTON = (By.LINK_TEXT, "Beauty")
    OUTLET_BUTTON = (By.LINK_TEXT, "Outlet")
    SEARCH_BOX  = (By.NAME, "q")
    LOGIN_AVATAR =  (By.ID, "acco")
    LOGIN_BUTTON = (By.LINK_TEXT, "INICIAR SESIÓN")
    FOOTER_LINK = (By.PARTIAL_LINK_TEXT, "Gestiona")
    COOKIE_ACCEPT = (By.XPATH, "//span[contains(text(), 'Acepto')]")
    NEWSLETTER_POPUP = (By.CSS_SELECTOR, 'div[data-testid="POPUP"]')
    NEWSLETTER_CLOSE  = (By.XPATH,'//svg[@title="Close form 1"]')

class ClothesPageLocators(object):
    FIRST_CARD = (By.CSS_SELECTOR, '.card')
    LINK_CARD = (By.CSS_SELECTOR, 'a')

class ProductPageLocators(object):
    SIZE_SELECTOR = (By.ID, "dv_swatches")
    SIZE_OPTION = (By.CLASS_NAME, "swatch-element")
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@id="btn_anadir_carrito"]')
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
    PRODUCT_PRICE = (By.CLASS_NAME, "product-price-mov")
    ICON_SHOPPING_CART = (By.CSS_SELECTOR, 'a.nav-link.cartIcon')


class ShoppingCartPageLocators(object):
    SHOPPING_CART_COUNTER = (By.CSS_SELECTOR, "span.cart-count")

class LoginPageLocators(object):
    EMAIL_BOX = (By.NAME, "customer[email]")
    PASSWORD_BOX = (By.NAME, "customer[password]")
    LOGIN_BOTTON = (By.XPATH, "//button[@class='button button-black' and text()='INICIAR SESIÓN']")
   
import time

from .base_page import BasePage
from .locators import SitePageLocators
from selenium.webdriver.support import expected_conditions as EC

class SitePage(BasePage):
    def should_be_site(self):
        self.should_be_basket()


    def should_be_basket(self):
        basket = self.browser.find_element(*SitePageLocators.ADD_BASKET)
        assert basket, "basket dont find"
        basket.click()

    def examination_basket(self):
        name_product = self.browser.find_element(*SitePageLocators.NAME_PRODUCT).text
        name_product_add = self.browser.find_element(*SitePageLocators.NAME_PRODUCT_ADD).text
        assert name_product == name_product_add, "Название товара в корзине не совпадает с добавленным товаром"
        print(name_product)
        print(name_product_add)

    def examination_cost(self):
        time.sleep(3)
        cost_product = self.browser.find_element(*SitePageLocators.COST_PRODUCT).text
        print(cost_product)
        cost_product_basket = self.browser.find_element(*SitePageLocators.COST_PRODUCT_ADD).text
        print(cost_product_basket)
        assert cost_product == cost_product_basket, "Цена совпадает"



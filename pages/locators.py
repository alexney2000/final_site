from selenium.webdriver.common.by import By


class SitePageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_PRODUCT_ADD = (By.CSS_SELECTOR, "div.alertinner > strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    COST_PRODUCT_ADD = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


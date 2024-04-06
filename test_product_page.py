from pages.product_page import SitePage
import pytest


@pytest.mark.parametrize('i', [
    pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}",
                 marks=pytest.mark.xfail(
                     reason="some bug")) if i == 7 else f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
    for i in range(10)
])

def test_guest_can_add_product_to_basket(browser,i):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
    page = SitePage(browser, link)
    page.open()
    page.should_be_basket()
    page.solve_quiz_and_get_code()
    page.examination_basket()
    page.examination_cost()


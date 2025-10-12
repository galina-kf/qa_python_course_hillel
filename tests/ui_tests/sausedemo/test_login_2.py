from .conftests import *
from qa_python_cource_hillel.settings import settings


def test_product_page_is_open(driver, login_page, products_page):
    login_page.open_page()
    login_page.login_user(settings.user, settings.password)
    products_page.products_images()




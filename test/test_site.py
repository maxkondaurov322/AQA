from selenium.webdriver.common.by import By
import time
from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_s6(browse):
    homepage = Homepage(browse)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browse)
    product_page.check_title_is("Samsung Galaxy S6")


def test_two_monitors(browse):
    homepage = Homepage(browse)
    homepage.open()
    homepage.click_monitor_link()
    time.sleep(3)
    homepage.check_products_count(2)
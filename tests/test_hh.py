import allure
from page.page import Page


@allure.tag('web')
@allure.title('Select city')
def test_search_city():
    p = Page()
    p.open()
    p.fill_city()


def test_search_job():
    p = Page()
    p.open()
    p.search_job()


def test_search_resume():
    p = Page()
    p.open()
    p.search_resume()


def test_search_company():
    p = Page()
    p.open()
    p.search_company()


def test_check_resume():
    p = Page()
    p.open()
    p.search_resume()


def test_check_city():
    p = Page()
    p.open()
    p.fill_city()

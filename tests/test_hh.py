import allure

from pages.page import MainPage


def test_search_city():
    m = MainPage()
    m.select_city()
    m.check_city()


def test_search_company():
    m = MainPage()
    m.find_company()
    m.check_company()


def test_search_resume():
    m = MainPage()
    m.search_resume()
    m.check_resume()


def test_search_job():
    m = MainPage()
    m.search_job()
    m.check_job()

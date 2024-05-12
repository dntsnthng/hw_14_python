from pages.page import MainPage


def test_search_city():
    m = MainPage()
    m.select_city()
    m.check_city()



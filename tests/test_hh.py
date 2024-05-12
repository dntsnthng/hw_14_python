import allure

from pages.page import MainPage


@allure.tag("WEB")
@allure.title('Открытие страницы')

def test_search_city():
    m = MainPage()
    m.select_city()
    m.check_city()

@allure.title('Поиск компании')
def test_search_company():
    m = MainPage()
    m.find_company()
    m.check_company()

@allure.title('Поиск резюме')
def test_search_resume():
    m = MainPage()
    m.search_resume()
    m.check_resume()

@allure.title('Поиск работы')
def test_search_job():
    m = MainPage()
    m.search_job()
    m.check_job()

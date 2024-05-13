import allure

from pages.home_page import MainPage


@allure.tag("WEB")
@allure.title('Выбор города')
def test_search_city():
    main = MainPage()
    main.select_city()
    main.check_city()

@allure.title('Поиск компании')
def test_search_company():
    main = MainPage()
    main.find_company()
    main.check_company()

@allure.title('Поиск резюме')
def test_search_resume():
    main = MainPage()
    main.search_resume()
    main.check_resume()

@allure.title('Поиск работы')
def test_search_job():
    main = MainPage()
    main.search_job()
    main.check_job()

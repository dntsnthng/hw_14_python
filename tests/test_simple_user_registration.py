import allure
from page.page import Page


@allure.tag('web')
@allure.title('Successful search job')
def test_one_hh():
    p = Page()
    with allure.step('Search job'):
        p.add_resume()


def test_check():
    p = Page()
    with allure.step('Checking user data'):
        p.check_data()

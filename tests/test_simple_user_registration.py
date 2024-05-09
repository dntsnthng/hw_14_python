import time
from selene import have
from selene.support.shared import browser
import allure


# def open(self):
#     browser.open('/')
#     browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
#         have.size_greater_than_or_equal(3)
#     )
#     browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
#     return self

@allure.step('ВЫбираем город')
def test_fill_city_():
    browser.open('/')
    browser.element('.supernova-navi-item_area-switcher-button').click()
    browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()


@allure.step('ВЫбираем компанию')
def test_search_company_():
    browser.open('/')
    browser.element('#a11y-search-input').type('Юmoney').press_enter()
    browser.element('[data-qa="bloko-modal-close"]').click()
    browser.element('[data-hh-tab-id="employersList"]').click()
    browser.element('[href="/employer/655542"]').click()


@allure.step('Резюме')
def test_add_resume():
    browser.open('/')
    browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
    browser.element('[data-qa="bloko-modal-close"]').click()
    browser.element('[data-hh-tab-id="resumeSearch"]').click()
    browser.element('[data-qa="serp-item__title"]').click()


@allure.step('Ищем работу')
def test_search_job():
    browser.open('/')
    browser.element('#a11y-search-input').type('Python').press_enter()
    browser.element('[data-qa="bloko-modal-close"]').click()
    browser.element('[name=part_time][value=start_after_sixteen]+span').click()
    browser.execute_script('window.scrollTo(0, 1000)')
    time.sleep(3)
    browser.element('[name=salary][value="50000"]+span').click()
    browser.execute_script('window.scrollTo(0, 4400)')
    browser.element('[class=bloko-checkbox__input][value="124"]+span').click()
    browser.element('[name=education][value="not_required_or_not_specified"]+span').click()
    time.sleep(3)


@allure.step('Тест на город')
def test_should_have_city():
    browser.open('/')
    browser.element('.supernova-navi-item_area-switcher-button').click()
    browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()
    browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))


@allure.step('Тест на компанию')
def test_should_have_company():
    browser.open('/')
    browser.element('#a11y-search-input').type('Юmoney').press_enter()
    browser.element('[data-qa="bloko-modal-close"]').click()
    browser.element('[data-hh-tab-id="employersList"]').click()
    browser.element('[data-qa="employers-list-company-list"]').should(have.text('ЮMoney'))




'''
def test_should_have_resume():
    browser.open('/')
    browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
    browser.element('[data-qa="bloko-modal-close"]').click()
    browser.element('[data-hh-tab-id="resumeSearch"]').click()
    browser.element('[data-qa="serp-item__title"]').click()
    '''
    #browser.all(не знаю за что зацепиться).should(have.text('Специалист'))


# def test_should_have_job():
#     browser.open('/')
#     browser.element('#a11y-search-input').type('Python').press_enter()
#     browser.element('[data-qa="bloko-modal-close"]').click()
#     browser.element('[name=part_time][value=start_after_sixteen]+span').click()
#     browser.execute_script('window.scrollTo(0, 1000)')
#     time.sleep(3)
#     browser.element('[name=salary][value="50000"]+span').click()
#     browser.execute_script('window.scrollTo(0, 3000)')
#     browser.element('[class=bloko-checkbox__input][value="124"]+span').click()
#     browser.element('[name=education][value="not_required_or_not_specified"]+span').click()
#     time.sleep(3)
#     browser.execute_script('window.scrollTo(5000, 0)')
#     browser.all('[class="serp-item__title-link serp-item__title"] :before').should(have.text('Преподаватель курсов - Тестировщик ПО (Автоматизированного тестирования на Java) (QA Engineer)'))


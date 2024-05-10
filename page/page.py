import time
from selene import have
from selene.support.shared import browser


class Page:

    def open(self):
        browser.open('https://hh.ru/?customDomain=1')
        return self

    def fill_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()
        return self

    def search_company(self):
        browser.element('#a11y-search-input').type('Юmoney').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[href="/employer/655542"]').click()
        return self

    def search_resume(self):
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="serp-item__title"]').click()
        return self

    def search_job(self):
        browser.element('#a11y-search-input').type('Python').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[name=part_time][value=start_after_sixteen]+span').click()
        browser.execute_script('window.scrollTo(0, 1000)')
        time.sleep(3)
        browser.element('[name=salary][value="50000"]+span').click()
        browser.execute_script('window.scrollTo(0, 4400)')
        browser.element('[class=bloko-checkbox__input][value="124"]+span').click()
        browser.element('[name=education][value="not_required_or_not_specified"]+span').click()
        return self

    def should_have_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()
        browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))

    def should_have_company(self):
        browser.element('#a11y-search-input').type('Юmoney').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[data-qa="employers-list-company-list"]').should(have.text('ЮMoney'))
        return self

    '''
    def test_should_have_resume():
        browser.open('/')
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="serp-item__title"]').click()
        
    # browser.all(не знаю за что зацепиться).should(have.text('Специалист'))

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
    '''

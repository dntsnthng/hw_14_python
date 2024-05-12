from selene import have, command
from selene import browser, have


class MainPage:

    def open(self):
        browser.open('/')

    def fill_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()

    def search_company(self):
        browser.element('#a11y-search-input').type('Юmoney').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[href="/employer/655542"]').click()

    def fill_resume(self):
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="serp-item__title"]').click()

    def search_job(self):
        browser.element('#a11y-search-input').type('Python').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[name=part_time][value=start_after_sixteen]+span').click()
        browser.element('[name=salary][value="55000"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[class=bloko-checkbox__input][value="124"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[name=education][value="not_required_or_not_specified"]+span').click()

    def should_have_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()
        browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))

    def should_have_company(self):
        browser.element('#a11y-search-input').type('Юmoney').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[data-qa="employers-list-company-list"]').should(have.text('ЮMoney'))

    def select_city(self):
        self.open()
        self.fill_city()

    def check_city(self):
        self.open()
        self.should_have_city()

    def find_company(self):
        self.open()
        self.search_company()

    def check_company(self):
        self.open()
        self.should_have_company()

    def search_resume(self):
        self.open()
        self.fill_resume()

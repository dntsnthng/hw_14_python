import allure
from selene import command
from selene import browser, have


@allure.tag("WEB")
class MainPage:
    @allure.step('Открытие страницы')
    def open(self):
        browser.open('/')

    @allure.step('Выбор города')
    def fill_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()


    def search_company(self):
        browser.element('#a11y-search-input').type('Qiwi').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[href="/employer/3125"]').click()


    def fill_resume(self):
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="serp-item__title"]').click()


    def fill_job(self):
        browser.element('#a11y-search-input').type('Python').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[name=part_time][value=start_after_sixteen]+span').click()
        browser.element('[name=salary][value="55000"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[class=bloko-checkbox__input][value="124"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[name=education][value="not_required_or_not_specified"]+span').click()


    def should_have_city(self):
        browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))

    @allure.title('Проверка информации')
    def should_have_company(self):
        browser.element('.g-user-content').should(have.text('QIWI'))

    def should_have_job(self):
        pass


    def should_have_resume(self):
        pass

    @allure.step('Выбор города')
    def select_city(self):
        self.open()
        self.fill_city()

    @allure.step('Проверка города')
    def check_city(self):
        self.should_have_city()

    def find_company(self):
        self.open()
        self.search_company()

    def check_company(self):
        self.should_have_company()

    def search_resume(self):
        self.open()
        self.fill_resume()

    def check_resume(self):
        self.should_have_resume()

    def search_job(self):
        self.open()
        self.fill_job()
    def check_job(self):
        self.should_have_job()

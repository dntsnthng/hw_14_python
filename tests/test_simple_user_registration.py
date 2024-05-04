from demoqa_tests.data.users import user
from demoqa_tests.model.pages.registration_page import RegistrationPage
import allure


@allure.tag('web')
@allure.title('Successful fill form')
def test_registers_user():
    registration_page = RegistrationPage()

    with allure.step('Open registration page'):
        registration_page.open()

    with allure.step('Fill in user data'):
        registration_page.register(user)

    with allure.step('Checking user data'):
        registration_page.should_have_registered(user)
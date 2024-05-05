from playwright.sync_api import Page, expect
from time import sleep


def test_by_role(page: Page):
    sleep(1)
    page.goto('https://the-internet.herokuapp.com')
    page.get_by_role('link', name="Form Authentication").click()
    sleep(1)

    # почему username = page.get_by_role('combobox', name='username') не работает?
    # в документации говорится:
    # input type=text, search, tel, url, email, or with a missing or invalid type, WITH a list attribute - role=combobox
    # разве name и id не относятся к списку атрибутов? <input type="text" name="username" id="username">
    username = page.get_by_role('textbox', name='username')
    username.type('random_user_name', delay=100)
    sleep(1)

    password = page.get_by_role('textbox', name='password')
    password.fill('random_password')

    submit_button = page.get_by_role('button')
    submit_button.click()
    sleep(1)


def test_26_part_2(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    # demoqa.com не грузится - TimeoutError

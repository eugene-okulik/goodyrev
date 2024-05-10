from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com')
    page.get_by_role('link', name="Form Authentication").click()

    # почему username = page.get_by_role('combobox', name='username') не работает?
    # в документации говорится:
    # input type=text, search, tel, url, email, or with a missing or invalid type, WITH a list attribute - role=combobox
    # разве name и id не относятся к списку атрибутов? <input type="text" name="username" id="username">
    username = page.get_by_role('textbox', name='username')
    username.type('random_user_name', delay=100)

    password = page.get_by_role('textbox', name='password')
    password.fill('random_password')

    submit_button = page.get_by_role('button')
    submit_button.click()


def test_26_part_2(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://demoqa.com/automation-practice-form', wait_until='domcontentloaded')

    first_name = page.locator('#firstName')
    first_name.type('Ivan', delay=50)

    last_name = page.locator('#lastName')
    last_name.fill('Gudyrev')

    email = page.get_by_placeholder('name@example.com')
    email.fill('example@gmail.com')

    gender = page.locator('label[for="gender-radio-1"]')
    gender.click()

    mobile = page.get_by_role('textbox', name='Mobile Number')
    mobile.fill('0123456789')

    page.locator('#dateOfBirthInput').click()
    page.select_option('.react-datepicker__month-select', '8')
    page.select_option('.react-datepicker__year-select', '1987')
    page.get_by_label("Choose Sunday, September 13th,").click()

    subjects = page.locator(".subjects-auto-complete__value-container")
    subjects.click()
    subjects.type("com", delay=30)
    page.get_by_text("Computer Science", exact=True).click()
    subjects.type("en", delay=30)
    page.get_by_text("English", exact=True).click()

    sport = page.locator("label[for=hobbies-checkbox-1]")
    reading = page.locator("label[for=hobbies-checkbox-2]")
    sport.click()
    reading.check()

    current_address = page.locator("#currentAddress")
    current_address.type("Moscow", delay=30)

    state = page.locator("#state .css-1wa3eu0-placeholder")
    state.click()
    page.get_by_text("NCR", exact=True).click()

    city = page.locator("#city .css-1wa3eu0-placeholder")
    city.click()
    page.get_by_text("Delhi", exact=True).click()

    submit = page.get_by_role('button', name='Submit')
    submit.click()

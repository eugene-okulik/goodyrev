from playwright.sync_api import Page, BrowserContext, expect


'''
Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/alert/confirm,
кликает на кнопку, чтобы появился алерт, жмет Ok и проверяет, что на страние в секции "You selected" написано "Ok"
'''
def test_27_part1_alert(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.on('dialog', lambda alert: alert.accept())

    page.goto('https://www.qa-practice.com/elements/alert/confirm', wait_until='domcontentloaded')
    
    click = page.get_by_role('link', name='Click')
    click.click()

    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')


'''
Напишите тест, который зайдет на страницу https://www.qa-practice.com/elements/new_tab/button,
нажмет на кнопку Click, в открывшемся табе проверит,
что в результате написано "I am a new page in a new tab" и проверит, что на изначальной вкладке кнопка Click - активна (enabled)
'''
def test_27_part2_tabs(page: Page, context: BrowserContext):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://www.qa-practice.com/elements/new_tab/button', wait_until='domcontentloaded')
    
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')

    expect(result).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()


'''
Напишите тест, который зайдет на страницу https://demoqa.com/dynamic-properties,
нажмет на кнопку Color change только после того как она станет красной.
'''
def test_27_part3_waits(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://demoqa.com/dynamic-properties', wait_until='domcontentloaded')

    changing_button = page.locator('#colorChange')
    # (HEX #dc3545 == rgb(220,53,69))
    expect(changing_button).to_have_css('color', 'rgb(220, 53, 69)', timeout=20000)
    changing_button.click()

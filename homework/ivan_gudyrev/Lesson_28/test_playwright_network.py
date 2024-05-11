'''
Homework_28
'''
import re
import json
from playwright.sync_api import Page, Route, expect


def test_28(page: Page):
    '''
    test checks the interception of the http response and the replacement of the conten
    '''
    page.set_viewport_size({'width': 1920, 'height': 1080})
    new_name = 'яблокофон 15 про'

    def handle_route(route: Route):
        response = route.fetch()
        response_body = response.json()
        response_body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_name
        response_body = json.dumps(response_body)
        route.fulfill(body=response_body)

    page.route(re.compile('digital-mat'), handle_route)

    page.goto("https://www.apple.com/shop/buy-iphone")
    page.get_by_role("heading", name="iPhone 15 Pro & iPhone 15 Pro").click()

    product_name = page.locator('#rf-digitalmat-overlay-label-0').nth(0)
    expect(product_name).to_have_text(new_name)

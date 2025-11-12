import re
from playwright.sync_api import expect

def test_price_under_80quid(page):
    page.goto("https://www.argos.co.uk/product/2926175")
     
    expect(page).to_have_title(re.compile("Casio"))
    
    reject_button = page.locator("#onetrust-reject-all-handler")
    expect(reject_button).to_be_visible()
    reject_button.click()

    page.locator("#onetrust-reject-all-handler").click()
    price_element = page.locator("li[data-test='product-price-primary'] > h2")
    expect(price_element).to_be_visible()

    price = float(price_element.text_content().strip().strip("£").replace(",", ""))

    full_price = 99.99
    expected_price = 85.99
    assert price < full_price, f"Expected to be less than {99.99}"
    assert price == expected_price, f"Expected {expected_price}, got {price}"

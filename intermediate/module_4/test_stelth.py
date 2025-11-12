def test_stealth_headless(page):
    page.goto("https://www.argos.co.uk/product/2926175")
    title = page.title()
    print("Page title:", title)

    assert "Casio" in title

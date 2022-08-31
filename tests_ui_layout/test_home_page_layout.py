import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage


def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    hom_page = HomePage(page)
    expect(hom_page.celebrate_header).to_be_visible()
    expect(hom_page.celebrate_header).to_be_visible()


@pytest.mark.skip(reason="not ready")
def test_about_us_section_verbiage_2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    hom_page = HomePage(page)
    expect(hom_page.celebrate_header).to_be_visible()
    expect(hom_page.celebrate_header).to_be_visible()


@pytest.mark.xfail(reason="should be visible")
def test_about_us_section_verbiage_3(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    hom_page = HomePage(page)
    expect(hom_page.celebrate_header).to_be_visible()
    expect(hom_page.celebrate_header).to_be_visible()


@pytest.mark.regression
def test_about_us_section_verbiage_4(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    hom_page = HomePage(page)
    expect(hom_page.celebrate_header).to_be_visible()
    expect(hom_page.celebrate_header).to_be_visible()
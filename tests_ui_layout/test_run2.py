import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    # page.click("button:has-text('Log In')", timeout=5000)
    # page.click("text=Log In") # if we have text in single quotes then playwright will treat it as exact match
    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid='signUp.switchToSignUp']"):
            page.click("'Log In'")
        else:
            login_issue = False
        time.sleep(0.1)
    page.click("[data-testid='signUp.switchToSignUp']", timeout=2000)
    page.click("[data-testid='siteMembersDialogLayout'] [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill("input:below(:text('Email'))", "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] input[type='email']", "Tab")
    page.fill("input[type='password']", "test123")
    page.click("[data-testid='submit'] [data-testid='buttonElement']")
    page.wait_for_selector("[aria-label='symon.storozhenko account menu']")
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")
    # expect(page.locator("text=My Orders")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

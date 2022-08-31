from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Act - When/And
    # Click button:has-text("Log In")
    page.locator("button:has-text(\"Log Ins\")").click()
    # Click [data-testid="signUp\.switchToSignUp"]
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    # Click [data-testid="siteMembersDialogLayout"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"siteMembersDialogLayout\"] [data-testid=\"buttonElement\"]").click()
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("symon.storozhenko@gmail.com")
    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("test123")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    # Click [aria-label="symon\.storozhenko account menu"]
    page.locator("[aria-label=\"symon\\.storozhenko account menu\"]").click()
    # Click text=My Orders
    page.locator("text=My Orders").click()

    # Assert - Then
    assert page.is_visible("text=My Orders")
    page.wait_for_url("https://symonstorozhenko.wixsite.com/website-1/account/my-orders")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

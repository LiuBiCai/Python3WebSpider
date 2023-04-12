from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to about:blank
    page.goto("about:blank")

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.locator("input[name=\"wd\"]").click()

    # Click span:has-text("春天里的中国外交")
    with page.expect_popup() as popup_info:
        page.locator("span:has-text(\"春天里的中国外交\")").click()
    page1 = popup_info.value

    # Click [aria-label="标题：春天里的中国外交"] >> text=春天里的中国外交
    with page1.expect_popup() as popup_info:
        page1.locator("[aria-label=\"标题：春天里的中国外交\"] >> text=春天里的中国外交").click()
    page2 = popup_info.value
    page1.wait_for_url("https://baijiahao.baidu.com/s?id=1762701346167167344")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

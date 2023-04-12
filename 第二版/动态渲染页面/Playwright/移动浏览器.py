from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    iphone_12_por_max=p.devices["iPhone 12 Pro Max"]
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(
        **iphone_12_por_max,
        locale="zh-CN",
    )
    page=context.new_page()
    page.goto("https://www.whatismybrowser.com/")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="iphone-12-pro-max.png")
    browser.close()
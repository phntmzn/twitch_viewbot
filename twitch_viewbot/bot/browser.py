from playwright.async_api import async_playwright
import asyncio
import random

class BrowserViewer:
    def __init__(self, url, proxy=None, user_agent=None):
        self.url = url
        self.proxy = proxy
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    async def launch(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, proxy={"server": self.proxy} if self.proxy else None)
            context = await browser.new_context(user_agent=self.user_agent)
            page = await context.new_page()
            await page.goto(self.url, timeout=60000)
            await asyncio.sleep(random.uniform(30, 120))  # Simulate viewing
            await browser.close()

import asyncio
from bot.client import TwitchClient
from bot.browser import BrowserViewer
from bot.identity import generate_identity

class ViewBotManager:
    def __init__(self, channel, mode="client", num_bots=10, proxy_list=None):
        self.channel = channel
        self.mode = mode
        self.num_bots = num_bots
        self.proxy_list = proxy_list or []

    async def run_bot(self, index):
        identity = generate_identity()
        proxy = self.proxy_list[index % len(self.proxy_list)] if self.proxy_list else None

        if self.mode == "client":
            client = TwitchClient(self.channel, proxy=proxy)
            await client.connect()
        elif self.mode == "browser":
            browser = BrowserViewer(f"https://twitch.tv/{self.channel}", proxy=proxy, user_agent=identity["user_agent"])
            await browser.launch()

    async def start(self):
        tasks = [self.run_bot(i) for i in range(self.num_bots)]
        await asyncio.gather(*tasks)

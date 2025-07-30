import asyncio
from bot.client import TwitchClient
from bot.browser import BrowserViewer
from bot.identity import generate_identity

class Worker:
    def __init__(self, index, channel, mode="client", proxy=None):
        self.index = index
        self.channel = channel
        self.mode = mode
        self.proxy = proxy
        self.identity = generate_identity()

    async def start(self):
        if self.mode == "client":
            client = TwitchClient(self.channel, proxy=self.proxy)
            print(f"[Worker {self.index}] Connecting via IRC...")
            await client.connect()
        elif self.mode == "browser":
            browser = BrowserViewer(
                url=f"https://twitch.tv/{self.channel}",
                proxy=self.proxy,
                user_agent=self.identity["user_agent"]
            )
            print(f"[Worker {self.index}] Launching browser...")
            await browser.launch()

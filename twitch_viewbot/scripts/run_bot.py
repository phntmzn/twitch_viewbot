import asyncio
from core.config import TWITCH_CHANNEL, NUM_BOTS, MODE, load_proxies
from bot.manager import ViewBotManager

async def main():
    proxies = load_proxies()
    manager = ViewBotManager(channel=TWITCH_CHANNEL, mode=MODE, num_bots=NUM_BOTS, proxy_list=proxies)
    await manager.start()

if __name__ == "__main__":
    asyncio.run(main())

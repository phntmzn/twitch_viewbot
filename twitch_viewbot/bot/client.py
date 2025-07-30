import aiohttp
import asyncio
import random

class TwitchClient:
    def __init__(self, channel_name, client_id=None, oauth_token=None, proxy=None):
        self.channel = channel_name
        self.client_id = client_id
        self.oauth_token = oauth_token
        self.proxy = proxy
        self.ws_url = "wss://irc-ws.chat.twitch.tv:443"

    async def connect(self):
        session_args = {}
        if self.proxy:
            session_args['proxy'] = self.proxy

        async with aiohttp.ClientSession(**session_args) as session:
            async with session.ws_connect(self.ws_url) as ws:
                await ws.send_str(f"PASS oauth:{self.oauth_token or 'guest'}")
                await ws.send_str(f"NICK justinfan{random.randint(10000, 99999)}")
                await ws.send_str(f"JOIN #{self.channel}")
                print(f"Connected to {self.channel}")

                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        print(f"[{self.channel}] {msg.data.strip()}")
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        break

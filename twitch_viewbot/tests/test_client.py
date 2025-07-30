import asyncio
import pytest
from bot.client import TwitchClient

@pytest.mark.asyncio
async def test_twitch_client_connection(monkeypatch):
    messages = []

    class MockWebSocket:
        async def send_str(self, data):
            messages.append(data)

        async def __aiter__(self):
            yield type("Msg", (), {"type": 1, "data": "PING :tmi.twitch.tv"})()

        async def close(self):
            pass

    class MockSession:
        async def __aenter__(self): return self
        async def __aexit__(self, *a): pass
        async def ws_connect(self, url): return MockWebSocket()

    monkeypatch.setattr("aiohttp.ClientSession", lambda **kwargs: MockSession())

    client = TwitchClient(channel_name="somechannel", oauth_token="test")
    await client.connect()

    assert any("JOIN #somechannel" in msg for msg in messages)

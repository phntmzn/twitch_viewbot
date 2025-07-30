import pytest
import asyncio
from bot.manager import ViewBotManager

class DummyManager(ViewBotManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launched = []

    async def run_bot(self, index):
        self.launched.append(index)

@pytest.mark.asyncio
async def test_manager_starts_correct_number_of_bots():
    mgr = DummyManager(channel="testchannel", mode="client", num_bots=5)
    await mgr.start()
    assert len(mgr.launched) == 5

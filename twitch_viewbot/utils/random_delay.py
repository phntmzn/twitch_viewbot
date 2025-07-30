import asyncio
import random

async def sleep_jitter(min_delay=2.0, max_delay=5.0):
    delay = random.uniform(min_delay, max_delay)
    await asyncio.sleep(delay)
    return delay

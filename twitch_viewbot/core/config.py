import os
from dotenv import load_dotenv

load_dotenv()

TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL", "some_channel")
NUM_BOTS = int(os.getenv("NUM_BOTS", 10))
MODE = os.getenv("MODE", "client")  # "client" or "browser"
PROXY_FILE = os.getenv("PROXY_FILE", "proxies.txt")

def load_proxies():
    try:
        with open(PROXY_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

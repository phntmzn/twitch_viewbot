import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0"
]

SCREEN_RESOLUTIONS = [
    (1920, 1080),
    (1366, 768),
    (1600, 900),
    (1440, 900)
]

def generate_identity():
    ua = random.choice(USER_AGENTS)
    width, height = random.choice(SCREEN_RESOLUTIONS)
    nickname = f"viewer{random.randint(100000, 999999)}"
    return {
        "user_agent": ua,
        "screen_width": width,
        "screen_height": height,
        "nickname": nickname
    }

import random

class ProxyPool:
    def __init__(self, proxy_list):
        self.proxies = proxy_list.copy()
        random.shuffle(self.proxies)

    def get_proxy(self):
        if not self.proxies:
            return None
        return random.choice(self.proxies)

    def rotate(self):
        if not self.proxies:
            return None
        proxy = self.proxies.pop(0)
        self.proxies.append(proxy)
        return proxy

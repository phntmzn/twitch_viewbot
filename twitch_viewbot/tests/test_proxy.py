from core.proxy import ProxyPool

def test_proxy_pool_rotation():
    proxies = ["proxy1", "proxy2", "proxy3"]
    pool = ProxyPool(proxies.copy())

    seen = set()
    for _ in range(6):
        proxy = pool.rotate()
        assert proxy in proxies
        seen.add(proxy)

    assert seen == set(proxies)

def test_proxy_pool_get_proxy():
    proxies = ["proxyA", "proxyB"]
    pool = ProxyPool(proxies)

    proxy = pool.get_proxy()
    assert proxy in proxies

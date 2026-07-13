import threading
import time


class ExpiringCache:
    def __init__(self):
        self._items = {}
        self._lock = threading.Lock()

    def put(self, key, value, ttl_seconds):
        expires_at = time.monotonic() + ttl_seconds
        with self._lock:
            self._items[key] = (value, expires_at)

    def get(self, key):
        item = self._items.get(key)
        if item is None:
            return None
        value, expires_at = item
        if expires_at <= time.monotonic():
            del self._items[key]
            return None
        return value

    def get_or_compute(self, key, ttl_seconds, compute):
        cached = self.get(key)
        if cached is not None:
            return cached
        value = compute()
        self.put(key, value, ttl_seconds)
        return value

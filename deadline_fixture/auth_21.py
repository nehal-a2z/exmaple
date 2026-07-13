import hashlib
import hmac
import time


class TokenStore:
    def __init__(self):
        self._tokens = {}

    def issue(self, user_id, secret):
        issued_at = int(time.time())
        payload = f"{user_id}:{issued_at}"
        signature = hmac.new(
            secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        token = f"{payload}:{signature}"
        self._tokens[token] = user_id
        return token

    def validate(self, token, secret, max_age_seconds=3600):
        try:
            user_id, issued_at, signature = token.split(":", 2)
            payload = f"{user_id}:{issued_at}"
            expected = hmac.new(
                secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
            ).hexdigest()
            if signature != expected:
                return None
            if int(time.time()) - int(issued_at) > max_age_seconds:
                return None
            return self._tokens.get(token)
        except (TypeError, ValueError):
            return None

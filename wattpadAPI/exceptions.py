
class WattpadAPIError(Exception):
    pass

class RateLimitError(WattpadAPIError):
    pass

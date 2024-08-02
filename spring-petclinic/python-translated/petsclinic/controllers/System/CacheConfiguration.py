from django.core.cache import cache
from django.conf import settings

class CacheConfiguration:
    def __init__(self):
        # Setting up cache configuration
        self.cache_backend = settings.CACHES['default']['BACKEND']
        self.cache_timeout = settings.CACHES['default']['TIMEOUT']

    def set_cache(self, key, value):
        cache.set(key, value, self.cache_timeout)

    def get_cache(self, key):
        return cache.get(key)

    def delete_cache(self, key):
        cache.delete(key)

# Example usage:
# cache_config = CacheConfiguration()
# cache_config.set_cache('vets', some_value)
# value = cache_config.get_cache('vets')

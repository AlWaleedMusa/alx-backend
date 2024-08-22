#!/usr/bin/python3
"""
Basic Cache implementation Class.
This module provides a simple caching mechanism using a dictionary.
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.

    This class provides methods to add and retrieve items from a cache.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The item stored in the cache, or None if the key does not exist.
        """
        return self.cache_data.get(key, None)
    
#!/usr/bin/python3
"""
FIFO Cache Replacement Implementation Class.

This module provides a FIFO (First In, First Out) caching mechanism.
"""
from threading import RLock

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.

    This class provides methods to add and retrieve
    items from a cache using FIFO replacement policy.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance.
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to be stored in the cache.
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print("DISCARD: {}".format(keyOut))

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The item stored in the cache,
            or None if the key does not exist.
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """
        Balance the cache by removing the oldest item if the cache is full.

        Args:
            keyIn (str): The key of the new item being added.

        Returns:
            str: The key of the item that was removed,
            or None if no item was removed.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__keys:
                keysLength = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
                self.__keys.insert(keysLength, keyIn)
        return keyOut

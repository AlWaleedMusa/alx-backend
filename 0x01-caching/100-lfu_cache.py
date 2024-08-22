#!/usr/bin/python3
"""
LFU Cache Replacement Implementation Class.

This module provides an LFU (Least Frequently Used) caching mechanism.
"""
from threading import RLock

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.

    This class provides methods to add and retrieve
    items from a cache using LFU replacement policy.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.__stats = {}
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
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """
        Balance the cache by removing the least
        frequently used item if the cache is full.

        Args:
            keyIn (str): The key of the new item being added.

        Returns:
            str: The key of the item that was removed,
            or None if no item was removed.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut

#!/usr/bin/env python3
"""
get_page function to server class
"""
import csv
from typing import Tuple, List


class Server:
    """Server class"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculates start index and ending index to the range of
        indexes
        """
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex

        return nextPageStartIndex - page_size, nextPageStartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get data for a given page number.

        Args:
            page (int): Page number.
            page_size (int): Number of items in a page.

        Returns:
            List[List]: A list of list(row) if inputs are within range.
            [] : An empty list if page and page_size are out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]

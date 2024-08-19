#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List, Any


class Server:
    """Server class to paginate a database of names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset =\
                {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
        self, start_index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        The goal here is that if between two queries,
        certain rows are removed from the dataset, the user
        does not miss items from dataset when changing page.

        Args:
            start_index (int): start index of the current page
            page_size (int): size of items required in
            current page

        Returns:
            Dict[str, Any]: a dict of the following:
                * index, next_index, page_size, data
        """
        dataset = self.indexed_dataset()
        start_index = 0 if start_index is None else start_index
        sorted_keys = sorted(dataset.keys())

        assert 0 <= start_index <= sorted_keys[-1]

        selected_keys = []
        for key in sorted_keys:
            if key >= start_index and len(selected_keys) < page_size:
                selected_keys.append(key)

        data = [dataset[key] for key in selected_keys]
        next_index = selected_keys[-1] + 1\
            if len(selected_keys) == page_size else None

        return {
            "index": start_index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }

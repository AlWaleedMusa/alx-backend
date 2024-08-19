#!/usr/bin/env python3

"""
a function `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and ending index to the range of
    indexes
    Args:
        page (int): current page
        page_size (int): items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex

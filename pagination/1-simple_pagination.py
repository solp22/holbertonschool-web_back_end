#!/usr/bin/env python3
"""simple_pagination module"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return start index and end index"""
    last_index = page * page_size
    first_index = last_index - page_size
    return (first_index, last_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        data = self.dataset()
        return data[range[0]:range[1]]

#!/usr/bin/env python3
"""simple_pagination module"""
import csv
import math
from typing import List, Dict


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
        """return the appropriate page of the dataset """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        data = self.dataset()
        return data[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns hypermedia pagination"""
        total_pages = math.ciel(len(self.dataset())) / page_size
        prev_page = 0
        next_page = 0

        if page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page - 1 >= 1:
            prev_page = page - 1
        else:
            prev_page = None

        hyper_dict = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return hyper_dict

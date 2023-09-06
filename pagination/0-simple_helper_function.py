#!/usr/bin/env python3
"""simple_helper_function module"""


def index_range(page, page_size):
    """return start index and end index"""
    last_index = page * page_size
    first_index = last_index - page
    return (first_index, last_index)

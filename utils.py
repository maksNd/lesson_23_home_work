# PATH = 'apache_logs.txt'
from typing import Generator, Union, List, Any, Iterable
import re


def open_log(path: str) -> Generator:
    with open(f'data/{path}') as file:
        while True:
            try:
                row = next(file)
            except StopIteration:
                break
            yield row


# filter
def filter_query(data: Iterable, value: str) -> filter:
    return filter(lambda row: value in row, data)


# map
def map_query(data: Iterable, value: str) -> map:
    return map(lambda row: row.split(' ')[int(value)], data)


# unique
def unique_query(data: Iterable, *args: Any, **kwargs: Any) -> set:
    return set(data)


# sort
def sort_query(data: Iterable, value: str) -> List:
    return sorted(data, reverse=value == 'desk')


# limit
def limit_query(data: Iterable, value: str) -> List:
    return list(data)[:int(value)]


# re
def regex_query(data: Iterable, value: str) -> List:
    return re.findall(value, '\n'.join(data))

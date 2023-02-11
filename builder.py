from typing import List, Generator, Union, Callable, Any, Dict, Iterable

from utils import filter_query, map_query, sort_query, unique_query, limit_query, regex_query

CMD_TO_QUERY: Dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'limit': limit_query,
    'regex': regex_query
}


def query_builder(cmd: str, value: str, data: Union[Iterable]) -> Union[Iterable]:
    foo: Callable = CMD_TO_QUERY[cmd]
    return foo(data, value)


print(type(map_query))

from typing import List, Generator, Union

from utils import filter_query, map_query, sort_query, unique_query, limit_query, regex_query

CMD_TO_QUERY = {
    'filter': filter_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'limit': limit_query,
    'regex': regex_query
}


def query_builder(cmd: str, value: str, data: Union[Generator, List, map, set, filter]) -> Union[
    Generator, List, map, set, filter]:
    # foo: function = CMD_TO_QUERY[cmd]
    foo = CMD_TO_QUERY[cmd]
    return foo(data, value)


print(type(map_query))

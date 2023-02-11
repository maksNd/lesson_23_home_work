from utils import filter_query, map_query, sort_query, unique_query, limit_query, regex_query

CMD_TO_QUERY = {
    'filter': filter_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'limit': limit_query,
    'regex': regex_query
}


def query_builder(cmd, value, data):
    result = CMD_TO_QUERY[cmd](data, value)
    return result

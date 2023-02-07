from utils import filter_query, map_query, sort_query, unique_query, limit_query, open_log

CMD_TO_QUERY = {
    'filter': filter_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'limit': limit_query
}


def query_builder(cmd, value, data=None):
    if data is None:
        prepared_data = open_log()
    else:
        prepared_data = data

    result = CMD_TO_QUERY[cmd](prepared_data, value)
    return result
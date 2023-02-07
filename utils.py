PATH = 'data/apache_logs.txt'


def open_log(path=PATH):
    with open(path) as file:
        while True:
            try:
                row = next(file)
            except StopIteration:
                break
            yield row


# filter
def filter_query(data, value):
    return filter(lambda row: value in row, data)


# map
def map_query(data, value):
    return map(lambda row: row.split(' ')[int(value)], data)


# unique
def unique_query(data, *args, **kwargs):
    return set(data)


# sort
def sort_query(data, value):
    return sorted(data, reverse=value == 'desk')


# limit
def limit_query(data, value):
    return list(data)[:int(value)]

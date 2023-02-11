from flask import Flask, request

from class_query import Query, QuerySchema
from builder import query_builder
from utils import open_log

app = Flask(__name__)


@app.post('/perform_query')
def query_page():
    query: Query = QuerySchema().load(request.get_json())

    if None in (query.cmd1, query.cmd2, query.value1, query.value2):
        return 'Query params is not enough', 404

    try:
        data = list(open_log(query.file_name))
    except FileNotFoundError:
        return 'File not found', 404

    result = query_builder(query.cmd1, query.value1, data)
    result = query_builder(query.cmd2, query.value2, result)

    return '\n'.join(list(result)), 200


if __name__ == '__main__':
    app.run()

from flask import Flask, request

from builder import query_builder

app = Flask(__name__)


@app.post('/perform_query')
def query_page():
    query = request.get_json()
    cmd1 = query.get('cmd1')
    value1 = query.get('value1')
    cmd2 = query.get('cmd2')
    value2 = query.get('value2')

    if None in (cmd1, cmd2, value1, value2):
        return 'Query params is not enough', 404
    try:
        result = query_builder(cmd1, value1)
        result = query_builder(cmd2, value2, result)
    except FileNotFoundError:
        return 'File not found', 404

    return '\n'.join(list(result)), 200


if __name__ == '__main__':
    app.run()

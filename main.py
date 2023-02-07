from flask import Flask, request

from builder import query_builder

app = Flask(__name__)


@app.get('/')
def query_page():
    cmd1 = request.args.get('cmd1')
    value1 = request.args.get('value1')
    cmd2 = request.args.get('cmd2')
    value2 = request.args.get('value2')

    try:
        result = query_builder(cmd1, value1)
        result = query_builder(cmd2, value2, result)
    except FileNotFoundError:
        return 'File not found', 404
    except KeyError:
        return 'Query params is not enough', 404

    return ''.join(list(result)), 200


app.run()

'''
Basic flask API
'''
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def get_api():
    '''
    returns jsonified data, and a 200 status code
    '''
    data = {
        'data':
        [
            {
                'name': 'John Doe',
                'age': 30,
                'job': 'Software Engineer'
            },
            {
                'name': 'Jane Doe',
                'age': 25,
                'job': 'Data Scientist'
            }
        ]
    }
    return make_response(jsonify(data), 200)

# register the app
if __name__ == '__main__':
    app.run(debug=True)

'''
Basic flask API
'''
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from database.connect import session
from database.classes import *


app = Flask(__name__)
CORS(app)


@app.route('/api/v1/artists', methods=['POST'])
def get_api():
    '''
    returns jsonified data, and a 200 status code
    '''
    body = request.get_json()
    artist_name = body.get('artist_name')
    artist_genre = body.get('artist_genre')
    fields = {
        # 'artist_id': uuid.uuid4(),
        'artist_name': artist_name,
        'artist_genre': artist_genre
    }

    with session() as sesh:
        sesh.add(Artist(**fields))
        sesh.commit()

    return make_response(jsonify(fields), 200)


@app.route('/api/v1/artists', methods=['GET'])
def get_all_artists():
    '''
    returns jsonified data, and a 200 status code
    '''
    with session() as sesh:
        artists = sesh.query(Artist).all()
        print('artists: ', artists)

    return make_response(jsonify([artist.artist_name for artist in artists]), 200)


# register the app
if __name__ == '__main__':
    app.run(debug=True)

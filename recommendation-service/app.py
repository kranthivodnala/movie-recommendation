# recommendation-service/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "genre": "Drama"},
    {"id": 2, "title": "The Godfather", "genre": "Crime"},
    {"id": 3, "title": "Pulp Fiction", "genre": "Crime"},
    {"id": 4, "title": "12 Angry Men", "genre": "Drama"},
    {"id": 5, "title": "The Dark Knight", "genre": "Action"},
]

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    genre = request.args.get('genre')
    if genre:
        recommended_movies = [m for m in movies if m['genre'] == genre]
        return jsonify(recommended_movies)
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

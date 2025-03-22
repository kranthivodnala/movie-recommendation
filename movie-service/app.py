# movie-service/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "genre": "Drama"},
    {"id": 2, "title": "The Godfather", "genre": "Crime"},
    {"id": 3, "title": "Pulp Fiction", "genre": "Crime"},
]

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return jsonify(movie)
    return jsonify({"message": "Movie not found"}), 404

@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    new_movie = {
        "id": len(movies) + 1,
        "title": data['title'],
        "genre": data['genre']
    }
    movies.append(new_movie)
    return jsonify(new_movie), 201

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        data = request.get_json()
        movie['title'] = data.get('title', movie['title'])
        movie['genre'] = data.get('genre', movie['genre'])
        return jsonify(movie)
    return jsonify({"message": "Movie not found"}), 404

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({"message": "Movie deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify, url_for
import requests

app = Flask(__name__)

MOVIE_SERVICE_URL = 'http://movie-service:5000/movies'  # Adjust if needed
RECOMMENDATION_SERVICE_URL = 'http://recommendation-service:5001/recommendations'  # Adjust if needed

@app.route('/')
def index():
    movies = requests.get(MOVIE_SERVICE_URL).json()
    return render_template('index.html', movies=movies)

@app.route('/create', methods=['POST'])
def create_movie():
    title = request.form['title']
    genre = request.form['genre']
    requests.post(MOVIE_SERVICE_URL, json={'title': title, 'genre': genre})
    return index()

@app.route('/delete/<int:movie_id>')
def delete_movie(movie_id):
    requests.delete(f'{MOVIE_SERVICE_URL}/{movie_id}')
    return index()

@app.route('/update/<int:movie_id>', methods=['POST'])
def update_movie(movie_id):
    title = request.form['title']
    genre = request.form['genre']
    requests.put(f'{MOVIE_SERVICE_URL}/{movie_id}', json={'title': title, 'genre': genre})
    return index()

@app.route('/recommendations', methods=['GET'])
def recommendations():
    genre = request.args.get('genre')
    if genre:
        recommendations = requests.get(f'{RECOMMENDATION_SERVICE_URL}?genre={genre}').json()
    else:
        recommendations = requests.get(RECOMMENDATION_SERVICE_URL).json()
    return render_template('recommendations.html', recommendations=recommendations, genre=genre)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002) #port changed to 5002

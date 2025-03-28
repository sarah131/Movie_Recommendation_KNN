import pickle

import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load the saved KNN model
with open('knn_model.pkl', 'rb') as file:
    knn = pickle.load(file)

# Load the user-item matrix and movie data
user_item_matrix = pd.read_csv('user_item_matrix.csv').values
movies_df = pd.read_csv('movies.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_index = int(data.get('user_index', 0))
        
        if user_index < 0 or user_index >= user_item_matrix.shape[0]:
            return jsonify({'error': 'Invalid user index'})

        user_data = user_item_matrix[user_index].reshape(1, -1)
        distances, indices = knn.kneighbors(user_data, n_neighbors=6)

        movie_ids = indices.flatten().tolist()[1:]
        recommended_movies = []

        for movie_id in movie_ids:
            movie_name = movies_df[movies_df['movieId'] == movie_id]['title'].values
            if len(movie_name) > 0:
                recommended_movies.append(movie_name[0])

        return jsonify({'recommendations': recommended_movies})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

# Movie Recommendation System using KNN 🎥

This repository contains the implementation of a movie recommendation system using the K-Nearest Neighbors (KNN) algorithm in Python. The goal of this project is to explore different variations of KNN, including cosine, Jaccard, Euclidean, and Manhattan distance metrics, and compare their performance with Singular Value Decomposition (SVD) for movie recommendation. The MovieLens dataset is used as the primary source of movie ratings.

## Overview ✨
The KNN algorithm is a popular collaborative filtering technique used in recommendation systems. It leverages the similarity between users or items to make predictions for unrated movies. In this project, we focus on user-based collaborative filtering, where the similarity between users is measured based on their movie ratings.

## Variations of KNN 🛣️
The implementation includes variations of KNN that utilize different distance metrics to calculate similarity between users. The available options are:

- **Cosine Similarity:** Measures the cosine of the angle between two users' rating vectors.
- **Jaccard Similarity:** Computes the Jaccard coefficient, which is the size of the intersection divided by the size of the union of the rated movies by two users.
- **Euclidean Distance:** Calculates the Euclidean distance between two users' rating vectors.
- **Manhattan Distance:** Computes the Manhattan distance (also known as the L1 distance) between two users' rating vectors.

These different metrics provide flexibility in capturing user similarity, allowing for more accurate recommendations based on specific characteristics of the dataset.

## SVD Comparison
To evaluate the performance of the KNN algorithm, we compare it with Singular Value Decomposition (SVD), a matrix factorization technique commonly used in recommendation systems. SVD decomposes the rating matrix into lower-rank matrices to approximate the original matrix and make predictions. By comparing the results of KNN and SVD, we can assess the effectiveness of each approach in generating movie recommendations.

## Dataset
The MovieLens dataset is used for this project, which provides a collection of movie ratings from various users. It contains a rich set of movie attributes, such as title, genre, and user ratings. The dataset is preprocessed and provided in a suitable format for the implementation.

## Implementation Details 🛠️
- **Data Preprocessing:** Loading, cleaning, and transforming the MovieLens dataset into a user-item matrix.
- **Model Training:** Fitting the KNN model using different similarity metrics.
- **Recommendation Generation:** Predicting ratings for unseen movies and recommending top-rated movies.
- **Ranking:** Ranking recommendations based on predicted ratings.
- **Cold Start Handling:** Providing popular or diverse recommendations for new users.

## Evaluation Metrics 📊
- **RMSE (Root Mean Square Error):** Measures the difference between predicted and actual ratings.
- **Precision:** Proportion of recommended items that are relevant.
- **Recall:** Proportion of relevant items that are recommended.
- **Coverage:** Proportion of total items the system can recommend.

## Also integrated into a website design
### 🏠 **Home Page**  
![Home Page](ss.png)  

## Future Improvements 🚀
- **Hybrid Recommendation System:** Combine collaborative filtering with content-based methods.
- **Parameter Tuning:** Optimize hyperparameters like the number of neighbors and similarity metrics.
- **Enhanced Cold Start Solutions:** Use demographic or content-based data to improve new user recommendations.
- **Diverse and Serendipitous Recommendations:** Prioritize novelty and diversity in suggestions.


## Do follow for more and Refer 
For projects : [Github](https://github.com/sarah131/)

For coding skills & Problem solving : [Youtube](https://youtube.com/@theengineeringcodex?si=5o6xpI8eqK7-2fQf)

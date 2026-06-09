from django.shortcuts import render
from django.views import View
import pickle
from sklearn.metrics.pairwise import cosine_similarity



with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('finalVectors.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


class homepage(View):

   
    def get(self, request):
        return render(request, 'home.html', {
            'recommendations': [],
            'error': None
        })

  
    def post(self, request):

        movie_name = request.POST.get('movie', '').strip()

        filtered_movie = movies[
            movies['Series_Title'].str.strip().str.lower() == movie_name.lower()
        ]

        if filtered_movie.empty:
            return render(request, 'home.html', {
                'error': 'Movie not found',
                'recommendations': []
            })

        movie_index = filtered_movie.index[0]

        recommended_movies = self.get_recommendations(vectorizer[movie_index])

        return render(request, 'home.html', {
            'recommendations': recommended_movies,
            'error': None
        })

    
    def get_recommendations(self, vector):

        distances = cosine_similarity(vector, vectorizer).flatten()

        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        result = []

        for i in movie_list:
            index = i[0]

            result.append({
                "Series_Title": movies.iloc[index]["Series_Title"],
                "Poster_Link": movies.iloc[index]["Poster_Link"]
            })

        return result

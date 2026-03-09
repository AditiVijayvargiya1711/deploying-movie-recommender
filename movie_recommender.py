import pickle

titles = pickle.load(open('titles.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def recommend(movie):
    try:
        movie_index = model[model['title']==movie].index[0]
    except:
        return []
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    return [model.iloc[i[0]].title for i in movies_list]
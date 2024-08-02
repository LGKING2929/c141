from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies=movies_data[['original_title','poster_link','realease_date','runtime','weighted_rating']]

# variables to store data
liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

# method to fetch data from database
def assign_val():
  m={
    "original_title":all_movies.iloc[0,0],
    "poster_link":all_movies.iloc[0,1],
    "realease_date":all_movies.iloc[0,2],
    "duration":all_movies.loc[0,3],
    "rating":all_movies.loc[0,4]
  }
  return m

# /movies api
@app.route("/movies")
def get_movies():
  movie_data=assign_val()
  return jsonify({
    "data":movie_data,
    "status":"sucuess"
  })

# /like api
@app.route("/like")
def liked_movie():
  global all_movies
  movie_data=assign_val()
  liked_movies.append(movie_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"sucuess"
  })


# /dislike api
@app.route("/dislike")
def unliked_movie():
  global all_movies
  movie_data=assign_val()
  not_liked_movies.append(movie_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"sucuess"
  })


# /did_not_watch api
@app.route("/did_not_watch")
def did_not_watch():
  global all_movies
  movie_data=assign_val()
  did_not_watch.append(movie_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"sucuess"
  })


if __name__ == "__main__":
  app.run()
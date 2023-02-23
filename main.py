from fastapi import FastAPI, Body, requests
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
app.title = "My aplication with FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
    {
            "id":1,
            "title":"Avatar",
            "overview":"In this movie a amaizin blue people that other word try to save their land, and a human help ther",
            "year":2009,
            "rating":7.8,
            "category":"Action"
        },
    {
            "id":2,
            "title":"Titanic",
            "overview":"History of bigger ship of the word in those moment, and love history of two young lovers",
            "year":1999,
            "rating":8.8,
            "category":"Drama"
        },
    {
            "id":3,
            "title":"Iron Man",
            "overview":"Millionary man with make a super metal suit and help or word",
            "year":2010,
            "rating":6.8,
            "category":"Fiction"
        }
]

@app.get(
    path='/', 
    tags = ['Home'], 
    summary="Home of page")
def message():
    return HTMLResponse ("<h2> Hello myt Best friend, in this page there are amazin movies. </h2>")

@app.get(
    path='/movies',
    tags=['Movies'],
    summary="Show all movies")
def get_movies():
    return movies

@app.get('/movies/{id}', 
         tags=['Movies'],
         summary="Show a movie with the ID")
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return "This movie there is not in the actually list."

@app.get(
    path='/movies/',
    tags=['Movies'],
    summary="Show movie by category")
def get_movie_by_category(category: str, year: int):
    for i in movies:
        if i["category"] == category and i["year"] == year:
            return i
    return HTMLResponse ("<h2> This CATEGORY and YEAR there aren't in the actually list\n Please validate the year and category. </h2>")    

@app.post(
    path='/movies',
    tags=['Movies'],
    summary="Create a movie in the list.")
def create_movie(movie: Movie):
    movies.append(movie.dict())
    return movies

@app.put(
    path='/movies/{id}',
    tags=['Movies'],
    summary="Modifique a movie in the list")
def update_movies(id:int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return movies            
            
@app.delete(
    path='/movies/{id}',
    tags=['Movies'],
    summary="Delete a movie with the ID")
def delete_movie(id: int):
    for i in movies:
        if i['id'] == id:
            movies.remove(i)
            return movies            
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My aplication with FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id":1,
        "title":"Avatar",
        "overview":"In this movie a amaizin blue people that other word try to save their land, and a human help ther",
        "year":2009,
        "ranging":7.8,
        "category":"Action"
    },
    {
        "id":2,
        "title":"Titanic",
        "overview":"History of bigger ship of the word in those moment, and love history of two young lovers",
        "year":1999,
        "ranging":8.8,
        "category":"Drama"
    },
    {
       "id":3,
        "title":"Iron Man",
        "overview":"Millionary man with make a super metal suit and help or word",
        "year":2010,
        "ranging":6.8,
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

@app.get(
    path='/movies/{id}',
    tags=['Movies'],
    summary="Show a movie with your ID")
def get_movie(id: int):
    for i in movies:
        if i["id"] == id:
            return i
    return HTMLResponse ("<h3> This movie there is not in the actually list. </h3>")

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
def create_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), ranging:float = Body(), category:str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "ranging":ranging,
        "category":category
    })
    return movies
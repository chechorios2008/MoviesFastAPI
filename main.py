from fastapi import FastAPI, Body, requests, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI()
app.title = "My aplication with FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi pelicula", min_length=5, max_length=15)
    overview: str = Field(default="Descripción", min_length=15, max_length=50)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=4, max_length=15)
#Clase para enviar información por defesto. 
    class Config:
        schema_extra = {
            "example": {
                "id":4,
                "title":"Mi pelicula",
                "overview":"Descripción de la pelicula",
                "year":2000,
                "rating":1.1,
                "category":"Arte"
            }
        }
    
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
            "category":"Action"
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
    summary="Show all movies",
    response_model=List[Movie],
    status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200,content=movies) 

@app.get('/movies/{id}', 
    tags=['Movies'],
    summary="Show a movie with the ID",
    response_model=Movie,
    status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(status_code=200, content=item) 
    return JSONResponse(status_code=404,content="This movie there is not in the actually list.")

@app.get(
    path='/movies/',
    tags=['Movies'],
    summary="Show movie by category",
    response_model= List[Movie],
    status_code=200)
def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(status_code=200, content=data)    

@app.post(
    path='/movies',
    tags=['Movies'],
    summary="Create a movie in the list.",
    response_model=dict,
    status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.dict())
    return JSONResponse(status_code=201,content={"message":"Your movie has been REGISTERED!!!"})

@app.put(
    path='/movies/{id}',
    tags=['Movies'],
    summary="Modifique a movie in the list",
    response_model=dict,
    status_code=200)
def update_movies(id:int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(status_code=200, content={"message":"Your movie has been MODIFIED!!!"})            
            
@app.delete(
    path='/movies/{id}',
    tags=['Movies'],
    summary="Delete a movie with the ID",
    response_model=dict,
    status_code=200)
def delete_movie(id: int) -> dict:
    for i in movies:
        if i['id'] == id:
            movies.remove(i)
            return JSONResponse(status_code=200,content={"message":"Your movie has been DELETED!!!"})          
from typing import Union
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    text = "Hi! Welcome to my API.Christopher Nolan is a British-American film director, producer, and screenwriter.The Christopher Nolan API provides information for Christopher Nolan's movies."
    return text

@app.get("/movies")
def movies_list():
    movies = {
    "following", "memento", "insomnia", "batman begins", "the prestige", "the dark knight", "inception",
    "the dark knight rises","Man of steel","interstellar", "dunkirk", "tenet", "oppenheimer"}
 
    return movies

@app.get("/movies/{movie_name}")
def movies_info(movie_name: str):
    try:
        movies_name_list ={
    "following" : {
        "release year" : "1998",
        "running time" : "70 minutes",
        "country" : "united kingdom",
        "language" : "english",
        "budget" : "6.000 $",
        "box office" : "126.052 $"
    },

    "memento" : {
        "release year" : "2000",
        "running time" : "113 minutes",
        "country" : "united states",
        "language" : "english",
        "budget" : "5-9 million $",
        "box office" : "40.1 million $"
    },
    "insomnia" : {
        "release year" : "2002",
        "running time" : "118 minutes",
        "country" : "united states",
        "language" : "english",
        "budget" : "46 million $",
        "box office" : "113.8 million $"
    },

    "batman begins" : {
        "release year" : "2005",
        "running time" : "140 minutes",
        "country" : "united states and united kingdom",
        "language" : "english",
        "budget" : "150 million $",
        "box office" : "373.7 million $"
    },

    "the prestige" : {
        "release year" : "2006",
        "running time" : "130 minutes",
        "country" : "united kingdom and united states",
        "language" : "english",
        "budget" : "40 million $",
        "box office" : "109.7 million $"
    },

    "the dark knight" : {
        "release year" : "2008",
        "running time" : "152 minutes",
        "country" : "united states and united kingdom",
        "language" : "english",
        "budget" : "185 million $",
        "box office" : "1.006 billion $"
    },

    "inception" : {
        "release year" : "2010",
        "running time" : "148 minutes",
        "country" : "united states and united kingdom",
        "language" : "english",
        "budget" : "160 million $",
        "box office" : "839 million $"
    },

    "the dark knight rises" : {
        "release year" : "2012",
        "running time" : "165 minutes",
        "country" : "united states and united kingdom",
        "language" : "english",
        "budget" : "230 million $",
        "box office" : "1.085 million $"
    },

    "Man of steel" : {
        "release year" : "2013",
        "running time" : "143 minutes",
        "country" : "united states and canada",
        "language" : "english",
        "budget" : "225-258 million $",
        "box office" : "668 million $"
    },

    "interstellar" : {
        "release year" : "2014",
        "running time" : "169 minutes",
        "country" : "united kingdom and united states",
        "language" : "english",
        "budget" : "165 million $",
        "box office" : "731 million $"
    },

    "dunkirk" : {
        "release year" : "2017",
        "running time" : "106 minutes",
        "country" : "united kingdom ,united states, France, Netherland",
        "language" : "english",
        "budget" : "82-150 million $",
        "box office" : "530 million $"
    },

    "tenet" : {
        "release year" : "2020",
        "running time" : "150 minutes",
        "country" : "united kingdom and united states",
        "language" : "english",
        "budget" : "205 million $",
        "box office" : "366 million $"
    },

    "oppenheimer" : {
        "release year" : "2023",
        "running time" : "180 minutes",
        "country" : "united states and united kingdom",
        "language" : "english",
        "budget" : "100 million $",
        "box office" : "964.8 million $"
    }
}
    
        return movies_name_list[movie_name]

    except:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="wrong Nolan`s movie name spell")
    

@app.get("/movies/{movie_name}/poster")
def movies_poster(movie_name: str):
    try:
    

        return FileResponse(f"/movies_posters/{movie_name}.jpg")
    
    except:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="wrong Nolan`s movie name spell")
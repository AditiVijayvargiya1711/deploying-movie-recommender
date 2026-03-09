from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from movie_recommender import recommend
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/recommend/{movie}")
def rec(movie: str):
    result = recommend(movie)
    return {"recommendations": result}

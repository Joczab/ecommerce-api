# Python libs
from pathlib import Path

# FastAPI libs

from fastapi import FastAPI
from fastapi.responses import FileResponse

# FastAPI libs
from src.routes import router 

app = FastAPI()

@app.get('/')
def index():
    return "Hello word"

@app.get('/home')
def render_home():
    return FileResponse(
        path=Path(__file__).parent / 'static' / 'index.html'
    )
    
app.include_router(router)
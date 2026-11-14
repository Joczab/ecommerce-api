from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    
    pass
    return "Hello word"
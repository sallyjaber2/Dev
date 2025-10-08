from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def home():
    return '<h1>Hello Dev Team </h1>'


@app.get('/whowrotethis')
def whowrotethis():
    return "ahmad alkurdi"

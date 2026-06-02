from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(
    directory = "backend/templates"
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request= request,
        name="index.html"
    )

@app.post("/chat")
def chat():
    return {
        "response":
        "I can help you "
        "with refund "
        "related issues"
    }
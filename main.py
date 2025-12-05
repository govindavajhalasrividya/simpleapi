from fastapi import FastAPI,requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routes import test

app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.include_router(test.router)
@app.get("/",response_class=HTMLResponse)
def read_root(request:requests.Request):
    return templates.TemplateResponse("index.html",{"request":request,"name":"Vidya"})


@app.get("/about",response_class=HTMLResponse)
def about(request:requests.Request):
    return templates.TemplateResponse("about.html",{"request":request,"name":"Vidya"})

@app.get("/test",response_class=HTMLResponse)
def test_page(request:requests.Request):
    return templates.TemplateResponse("test.html",{"request":request,"name":"Vidya"})
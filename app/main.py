from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  
from database import engine, Base, get_db
import routers.pc as pc
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
import uvicorn

Base.metadata.create_all(bind= engine)

app = FastAPI()

app.include_router(pc.router)

@app.get("/healthcheck")
def healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  
        return {"status": "ok", "message": "Conectado na base de dados"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
# Corrected mount path for static files
app.mount('/static', StaticFiles(directory='static'), name='static')

# Corrected path for templates
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='index.html',
        context={'request': request}
    )

@app.get('/criar_conta', response_class=HTMLResponse)
def criar_conta(request: Request):
    return templates.TemplateResponse(
        name='criar_conta.html',
        context={'request': request}
    )

@app.get('/delete_item', response_class=HTMLResponse)
def delete_item(request: Request):
    return templates.TemplateResponse(
        name='delete_item.html',
        context={'request': request}
    )

@app.get('/login', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='login.html',
        context={'request': request}
    )

@app.get('/create_item', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='create_item.html',
        context={'request': request}
    )

@app.get('/edit_item', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='edit_item.html',
        context={'request': request}
    )

@app.get('/update_item', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='update_item.html',
        context={'request': request}
    )

@app.get('/pc_lista', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='pc_lista.html',
        context={'request': request}
    )

@app.get('/pc_detalhe', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name='pc_detalhe.html',
        context={'request': request}
    )

if __name__ == "__main__":
    uvicorn.run(app)

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  
from .database import engine, Base, get_db
import app.routers.pc as pc

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pc.router)

@app.get("/healthcheck")
def healthcheck(db: Session = Depends(get_db)):
    try:
       
        db.execute(text("SELECT 1"))  
        return {"status": "ok", "message": "Conectado na base de dados"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

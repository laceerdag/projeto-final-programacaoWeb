from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import app.crud
import app.models
import app.schemas as schemas
from app.database import get_db

router = APIRouter(
    prefix="/pcs",
    tags=["pcs"],
    responses={404: {"descricao": "Não Encontrado"}},
)

@router.post("/", response_model=schemas.PC, status_code=status.HTTP_201_CREATED)
def create_pc(pc: schemas.PCCreate, db: Session = Depends(get_db)):
    return crud.create_pc(db=db, pc=pc)


@router.get("/", response_model=List[schemas.PC])
def read_pcs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pcs = crud.get_pcs(db, skip=skip, limit=limit)
    return pcs


@router.get("/{pc_id}", response_model=schemas.PC)
def read_pc(pc_id: int, db: Session = Depends(get_db)):
    db_pc = crud.get_pc(db, pc_id=pc_id)
    if db_pc is None:
        raise HTTPException(status_code=404, detail="PC Nao encontrado")
    return db_pc


@router.delete("/{pc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pc(pc_id: int, db: Session = Depends(get_db)):
    db_pc = crud.get_pc(db, pc_id=pc_id)
    if db_pc is None:
        raise HTTPException(status_code=404, detail="PC not found")
    crud.delete_pc(db, pc_id=pc_id)
    return
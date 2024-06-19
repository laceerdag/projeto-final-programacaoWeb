from sqlalchemy.orm import Session
import models as models
import schemas as schemas

def get_pc(db: Session, pc_id: int):
    return db.query(models.PC).filter(models.PC.id == pc_id).first()

def get_pcs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PC).offset(skip).limit(limit).all()

def create_pc(db: Session, pc: schemas.PCCreate):
    db_pc = models.PC(**pc.dict())
    db.add(db_pc)
    db.commit()
    db.refresh(db_pc)
    return db_pc

def delete_pc(db: Session, pc_id: int):
    db_pc = db.query(models.PC).filter(models.PC.id == pc_id).first()
    if db_pc:
        db.delete(db_pc)
        db.commit()
    return db_pc
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/data", response_model=list[schemas.TabelaDadosSchema])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_data(db, skip=skip, limit=limit)

from sqlalchemy.orm import Session
from app.models import TabelaDados

def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TabelaDados).offset(skip).limit(limit).all()

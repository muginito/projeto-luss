from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class TabelaDados(Base):
    __tablename__ = "tabela_dados"

    municipio = Column(String)
    ano = Column(Integer)
    codigo = Column(Integer, primary_key=True)
    area = Column(Float, name='AREA (Ha)')
    nome = Column(String)
    bacia = Column(String)

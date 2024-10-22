from pydantic import BaseModel
from datetime import date

class TabelaDadosSchema(BaseModel):

    municipio: str
    ano: int
    codigo: int
    area: float
    nome: str
    bacia: str

    class Config:
        orm_mode = True

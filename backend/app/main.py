from fastapi import FastAPI
from app.routers import data
from app.database import engine, Base

# Cria as tabelas no banco de dados se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas
app.include_router(data.router)

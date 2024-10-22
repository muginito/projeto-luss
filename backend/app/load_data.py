import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
  raise ValueError("A variável de ambiente DATABASE_URL não foi definida.")
USO_PARAGUACU = os.getenv('USO_PARAGUACU')
if not USO_PARAGUACU:
  raise ValueError("A variável de ambiente USO_PARAGUACU não foi definida.")


# Carregar o arquivo Excel
df = pd.read_excel(USO_PARAGUACU, sheet_name='2000')

# Colunas em uppercase
df.rename(columns=(lambda x: x.upper()), inplace=True)

# Criar uma conexão com o banco de dados SQLite
engine = create_engine(DATABASE_URL)

# Escrever os dados na tabela
df.to_sql('tabela_dados', con=engine, if_exists='replace', index=False)

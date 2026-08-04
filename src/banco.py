import sqlite3
from models import Hospede

conexao = sqlite3.connect("hotel.db")
cursor = conexao.cursor()

def criar_tabela_hospedes():
    cursor.execute("""
    CREATE TABLE IF NOT  EXISTS hospedes (
    cpf TEXT PRIMARY KEY,
    nome_completo TEXT,
    data_de_nascimento TEXT,
    telefone TEXT,
    email TEXT,
    cep TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    pais TEXT
    )
    """)

    conexao.commit()

def salvar_hospede(hospede):

    cursor.execute("""
    INSERT INTO hospedes (
    cpf,
    nome_completo,
    data_de_nascimento,
    telefone,
    email,
    cep,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    estado,
    pais
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        hospede.cpf,
        hospede.nome_completo,
        hospede.data_de_nascimento,
        hospede.telefone,
        hospede.email,
        hospede.cep,
        hospede.logradouro,
        hospede.numero,
        hospede.complemento,
        hospede.bairro,
        hospede.cidade,
        hospede.estado,
        hospede.pais
    ))

    conexao.commit()



def buscar_hospede_por_cpf(cpf):
    cursor.execute(
        "SELECT * FROM hospedes WHERE cpf = ?",
        (cpf,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        return None



    hospede = Hospede(
    resultado[0],
    resultado[1],
    resultado[2],
    resultado[3],
    resultado[4],
    resultado[5],
    resultado[6],
    resultado[7],
    resultado[8],
    resultado[9],
    resultado[10],
    resultado[11],
    resultado[12],
)
    return hospede



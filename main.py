import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando Banco de dados.
# Conexão com o banco de dados.
db = create_engine("sqlite:///meubanco.db")


# CREATE DATABASE meubanco.
Session = sessionmaker(bind=db)
session = Session()

# I/O
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão

Base = declarative_base()

# Criando tabela.
class Aluno(Base):
    __tablename__ = "alunos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    idade = Column("idade", String)
    ra = Column("R.A.", String)

    # Definindo atributos da classe.    
    def __init__(self, nome: str, email: str, senha: str, ra: str):
        self.nome = nome 
        self.email = email 
        self.senha = senha
        self.ra = ra

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
# usuario = Usuario("Marta", "marta@gmail.com", "123").
# aluno = Aluno(senha="123", nome="Marta", email="marta@gmail.com", ra="568565")
# session.add(aluno)
# session.commit()

for i in range(2):
    ra = input("\nDigita seu R.A.")
    nome = input("\nDigite seu nome")
    idade = input("\nDigita sua idade")
    email = input("\nDigita seu email")

# Mostrando contéudo do banco de dados.
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.ra}")

# Deletando um usuário.
print("\nExclindo usuário no banco de dados.")
email_aluno = input("Informe o email do aluno: ")
aluno = session.query(Aluno).filter_by(email = email_aluno).first()
session.delete(Aluno)
session.commit()
print("\nEmail apagado com sucesso!")

# Atualiar um usuário.
print("\nAtualizando os dados de um aluno: ")

email_aluno = input("Informe o email do aluno: ")

aluno - session.query(Aluno).filter_by(email = email_aluno).first()

print(f"{aluno.id} - {aluno.nome} - {aluno.email}")

# Fechando conexão.
session.close()
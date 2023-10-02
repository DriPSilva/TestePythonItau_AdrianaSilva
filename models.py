from sqlalchemy import Column, Integer, String

from database import Base

class Pessoa(Base):
    __tablename__ = "Pessoa"

    id: int = Column(Integer, primary_key=True, index=True)
    nomeCompleto: str = Column(String(200), nullable=False)
    dataNascimento: str = Column(String(10), nullable=False)
    endereco: str = Column(String(200), nullable=False)
    cpf: int = Column(Integer, nullable=False)
    estadoCivil: str = Column(String(20), nullable=False)


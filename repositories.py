from sqlalchemy.orm import Session

from models import Pessoa


class PessoaRepository:

    @staticmethod
    def save(db: Session, pessoa: Pessoa) -> Pessoa:
        if pessoa.id:
            db.merge(pessoa)
        else:
            db.add(pessoa)
        db.commit()
        return pessoa

    @staticmethod
    def find_by_id(db: Session, id: int) -> Pessoa:
        return db.query(Pessoa).filter(Pessoa.id == id).first()
    
    @staticmethod
    def find_by_name(db: Session, name: str) -> Pessoa:
        return db.query(Pessoa).filter(Pessoa.nomeCompleto == name).all()
    
    @staticmethod
    def find_by_cpf(db: Session, cpf: int) -> Pessoa:
        return db.query(Pessoa).filter(Pessoa.cpf == cpf).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Pessoa).filter(Pessoa.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        pessoa = db.query(Pessoa).filter(Pessoa.id == id).first()
        if pessoa is not None:
            db.delete(pessoa)
            db.commit()

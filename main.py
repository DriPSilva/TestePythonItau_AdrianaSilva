from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Pessoa
from database import engine, Base, get_db
from repositories import PessoaRepository
from schemas import PessoaRequest, PessoaResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/pessoa", response_model=PessoaResponse, status_code=status.HTTP_201_CREATED)
def create(request: PessoaRequest, db: Session = Depends(get_db)):
    pessoa = PessoaRepository.save(db, Pessoa(**request.dict()))
    return PessoaResponse.from_orm(pessoa)


@app.get("/api/pessoa/{id}", response_model=PessoaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    pessoa = PessoaRepository.find_by_id(db, id)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    return PessoaResponse.from_orm(pessoa)


@app.get("/api/pessoa/{cpf}", response_model=PessoaResponse)
def find_by_cpf(cpf: int, db: Session = Depends(get_db)):
    pessoa = PessoaRepository.find_by_cpf(db, cpf)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    return PessoaResponse.from_orm(pessoa)


@app.get("/api/pessoa/{name}", response_model=PessoaResponse)
def find_by_name(name: str, db: Session = Depends(get_db)):
    pessoa = PessoaRepository.find_by_name (db, name)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    return PessoaResponse.from_orm(pessoa)


@app.delete("/api/pessoa/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PessoaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrado"
        )
    PessoaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/api/pessoa/{id}", response_model=PessoaResponse)
def update(id: int, request: PessoaRequest, db: Session = Depends(get_db)):
    if not PessoaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrado"
        )
    pessoa = PessoaRepository.save(db, Pessoa(id=id, **request.dict()))
    return PessoaResponse.from_orm(pessoa)

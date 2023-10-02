from pydantic import BaseModel


class PessoaBase(BaseModel):
    nomeCompleto: str
    dataNascimento: str
    endereco: str
    cpf: int
    estadoCivil: str


class PessoaRequest(PessoaBase):
    ...


class PessoaResponse(PessoaBase):
    id: int

    class Config:
        orm_mode = True

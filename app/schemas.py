from pydantic import BaseModel


class PCBase(BaseModel):
    nome: str
    descricao: str


class PCCreate(PCBase):
    pass


class PC(PCBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

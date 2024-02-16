from fastapi import APIRouter
from typing import List
from decimal import Decimal
from pydantic import BaseModel
router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str  # PAGAR E RECEBER


class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str  # PAGAR E RECEBER


@router.get("", response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
            id=1,
            descricao='Aluguel',
            valor=1000.50,
            tipo="PAGAR"
        ),
        ContasPagarReceberResponse(
            id=2,
            descricao='Salário',
            valor=5000,
            tipo="RECEBER"
        ),

    ]


# Post sempre restorna algo; código padrão de postagem é o 201
@router.post("", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta: ContasPagarReceberRequest):
    return ContasPagarReceberResponse(
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )

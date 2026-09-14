from enum import Enum


class FormaPagamento(Enum):
    PIX = 'pix'
    BOLETO = 'boleto'
    CARTAO_CREDITO = 'cartao_credito'
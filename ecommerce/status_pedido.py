class StatusPedido:
    CRIADO = "criado"
    PAGO = "pago"
    ENVIADO = "enviado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"

    _TRANSICOES_VALIDAS = {
        CRIADO: [PAGO, CANCELADO],
        PAGO: [ENVIADO, CANCELADO],
        ENVIADO: [ENTREGUE],
        ENTREGUE: [],
        CANCELADO: [],
    }

    @classmethod
    def transicao_valida(cls, de: str, para: str) -> bool:
        return para in cls._TRANSICOES_VALIDAS.get(de, [])
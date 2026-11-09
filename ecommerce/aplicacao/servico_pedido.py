from ecommerce.dominio.criador_pagamento import CriadorPagamento
from ecommerce.dominio.entrega import Entrega
from ecommerce.dominio.expedidor import Expedidor
from ecommerce.dominio.forma_pagamento import FormaPagamento
from ecommerce.infraestrurura.repositorio_pedido import RepositorioPedido
from ecommerce.aplicacao.servico_notificacao import ServicoNotificacao


class ServicoPedido:
    def __init__(
        self,
        criador_pagamento: CriadorPagamento,
        expedidor: Expedidor,
        servico_notificacao: ServicoNotificacao,
        repositorio_pedido: RepositorioPedido
    ) -> None:
        self._criador_pagamento = criador_pagamento
        self._expedidor = expedidor
        self._servico_notificacao = servico_notificacao
        self._repositorio_pedido = repositorio_pedido

    def pagar(
        self, pedido_id: int, cliente, forma: FormaPagamento = FormaPagamento.PIX, **dados
    ) -> None:
        pedido = self._repositorio_pedido.obter(pedido_id)
        pedido.confirmar_pagamento(self._criador_pagamento, forma, **dados)
        self._servico_notificacao.pedido_pago(pedido, cliente)

    def finalizar_compra(self, cliente: "Cliente") -> "Pedido":
        pedido = cliente.finalizar_compra()
        self._repositorio_pedido.adicionar(pedido)
        return pedido

    def despachar(self, pedido, cliente) -> Entrega:
        pedido = self._repositorio_pedido.obter(pedido)
        entrega = self._expedidor.despachar(pedido)
        self._repositorio_pedido.atualizar(pedido)
        self._servico_notificacao.pedido_enviado(pedido, cliente)
        return entrega

import pytest

from ecommerce.categoria import Categoria
from ecommerce.pedido import Pedido
from ecommerce.produto import Produto
from ecommerce.expedidor import ExpedidorLojaCentral, EntregaCorreios
from ecommerce.criador_pagamento import CriadorPagamento


class TestExpedidor:
    def setup_method(self) -> None:
        cat = Categoria(nome="Informática")
        self.notebook = Produto(nome="Notebook", preco=2000, quantidade_estoque=5, categoria=cat)

    def _pedido_pago(self) -> Pedido:
        pedido = Pedido()
        pedido.adicionar_item(self.notebook, 1)
        pedido.confirmar_pagamento(criador_pagamento=CriadorPagamento())
        return pedido

    def test_loja_central_despacha_pelos_correios(self) -> None:
        entrega = ExpedidorLojaCentral().despachar(self._pedido_pago())
        assert isinstance(entrega, EntregaCorreios)
        assert entrega._modalidade == "SEDEX"

    def test_despachar_registra_entrega_e_muda_o_estado(self) -> None:
        pedido = self._pedido_pago()
        entrega = ExpedidorLojaCentral().despachar(pedido)
        assert pedido.entrega is entrega
        assert pedido.status == "enviado"

    def test_nao_despacha_pedido_nao_pago(self) -> None:
        pedido = Pedido()
        pedido.adicionar_item(self.notebook, 1)
        with pytest.raises(ValueError):
            ExpedidorLojaCentral().despachar(pedido)

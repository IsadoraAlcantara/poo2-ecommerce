import pytest

from ecommerce.pedido import Pedido
from ecommerce.criador_pagamento import CriadorPagamento
from ecommerce.forma_pagamento import FormaPagamento
from ecommerce.pagamento import PagamentoPix, PagamentoCartao
from ecommerce.produto import Produto
from ecommerce.categoria import Categoria


class TestCriadorPagamento:

    def setup_method(self) -> None:
        cat = Categoria("Informática")
        notebook = Produto("Notebook", 3000.00, 10, cat)
        self.pedido = Pedido()
        self.pedido.adicionar_item(notebook, 1)
        self.criador = CriadorPagamento()

    def test_cria_pagamento_pix(self) -> None:
        pagamento = self.criador.criar(FormaPagamento.PIX, self.pedido, 3500.0)
        assert isinstance(pagamento, PagamentoPix)

    def test_cria_pagamento_cartao_com_parcelas(self) -> None:
        pagamento = self.criador.criar(
            FormaPagamento.CARTAO_CREDITO, self.pedido, 3600.0, parcelas=3
        )
        assert isinstance(pagamento, PagamentoCartao)
        assert pagamento.parcelas == 3

    def test_forma_desconhecida_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            self.criador.criar("pix", self.pedido, 3500.0)
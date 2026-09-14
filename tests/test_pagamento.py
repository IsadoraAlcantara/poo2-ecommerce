import pytest
from datetime import timedelta, date

from ecommerce.situacao_pagamento import SituacaoPagamento
from ecommerce.pagamento import Pagamento, PagamentoBoleto


class TestPagamento:
    def test_pagamento_e_abstrato(self) -> None:
        with pytest.raises(TypeError):
            Pagamento(self.pedido, 3500.0)

    def test_boleto_vencido_e_recusado(self) -> None:
        pag = PagamentoBoleto(
            self.pedido,
            3500.0,
            linha_digitavel="123",
            vencimento=date.today() - timedelta(days=1),
        )
        pag.confirmar()
        assert pag.situacao == SituacaoPagamento.RECUSADO

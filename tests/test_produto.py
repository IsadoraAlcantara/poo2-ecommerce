from ecommerce.categoria import Categoria
from ecommerce.produto import Produto


class TestProduto:

    def setup_method(self) -> None:
        self.cat = Categoria("Informática")

    def test_cria_produto_com_atributos(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        assert p.nome == "Notebook"
        assert p.preco == 3500.0
        assert p.quantidade_estoque == 10
        assert p.categoria is self.cat
        assert p.descricao == "Notebook azul"

    def test_produto_disponivel_com_estoque(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        assert p.esta_disponivel() is True

    def test_produto_indisponivel_sem_estoque(self) -> None:
        p = Produto("Notebook", 3500.0, 0, self.cat, "Notebook azul")
        assert p.esta_disponivel() is False

    def test_produto_indisponivel_com_estoque_negativo(self) -> None:
        p = Produto("Notebook", 3500.0, -1, self.cat, "Notebook azul")
        assert p.esta_disponivel() is False

    def test_aplicar_desconto_valido(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        p.aplicar_desconto(10)
        assert p.preco == 3150.0

    def test_aplicar_desconto_invalido_abaixo_de_zero(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        try:
            p.aplicar_desconto(-5)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_aplicar_desconto_invalido_acima_de_cem(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        try:
            p.aplicar_desconto(150)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_alterar_preco_valido(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        p.alterar_preco(4000.0)
        assert p.preco == 4000.0

    def test_alterar_preco_invalido_negativo(self) -> None:
        p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
        try:
            p.alterar_preco(-500)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    # def test_alterar_preco_invalido_zero(self) -> None:
    #     p = Produto("Notebook", 3500.0, 10, self.cat, "Notebook azul")
    #     try:
    #         p.alterar_preco(0)
    #         assert False, "Deveria ter lançado exceção"
    #     except ValueError:
    #         pass

    def test_alterar_descricao_para_vazio(self) -> None:
        p = Produto("Notebook", 3000.00, 10, self.cat, "Notebook azul")
        try:
            p.altera_descricao("")
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass
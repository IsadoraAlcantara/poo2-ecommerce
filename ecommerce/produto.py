from ecommerce.categoria import Categoria


class Produto:
    def __init__(
        self, nome: str, preco: float, quantidade_estoque: int, categoria: Categoria
    ) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria

    def esta_disponivel(self) -> bool:
        return self.quantidade_estoque > 0

    def aplicar_desconto(self, percentual: float) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual de desconto deve estar entre 0 e 100.")
        self.preco -= self.preco * (percentual / 100)

    def alterar_preco(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("O preço não pode ser menor que zero.")
        self.preco = novo_preco


if __name__ == "__main__":
    from ecommerce.categoria import Categoria

    cat = Categoria("Informática")
    produto = Produto("Notebook", 3000.00, 10, cat)
    print(
        f"Produto: {produto.nome} - Preco {produto.preco} - Em estoque: {produto.esta_disponivel()}"
    )

    produto.aplicar_desconto(15)
    print(
        f"Produto: {produto.nome} - Preco {produto.preco} - Em estoque: {produto.esta_disponivel()}"
    )

    produto.alterar_preco(2500.00)
    print(
        f"Produto: {produto.nome} - Preco {produto.preco} - Em estoque: {produto.esta_disponivel()}"
    )

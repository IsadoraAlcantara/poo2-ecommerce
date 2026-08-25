class Cliente:
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email
        self.carrinho: "Carrinho | None" = None
        self._pedidos: list["Pedido"] = []

    @property
    def pedidos(self) -> list["Pedido"]:
        return list(self._pedidos)


    def adicionar_pedido(self, pedido: "Pedido") -> None:
        self._pedidos.append(pedido)

    def possui_carrinho(self) -> bool:
        return self.carrinho is not None

    def finalizar_compra(self) -> "Pedido":
        if self.carrinho is None:
            raise ValueError("Cliente nao possui carrinho")
        if not self.carrinho.itens:
            raise ValueError("Carrinho vazio")
        pedido = self.carrinho.finalizar()
        self._pedidos.append(pedido)
        self.carrinho.esvaziar()
        return pedido


if __name__ == "__main__":
    cliente = Cliente("Isadora", "isadora@example.com")
    print(f"Cliente: {cliente.nome} - Email: {cliente.email}")
    print(f"Possui carrinho: {cliente.possui_carrinho()}")

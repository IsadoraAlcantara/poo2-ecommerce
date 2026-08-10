class Cliente:

    def __init__(self, nome: str, email:str) -> None:
        self.nome = nome
        self.email = email
        self.carrinho: "Carrinho | None" = None

    def possui_carrinho(self) -> bool:
        return self.carrinho is not None

if __name__ == "__main__":
    cliente = Cliente("Isadora", "isadora@example.com")
    print(f"Cliente: {cliente.nome} - Email: {cliente.email}")
    print(f"Possui carrinho: {cliente.possui_carrinho()}")
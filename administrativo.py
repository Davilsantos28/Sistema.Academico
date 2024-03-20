from pessoa import Pessoa
class FuncionarioAdministrativo(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def info(self):
        return f"{super().info()}, Cargo: {self.cargo}"
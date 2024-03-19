from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def info(self):
        return f"{super().info()}, Matrícula: {self.matricula}"

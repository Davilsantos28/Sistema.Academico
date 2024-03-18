class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        return f"{self.nome}, {self.idade} anos"


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def info(self):
        return f"{self.nome}, {self.idade} anos, Matrícula: {self.matricula}"


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def info(self):
        return f"{self.nome}, {self.idade} anos, Disciplina: {self.disciplina}"


class FuncionarioAdministrativo(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def info(self):
        return f"{self.nome}, {self.idade} anos, Cargo: {self.cargo}"


def main():
    aluno = Aluno("João", 20, "12345")
    print(aluno.info())

    professor = Professor("Maria", 35, "Matemática")
    print(professor.info())

    funcionario = FuncionarioAdministrativo("Carlos", 40, "Secretário")
    print(funcionario.info())


if __name__ == "__main__":
    main()
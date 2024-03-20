from aluno import Aluno
from professor import Professor
from administrativo import FuncionarioAdministrativo

def main():
    aluno = Aluno("João", 20, "12345")
    print(aluno.info())

    professor = Professor("Maria", 35, "Matemática")
    print(professor.info())

    funcionario = FuncionarioAdministrativo("Carlos", 40, "Secretário")
    print(funcionario.info())


if __name__ == "__main__":
    main()
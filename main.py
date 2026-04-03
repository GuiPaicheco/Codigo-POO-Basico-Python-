class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Matricula: {self.matricula}')
        print(f'Curso: {self.curso}')
        print()

class Universidade:
    def __init__(self, nome, ano_fundacao):
        self.nome = nome
        self.ano_fundacao = ano_fundacao
        self.cursos = []
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
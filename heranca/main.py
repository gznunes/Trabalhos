from aluno import Aluno
from alunoEnsinoMedio import AlunoEnsinoMedio
from alunoGraduacao import AlunoGraduacao

aluno = Aluno(12, "Gabriel", 825)

alunoG = AlunoGraduacao (12, "Gabriel", 825, "5")

alunoMedio = AlunoEnsinoMedio (12, "Gabriel", 825, 9)

alunoG.imprimir()

alunoMedio.imprimir()

aluno.imprimir()


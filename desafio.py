# 6 - Estrutura de condição / Desafio de Código
n = 2
if n % 2 != 0:
    print('Estranho')
elif n % 2 == 0 and n < 10:
    print('Não é estranho')
elif n % 2 == 0 and n >= 10 and n <= 20:
    print('Estranho')
elif n % 2 == 0 and n > 20:
    print('Não é estranho')

# Fatorial
n = int(input("Fatorial: "))
fatorial = 1

for x in range(1, n+1):
    fatorial = fatorial * x

print(fatorial)

# 7 - Estrutura de repetição
# Tabuada
N = int(input("Tabuada: "))

for i in range(1, 11):
    print("{} x {} = {}".format(N, i, N * i))


# Orientação a Objetos
class PrimeiraClasse:
    def __init__(self, curso, descricao):
        self.curso = curso
        self.descricao = descricao

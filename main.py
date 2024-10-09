nome, idade, sobrenome = "Janio", 38, "Alexandre"

for x in range(1, 10):
    print(x)
    print("Olá, ", nome, sobrenome, "sua idade é", idade)
    if x == 2:
        continue
    if x == 8:
        break
    if idade >= 18:
        print(f"{nome} é maior de idade")
    else:
        print(f"{nome} é menor de idade")
else:
    print("O loop entrou no else")

idade2 = 1
while idade2 != 0:
    nome2 = input("Qual o seu nome: ")
    idade2 = int(input("Qual a sua idade: "))
    sobrenome2 = input("Qual o seu sobrenome: ")

    if idade2 == 99:
        break

    if idade2 == 98:
        continue

    print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

    media_idade = (idade + idade2) / 2
    print(f"A média das idades é: {media_idade}")

    if idade2 <= 17:
        print(f"{nome2} é adolecente")
    elif idade2 >= 18 and idade2 <= 50:
        print(f"{nome2} é adulto")
    else:
        print(f"{nome2} é idoso")
else:
    print("O loop entrou no else")

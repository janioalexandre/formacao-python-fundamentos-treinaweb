from usuario import Usuario

lista_usuarios = []

continuar = 1
while continuar != 0:
    try:
        nome = input("Digite o nome do usuário: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = int(input("Digite a idade: "))

        usuario = Usuario(nome, idade, sobrenome)

        lista_usuarios.append(usuario)

        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        continuar = int(input("Deseja continuar cadastrando? 0 - Saír 1- Continuar: "))
    except ValueError:
        print("Você deve informar um número válido")
else:
    print("Lista de usuários cadastrados: ")

    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade}")

'''
# Manipulação de lista:
pop(índice): remove o elemento da lista;
index(elemento): retorna o índice do elemento na lista;
count(elemento): retorna a quantidade de vezes em que um elemento aparece na lista;
sort(): ordena a lista;
reverse(): inverte a ordem da lista.
'''
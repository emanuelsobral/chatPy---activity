import os

mensagem = []

nome = input("Digite seu nome: ")

while True:

    os.system('cls')

    print("Bem vindo ao chat, digite /quit para sair")

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'] + ": " + m['texto'])


    print('________________________________________')

    texto = input(nome + ': ')
    if texto == '/quit':
        break

    mensagem.append({
        'nome': nome,
        'texto': texto
        
    })
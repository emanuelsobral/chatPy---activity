import os

mesnagem = []

nome = input("Digite seu nome: ")

while True:

    os.system('cls')

    print("Bem vindo ao chat, digite /quit para sair")
    print("Digite sua mensagem: ")

    if len(mesnagem) > 0:
        for m in mesnagem:
            print(m['nome'] + ": " + m['texto'])


    print('________________________________________')

    texto = input('mesnagem: ')
    if texto == '/quit':
        break

    mesnagem.append({
        'nome': nome,
        'texto': texto
        
    })
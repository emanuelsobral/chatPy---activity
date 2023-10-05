# Atividade de Python - Estrutura de um Chat

## Descrição
Este projeto é uma atividade simples de Python que simula a estrutura de um chat. O objetivo é praticar o uso do laço `while` e condições com `if` em Python. Este chat não está conectado à internet, ele serve apenas para fins de aprendizado.

## Requisitos
- Python 3.x

## Como executar
1. Clone este repositório ou baixe o arquivo `chat.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo `chat.py` está localizado.
3. Execute o comando `python chat.py`.

## Funcionalidades
- O chat permite que o usuário insira uma mensagem.
- O chat exibe o nome e a mensagem inserida.
- O chat continua até que o usuário decida sair digitando `/quit`.

## Estrutura do Código
O código é estruturado em torno de um laço `while`, que continua a solicitar a entrada do usuário até que uma condição de saída seja atendida.

Dentro do laço `while`, há uma condição `if` que verifica a entrada do usuário.

# Parte 2: Atividade Assistida e Guiada

## Criando um chat local em Python

O chat pode ser encontrado na pasta `localChat` dentro do projeto, sendo dividido em o arquivo do host e dos convidados. Nesta atividade, fizemos a criação de um chat local em Python durante uma aula guiada. Este projeto utiliza as bibliotecas `time`, `socket`, e `sys`.

A aula assistida foi baseada no artigo da ANU no site askpython.com (devidos créditos concedidos).

### Estrutura do Projeto

```
localChat
│
├── chatLocalHost.py
└── chatLocalInvited.py
```

### Bibliotecas Utilizadas

- `time`
- `socket`
- `sys`

### Referências

- Artigo da ANU no site askpython.com

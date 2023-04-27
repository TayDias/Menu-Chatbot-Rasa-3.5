
<h1 align="center"> Rasa bot</h1>

<p>Este é o meu primeiro chatbot construído com a plataforma Rasa. As funcionalidades do menu de opções são recreativas, o objetivo desse projeto é entender melhor a estrutura de funcionamento do Rasa, manipulando cada vez mais o código.</p>


# Índice

* [Status do projeto](#Status-do-projeto)
* [Tecnologias utilizadas](#Tecnologias-utilizadas)
* [Funcionalidades](#Funcionalidades)
* [Modelo de NLU](#modelo-de-nlu)
* [Configuração do ambiente de teste](#configuração-do-ambiente-de-teste)
* [Referências](#Referências)


# Status do projeto

:construction: Em desenvolvimento :construction:


# Tecnologias utilizadas

- [Python](https://www.python.org)
- [Rasa](https://rasa.com/docs/rasa/)


# Funcionalidades

1 - Jogar Pedra/Papel/Tesoura
2 - Ver fotos de cachorros


# Modelo de NLU

<p>A interpretação de decisões e a contextualização é feita usando NLU (Natural Language Understanding), através da extração de informações estruturadas das mensagens do usuário.</p>

## Intenções

<table>
  <thead>
    <th>Nome da intenção</th>
    <th>Ação associada</th>
  </thead>
  <body>
    <tr>
      <td>greet</td>
      <td>Identificar o início da interação com o assistente</td>
    </tr>
    <tr>
      <td>goodbye</td>
      <td>Identificar o fim da interação com o assistente</td>
    </tr>
    <tr>
      <td>inform</td>
      <td>Identificar opção escolhida entre as entidades declaradas</td>
    </tr>
    <tr>
      <td>affirm</td>
      <td>Identificar afirmação quanto a ação oferecida pelo assistente</td>
    </tr>
    <tr>
      <td>deny</td>
      <td>Identificar negação quanto a ação oferecida pelo assistente</td>
    </tr>
    <tr>
      <td>play_game</td>
      <td>Identificar solicitação de uso da funcionalidade "1 - Jogar Pedra/Papel/Tesoura"</td>
    </tr>
    <tr>
      <td>dog_pic</td>
      <td>Identificar solicitação de uso da funcionalidade "2 - Ver fotos de cachorros"</td>
    </tr>
  </body>
</table>

## Entidades

<table>
  <thead>
    <th>Nome da entidade</th>
    <th>Ação associada</th>
  </thead>
  <body>
    <tr>
      <td>number</td>
      <td>Números utilizados como opções no menu de funcionalidades disponíveis</td>
    </tr>
    <tr>
      <td>choice</td>
      <td>Conjunto de valores aceitos pelo jogo Pedra/Papel/Tesoura</td>
    </tr>
  </body>
</table>

# Configuração do ambiente de teste

## Pré-requisitos

- **Python** versão 3.10.6 ou superior;
- **Rasa** - versão 3.5.0 ou superior;

## Teste em homologação

1. Faça o clone do repositório e abra o código no seu editor. Esse código foi desenvolvido no [Visual Studio Code](https://code.visualstudio.com).
2. Execute `rasa run actions` no terminal para ativar o servidor.
3. Fale com o assistente executando o comando `rasa shell` em uma nova aba do terminal.


# Referências

Command Line Interface
https://rasa.com/docs/rasa/command-line-interface

Conversational AI with Rasa Open Source 3.x
https://www.youtube.com/playlist?list=PL75e0qA87dlEjGAc9j9v3a5h1mxI2Z9fi

Emoji-cheat-sheet:
https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

Introduction to Rasa Open Source & Rasa Pro
https://rasa.com/docs/rasa/

Rasa 3.0: Create a new assistant in Rasa 3.0 (Livecoding)
https://www.youtube.com/watch?v=PfYBXidENlg

Rasa-3.0-rock-paper-scissors-chatbot
https://github.com/rctatman/Rasa-3.0-rock-paper-scissors-chatbot

The internet's biggest collection of open source dog pictures
https://dog.ceo/dog-api/

Web APIs, Python Requests & Performing an HTTP Request in Python Tutorial
https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiIh-Dxxcr-AhUPGkwKHbiWCgUYABAAGgJvYQ&ae=2&ohost=www.google.com&cid=CAESbOD2XHObo3U_Hd9juno3NdSAEj3IW82M-nBa11xEFSk4vzIfNlvphXpJzh1e1ispl6fLs9FIzjDBTndVT8_bPjMBTUfdXp2GLKJzdRhWUL_kcHbquFsW8LLygkZ_VXqaM8FoWY6vjGUqPaoePA&sig=AOD64_0d0aZ0Yu6hKeuR00CrCXdH-swshg&q&adurl&ved=2ahUKEwiQqdPxxcr-AhWsrJUCHX0-CLsQ0Qx6BAgGEAE
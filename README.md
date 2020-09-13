![enter image description here](https://github.com/Gabriel94Dantas/BOBAPI/blob/master/imgs/logo-bob-api.jpg)
#  BOB-OpenBlindBank-API

## Papel da BOB-API
A BOB-API é uma solução que visa a utilização do conceito de Open Bank por dispositivos de voz, seja ele Alexa, Google Assistente ou Siri.

## Aspectos Técnicos
A BOB-API foi construída em Python versão 3.6, utilizando Flask framework, MongoDB, Docker e Requests, cada um desses artefatos foram utilizados com um propósito específico que será explanado a frente.

### Flask
Flask é um microframework WSGI para aplicações web. Com ele, torna-se possível a construção de uma API Restful de maneira rápida e fácil preservando a possibilidade de escalar para produtos complexos.

### MongoDB
MongoDB é um moderno banco de dados não relacional, com capacidade de distribuição, baseado em documentos para próposito geral. Sua escolha está apoiada em seu desempenho quando não há necessidade de pesquisas muito complexas.

### Docker
Docker é um container de aplicação que possibilita a criação de unidades de softwares padronizadas que empacotam os códigos e suas dependências, então possibilita a execução de rápida e confiável da stack de um ambiente para o outro. Com isso, o Docker possibilita a escalabilidade da stack.

### Requests
Requests é uma biblioteca simples e elegante para utilizar para consumo de uma API. Foi esta biblioteca que foi utilizada para acessar a API disponibilizada durante o Hackathon.
 
 ## Endpoints
 Inicialmente a BOB-API possui quatro endpoints:
 

 1. `POST <host>/login`
 2. `GET <host>/balance`
 3. `GET <host>/transactions`
 4. `GET <host>/morning-calls`
 5. `GET <host>/logs`

O primeiro endpoint é responsável por executar o login do dispositivo operado por voz com o BOB-API, essa ação gerará um token que será válido por um período.

O segundo endpoint irá retornar  o saldo do cliente que estiver acessando a API.

O  terceiro endpoint irá retornar o extrato do cliente.

O quarto retorna um áudio da morning call disponível no canal do youtube do banco Safra.

E por fim o quinto retorno os logs gerados no sistema para um sistema administrativo, com isso visa-se obter métricas acerca do uso da API.

## Como executar
Nesta API foram utilizados tanto o docker-engine quanto o docker-compose, logo será necessária a prévia instalação destes softwares.

Com a utilização do Docker para montagem da stack, basta executar o comando `docker-compose up -d --build` na pasta principal da API que a stack irá ser inicializada.

## Erros Lançados
Ao executar a API, caso não seja feito a autenticação previamente, qualquer endpoint retornará o código HTTP 401.

Se o usuário ou o dispositivo não estiverem cadastrados na API o erro retornado será o código HTTP 404. 

## Host
A API foi disponibilizada por temporariamente no seguinte link:

 - ec2-18-218-87-145.us-east-2.compute.amazonaws.com
 - Porta 5001
 - O arquivo `API-test.postman_collection.json` possui os testes na API disponibilizada neste link.

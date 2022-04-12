
![Logo](https://www.seekpng.com/png/small/26-262743_black-on-transparent-apache-kafka-logo-transparent.png)


# Python kafka implementation

Esse repositório apresenta uma abstração em cima dos modulos de Consumer e Producer da biblioteca kafka-python, a qual entrega classes prontas para utilização do sistema de streaming e mensageria Apache Kafka.

Foi utilizada uma arquitetura hexagonal para implementar o serviço que irá consumir as mensagens criadas dentro dos tópicos broker, a qual apresenta as classes de utilização do Kafka dentro de adapters.

Além disso foi utilizado o módulo pydantic para criar a estrutura dos eventos.

## Features

- Criação de tópicos
- Utilização das mensagens dos tópicos
- Eventos como schemas do pydantic
- Arquitetura hexagonal para criação de serviços
- Containerização dos serviços singularmente
- Utilização de docker-compose para o broker e serviços


## Como executar

Para executar essa aplicação, é necessário apenas subir as instâncias dos containers através do docker-compose:

```bash
  docker-compose up
```
    
## Autores

- [@matheusafonsouza](https://www.github.com/matheusafonsouza)


## Contribuição

Qualquer contribuição é extremamente bem vinda!

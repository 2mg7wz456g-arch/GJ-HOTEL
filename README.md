# 🏨 GJ-AI HOTEL

Sistema de gerenciamento hoteleiro desenvolvido em Python como projeto de estudo, com foco em boas práticas de programação, orientação a objetos e banco de dados.

## 🚀 Funcionalidades atuais

- Menu principal
- Check-in
- Cadastro de hóspedes
- Classe `Hospede`
- Busca de hóspedes por CPF
- Banco de dados SQLite
- Persistência de dados
- Pesquisa de hóspedes já cadastrados

## 🛠 Tecnologias

- Python 3
- SQLite
- Git
- GitHub

## 📁 Estrutura

src/
├── main.py
├── menu.py
├── checkin.py
├── models.py
├── banco.py
└── hotel.db

## 🎯 Próximas funcionalidades

- [ ] Evitar cadastro duplicado de CPF
- [ ] Sistema de reservas
- [ ] Cadastro de quartos
- [ ] Check-out
- [ ] Histórico de hospedagens
- [ ] Interface gráfica
- [ ] Inteligência Artificial para auxiliar a recepção

## 📚 Objetivo

O GJ-AI HOTEL não é apenas um sistema de hotel. É um projeto para estudar programação na prática, evoluindo gradualmente até se tornar uma aplicação completa.

## 📅 Diário do Projeto

### v0.0.2

- Criada a classe `Hospede`
- Implementado banco de dados SQLite
- Criada tabela `hospedes`
- Implementado cadastro de hóspedes
- Implementada busca por CPF
- Conversão dos dados do SQLite em objetos `Hospede`
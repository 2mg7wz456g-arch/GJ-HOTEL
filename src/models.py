class Hospede:


    def __init__(self, cpf, nome_completo, data_de_nascimento,
                  telefone, email, cep, logradouro, numero,
                    complemento, bairro, cidade, estado, pais):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.data_de_nascimento = data_de_nascimento


        self.telefone = telefone
        self.email = email


        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais


class quarto:


    def __init__(self,categoria, andar, numero_do_quarto, status, capacidade):
        self.categoria = categoria
        self.andar = andar
        self.numero_do_quarto = numero_do_quarto
        self.status = status
        self.capacidade = capacidade


class Reserva:

    
    def __init__(self, hospede, quarto, valor_da_diaria, data_de_entrada, data_de_saida, 
                 quantidade_de_hospedes, forma_de_pagamento,):
        self.hospede = hospede
        self.quarto = quarto
        self.valor_da_diaria = valor_da_diaria
        self.data_de_entrada = data_de_entrada
        self.data_de_saida = data_de_saida
        self.quantidade_de_hospedes = quantidade_de_hospedes
        self.forma_de_pagamento = forma_de_pagamento
        
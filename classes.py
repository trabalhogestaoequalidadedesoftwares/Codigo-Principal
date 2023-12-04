class Hotel:

    def __init__(self, nome, quartos_disponiveis):
        self.nome = nome
        self.quartos_disponiveis = quartos_disponiveis

    def reservar_quarto(self, numero_quarto):
        if numero_quarto in self.quartos_disponiveis:
            self.quartos_disponiveis.remove(numero_quarto)
            print("O quarto está disponível para reserva.")
            reserva = str(input("Deseja reservar o quarto? S/N?"))
            if reserva == ("S" and "s"):
                print("Quarto reservado com sucesso!")
            else:
                print("Quarto não reservado.")
                self.quartos_disponiveis.append(numero_quarto)
                quartos.sort(key=int)

        else:
            print("O quarto não está disponível para ser reservado.")
            quartos.sort(key=int)

    def liberar_quarto(self, numero_quarto):
        if numero_quarto not in self.quartos_disponiveis:
            self.quartos_disponiveis.append(numero_quarto)
            numero = numero_quarto
            print(f"O quarto {numero} foi liberado.")
            quartos.sort(key=int)
        else:
            numero = numero_quarto
            print(f"O quarto {numero} já está disponível para reserva.")

    def status(self):
        print(f"O hotel {self.nome} tem {len(self.quartos_disponiveis)} quartos disponíveis.")

class Cliente:

    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

    def realizar_cadastro(self):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo: ")
        cpf = int(input("Digite seu CPF: "))
        if idade < 18:
            print("Cadastros permitidos apenas para maiores de 18 anos!")
            if idade >= 18:
                print(f"Cliente {cliente.nome} cadastrado com sucesso!")
        else:
            print(f"Cliente {cliente.nome} cadastrado com sucesso!")
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"CPF: {self.cpf}")

    def atualizar_cadastro(self):
        print("Para alterar os seus dados, insira os novos dados abaixo:")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo: ")
        cpf = int(input("Digite seu CPF: "))
        if idade < 18:
            print("Cadastros permitidos apenas para maiores de 18 anos!")
            if idade >= 18:
                print("Cliente atualizado com sucesso!")
        else:
            print(f"Cliente {cliente.nome} atualizado com sucesso!")
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

import datetime
class Checkin:

    def __init__(self, nome, qntd_hospedes, cpf, data):
        self.nome = nome
        self.qntd_hospedes = qntd_hospedes
        self.cpf = cpf
        self.data = data
        self.hospedes = []

    def realizar_checkin(self):
        nome = input("Digite seu nome: ")
        qntd_hospedes = int(input("Digite a quantidade de hospedes: "))
        cpf = input("Digite seu CPF: ")
        data = input("Digite o dia da sua hospedagem dd/mmm/aaaa: ")
        self.nome = nome
        self.qntd_hospedes = qntd_hospedes
        self.cpf = cpf
        self.data = data
        self.hospedes = []
        if data == datetime.date.today().strftime("%d/%m/%Y"):
            for i in range(self.qntd_hospedes):
                nome_hospede = input("Digite o nome do hospede: ")
                self.hospedes.append(nome_hospede)
            print("Checkin realizado com sucesso!")
            print("Nome do cliente:", self.nome)
            print("Quantidade de hospedes:", self.qntd_hospedes)
            print("CPF:", self.cpf)
            print("Data do check-in:", self.data)
            print("Hospedes:", self.hospedes)
        else:
            print(f"O check-in deve ser realizado no dia da hospedagem ({self.data})!\nCheck-in não realizado.")








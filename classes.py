class Hotel:

    def __init__(self, quartos_disponiveis):
        self.quartos_disponiveis = quartos_disponiveis

    def is_quartosdisponiveis(self):
        if len(quartosDisponiveis) == 0:
            return True
        else:
            return False
    
    def reservar_quarto(self, numero_quarto):
        if numero_quarto in self.quartos_disponiveis:
            quartosDisponiveis.remove(numero_quarto)
            quartosIndisponiveis.append(numero_quarto)
            print("O quarto está disponível para reserva.")
            reserva = str.lower(input("Deseja reservar o quarto? S/N? \n"))
            if reserva == ("s"):
                print("Quarto reservado com sucesso!")
            else:
                print("Quarto não reservado.")
                self.quartos_disponiveis.append(numero_quarto)
                quartosDisponiveis.sort(key=int)
        else:
            print("O quarto não está disponível para ser reservado.")
            quartosDisponiveis.sort(key=int)

    def liberar_quarto(self, numero_quarto):
        if quartosDisponiveis.count(numero_quarto) and quartosIndisponiveis.count(numero_quarto) == 0: 
            print("Não é possivel liberar um quarto que não exista nas nossas instalações")
        elif numero_quarto in quartosIndisponiveis:
            quartosIndisponiveis.remove(numero_quarto)
            quartosDisponiveis.append(numero_quarto)
            print(f"O quarto {numero_quarto} foi liberado.")
            quartosDisponiveis.sort(key=int)
        else:
            print(f"O quarto {numero_quarto} já está disponível para reserva.")

    def status(self):
        print(f"O hotel Bedroom Dreams tem {len(self.quartos_disponiveis)} quartos disponíveis.")

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
                print(f"Cliente {Cliente.nome} cadastrado com sucesso!")
        else:
            print(f"Cliente {Cliente.nome} cadastrado com sucesso!")
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

class Quarto:
    def _init_(self, numero, tipo, preco_por_noite):
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite
    def calcular_custo_estadia(self, numero_de_noites):
        return numero_de_noites * self.preco_por_noite

    def __str__(self):
        return f"Número do Quarto: {self.numero}, Tipo: {self.tipo}, Preço por Noite: {self.preco_por_noite}"

class Funcionario:
    def _init_(self, nome, cargo, numero_identificacao, salario):
        self.nome = nome
        self.cargo = cargo
        self.numero_identificacao = numero_identificacao
        self.salario = salario

class CheckOut:
    def _init_(self, data_hora, cliente, quarto):
        self.data_hora = data_hora
        self.cliente = cliente
        self.quarto = quarto
    def __str__(self):
        return f"Data e Hora: {self.data_hora}, Cliente: {self.cliente}, Quarto: {self.quarto}"
    checkout_instance = CheckOut(data_hora, cliente, quarto)
    print(checkout_instance)


class ComentarioHotel:
    def _init_(self, cliente, data, classificacao, comentario):
        self.cliente = cliente
        self.data = data
        self.classificacao = classificacao
        self.comentario = comentario

class ServicoHotel:
    def _init_(self, nome, horarios_funcionamento, custo_adicional):
        self.nome = nome
        self.horarios_funcionamento = horarios_funcionamento
        self.custo_adicional = custo_adicional
    def calcular_custo_total(self, custo_base):
        return custo_base + self.custo_adicional

    def __str__(self):
        return f"Nome do Serviço: {self.nome}, Horários de Funcionamento: {self.horarios_funcionamento}, Custo Adicional: {self.custo_adicional}"

class EventoHotel:
    def _init_(self, nome, data, localizacao, detalhes):
        self.nome = nome
        self.data = data
        self.localizacao = localizacao
        self.detalhes = detalhes


quartosDisponiveis = [1, 2, 3, 4, 5]
quartosIndisponiveis = []



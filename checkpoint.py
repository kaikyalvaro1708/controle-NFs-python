"""
Gabriel Machado Belardino - RM550121
Ana Beatriz Farah Alvez - RM97865
Kaiky Alvaro de Miranda - RM98118
Lucas Rodrigues da Silva - RM98344
Pedro Henrique Bicas Couto - RM99534"""


# Definindo uma lista vazia para armazenar as NFs
pagamentos = []
recebimentos = []
   
# Definindo as opções do menu
def menu_principal():
    print("----- MENU PRINCIPAL -----")
    print("1 - Contas a receber")
    print("2 - Contas a pagar")
    print("0 - Sair do Sistema")

# Definindo as opções do menu de contas a pagar
def menu_pagamento():
    print("----- MENU DE CONTAS A RECEBER -----")
    print("1 - Registrar Nota Fiscal")
    print("2 - Mostrar Todas as NFs")
    print("0 - Voltar ao Menu Principal")

# Definindo as opções do menu de contas a receber
def menu_recebimento():
    print("----- MENU DE CONTAS A PAGAR -----")
    print("1 - Registrar Nota Fiscal")
    print("2 - Mostrar Todas as NFs")
    print("0 - Voltar ao Menu Principal")


# Definindo a função para registrar contas a pagar
def info_pagamento():
    global consumidor
    global cpf
    global descricao
    global num_NF
    global quantidade
    global valor 

# utilizando try para impedir o usuario de inserir string nos inputs de int e float
    while True:
        try:
            consumidor = str(input("Digite o nome do consumidor: "))
            break
        except:
            print("Informação inválida, escreva novamente")
    while True:
        try:
            cpf = int(input("Digite o número do CPF: "))
            break
        except:
            print("Informação inválida, digite novamente")
    while True:
        try:
            descricao = str(input("Escreva uma descrição da NF: "))
            break
        except:
            print("Informação inválida, escreva novamente")
    while True:
        try:
            num_NF = int(input("Digite o número da Nota Fiscal: "))
            break
        except:
            print("Informação inválida, digite novamente")
    while True:
        try:
            quantidade = int(input("Digite a quantidade de NFs: "))
            break
        except:
            print("Quantidade invalida, tente novamente.")
    while True:
        try:
            valor = float(input("Digite o valor da NF: "))
            break
        except:
            print("Informação inválida, digite novamente")



#Definindo a função para registrar pagamentos
def registrar_pagamento():
    # For in iterando todos os items do contas a pagar
    for itens in pagamentos:
        # Verificando se o item ja possui no contas a pagar
        if itens['Descrição'] == descricao:
            info_pagamento()
            # Somando a quantidade da novos pagamentos 
            itens['Quantidade de NFs'] +=quantidade
            # Cadastrando o pagamento no no array de pagamentos
            pagamentos.append({'Nome do consumidor': consumidor, 'CPF': cpf, 'Descrição': descricao, 'Número da NF': num_NF, 'Quantidade': quantidade, 'Valor': valor})
            return
    info_pagamento()
    # Registrando o novo pagamento no array de pagamentos
    pagamentos.append({'Nome do consumidor': consumidor, 'CPF': cpf, 'Descrição': descricao, 'Número da NF': num_NF, 'Quantidade': quantidade, 'Valor': valor})
    print("Nota Fiscal registrada com sucesso!")

# Definindo a função para mostrar todas as contas a pagar
def mostrar_pagamentos():
    if len(pagamentos) == 0:
            print("Nenhuma conta a pagar registrada.")
    else:
        print("----- TODAS AS CONTAS A PAGAR -----")
        # For mostrando todas as contas a pagar
        for contas_pagar in pagamentos:
            print("Nome do consumidor:", contas_pagar['Nome do consumidor'])
            print("Descrição:", contas_pagar['Descrição'])
            print("CPF:", contas_pagar['CPF'])
            print("Número da NF:", contas_pagar['Número da NF'])
            print("Quantidade:", contas_pagar['Quantidade'])
            print("Valor total da compra:", contas_pagar['Valor'] * contas_pagar['Quantidade'])
            print("")
        print("-" * 20)


# Definindo as informações de notas fiscais a receber
def info_recebimento():
    global nome_cnpj
    global descricao
    global num_NF
    global quantidade
    global valor 

# utilizando try para impedir o usuario de inserir string nos inputs de int e float
    while True:
        try:
            nome_cnpj = str(input("Digite o nome do fornecedor CNPJ: "))
            break
        except:
            print("Informação inválida, escreva novamente")
    while True:
        try:
            descricao = str(input("Escreva a descrição: "))
            break
        except:
            print("Informação inválida, escreva novamente")
    while True:
        try:
            num_NF = int(input("Digite o número da Nota Fiscal: "))
            break
        except:
            print("Informação inválida, digite novamente")
    while True:
        try:
            quantidade = int(input("Digite a quantidade de NFs: "))
            break
        except:
            print("Quantidade invalida, tente novamente.")
    while True:
        try:
            valor = float(input("Digite o valor da NF: "))
            break
        except:
            print("Informação inválida, digite novamente")

#Definindo a função para registrar recebimentos
def registrar_recebimento():
    # For in iterando todos os itens do contar a receber
    for itens in recebimentos:
        # Verificando se o item da nova compra ja possui no contas a receber
        if itens['Descrição'] == descricao:
            info_recebimento()
            # Somando a quantidade da novos recebimentos 
            itens['Quantidade de NFs'] +=quantidade
            # Cadastrando o recebimento no no array de recebimentos
            recebimentos.append({'Nome do fornecedor CNPJ': nome_cnpj, 'Descrição': descricao, 'Número da Nota Fiscal': num_NF, 'Quantidade': quantidade, 'Valor': valor})
            return
    info_recebimento()

    # Registrando o novo recebimento no array de recebimentos
    recebimentos.append({'Nome do fornecedor CNPJ': nome_cnpj, 'Descrição': descricao, 'Número da Nota Fiscal': num_NF,'Quantidade': quantidade, 'Valor': valor})
    print("Nota Fiscal registrada com sucesso!")

# Definindo a função para mostrar todas as compras
def mostrar_recebimentos():
    if len(recebimentos) == 0:
            print("Nenhuma conta a receber registrada.")
    else:
        print("----- TODAS AS CONTAS A RECEBER -----")
        # For mostrando todas os recebimentos
        for contas_receber in recebimentos:
            print("Nome do Fornecedor CNPJ:", contas_receber['Nome do Fornecedor CNPJ'])
            print("Descrição:", contas_receber['Descrição'])
            print("Número da Nota Fiscal:", contas_receber['Número da Nota Fiscal'])
            print("Quantidade:", contas_receber['Quantidade'])
            print("Valor total da compra:", contas_receber['Valor'] * contas_receber['Quantidade'])
            print("")
        print("-" * 20)


# Definindo a função para sair do sistema
def sair():
    print("Obrigado por utilizar o sistema!")
    exit()


def main():
    while True:
        # Utilizando try para inpedir o usuario de inserir string nos inputs de int e float
        while True:
            try: 
                menu_principal()
                opcao = int(input("Digite a opção desejada: "))
                break
            except:
                print("Opção invalida, tente novamente.")
        # Match case para o menu principal
        match opcao:
            case 1:
                while True:
                    # Utilizando try para inpedir o usuario de inserir string nos inputs de int e float
                    while True:
                        try:
                            menu_pagamento()
                            opcao_pagamentos = int(input("Digite a opção desejada: "))
                            break
                        except:
                            print("Opção invalida, tente novamente.")
                    # Match case para o menu de contas a pagar
                    match opcao_pagamentos:
                        case 1:
                            registrar_pagamento()
                        case 2:
                            mostrar_pagamentos()
                        case 0:
                            break
                        case _:
                            print("Opção inválida!")
            case 2:
                while True:
                    # Utilizando try para inpedir o usuario de inserir string nos inputs de int e float
                    while True:
                        try:
                            menu_recebimento()
                            opcao_recebimentos = int(input("Digite a opção desejada: "))
                            break
                        except:
                            print("Opção invalida, tente novamente.")
                    # Match case para o menu de contas a receber
                    match opcao_recebimentos:
                        case 1:
                            registrar_recebimento()
                        case 2:
                            mostrar_recebimentos()
                        case 0:
                            break
                        case _:
                            print("Opção inválida!")
            case 0:
                sair()
            case _:
                print("Opção inválida!")
main()

    

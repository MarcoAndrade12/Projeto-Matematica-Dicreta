import Defs as df
import color as col
import Users as us
import bd_coletas as bd
import time
from datetime import datetime
import log

global user
user = None

global data
data = ''

global familia
familia = ''

global genero
genero = ''

global espécie
espécie = ''

global hábito
hábito = ''

global origem
origem = ''

global recurso
recurso = ''

global referencia
referencia = ''

global floração
floração = ''

#objeto da coleta, para facilitar a captura de dados
class obj_coleta:
   def __init__(self, id, nome):
    self.nome = nome
    self.id = id

  
## Banner padrão do logo do Sug-Flora App
# banner = '''   
#   █████████  █████  █████   █████████             ███████████ █████          ███████    ███████████     █████████  
#  ███░░░░░███░░███  ░░███   ███░░░░░███           ░░███░░░░░░█░░███         ███░░░░░███ ░░███░░░░░███   ███░░░░░███ 
# ░███    ░░░  ░███   ░███  ███     ░░░             ░███   █ ░  ░███        ███     ░░███ ░███    ░███  ░███    ░███ 
# ░░█████████  ░███   ░███ ░███          ██████████ ░███████    ░███       ░███      ░███ ░██████████   ░███████████ 
#  ░░░░░░░░███ ░███   ░███ ░███    █████░░░░░░░░░░  ░███░░░█    ░███       ░███      ░███ ░███░░░░░███  ░███░░░░░███ 
#  ███    ░███ ░███   ░███ ░░███  ░░███             ░███  ░     ░███      █░░███     ███  ░███    ░███  ░███    ░███ 
# ░░█████████  ░░████████   ░░█████████             █████       ███████████ ░░░███████░   █████   █████ █████   █████
#  ░░░░░░░░░    ░░░░░░░░     ░░░░░░░░░             ░░░░░       ░░░░░░░░░░░    ░░░░░░░    ░░░░░   ░░░░░ ░░░░░   ░░░░░ 
# Alpha.1.0'''

## Banner padrão do logo do Sug-Flora App
banner = '''
  ____  ____  _____ ____                          
 / ___||  _ \| ____/ ___|                         
 \___ \| |_) |  _|| |                             
  ___) |  __/| |__| |___                          
 |____/|_|   |_____\____| _____ _                 
 / ___| _   _  __ _      |  ___| | ___  _ __ __ _ 
 \___ \| | | |/ _` |_____| |_  | |/ _ \| '__/ _` |
  ___) | |_| | (_| |_____|  _| | | (_) | | | (_| |
 |____/ \__,_|\__, |     |_|   |_|\___/|_|  \__,_|
              |___/                               
Alpha.1.0'''

# Inicia o sistema mostrando a primeira página para o usuário
def intro():

    while True:
        indexes=['Entrar', 'Nova Conta','Encerrar']
            # Opções que o usuário terá nessa tela
        resp = df.options(banner+"\nSeja Bem vindo ao Sistema Único de Gestão de Flora! \nPara começarmos, selecione uma opção abaixo:\n", indexes)
            # Função que vai mostrar o menu para o usuário e retornar o que ele selecionou.
            # A função options retorna o index da opção selecionada pelo usuário da lista 'indexes'.

        if resp==0:
            global user
            # se o index retornado for 0, então o usuário escolheu logar.
            user = False

            while user == False:
                # Verifica se a função de login encontrou o usuário e retornou seus dados.

                user = login()
                    # Chama a função de login do main.py que vai colher os dados de login.

                if user != False:
                    # Se o login for bem sucedido, chama a tela Menu principal
                    MenuPrincipal()
                else:
                    # Se o login for mal sucedido, informa ao usuário que deu algo errado.
                    bn = banner + "\n\n Credenciais incorretas!! O que deseja fazer?\n"
                        # Informe do erro
                    opt = ['Tentar novamente','Cadastrar-se','Encerrar']
                        # Opções da tela de erro
                    resp = df.options(bn,opt)
                        # Menu do erro, retorna o index das opções escolhidas
                    
                    if resp == 0:
                        # Se retornar 0, a opção escolhida é 'Tentar novamente' e ele apenas mantém a repetição.
                        pass
                    elif resp == 1:
                        # Se retornar 1, a opção escolhida é 'Cadastre-se' e chama a função para cadastrar um novo usuário.
                        singup()
                    elif resp == 2:
                        # Se retornar 2, a opção escolhida é 'Encerrar'
                        Exit()

        elif resp==1:
            # se o index retornado for 1, então o usuário escolheu se cadastrar.
            singup()
                # Chama a função que vai colher os dados do novo usuário e solicitar ao Users.py que cadastre-o.

        elif resp == 2:
            Exit()

# login
def login():
    df.Cls()
    user = input(banner + "\nBEM VINDO AO SISTEMA ÚNICO DE GESTÃO FLORAL." + "\n Digite o login de seu usuário: ")
    df.Cls()

    pwd = input(banner+ "\nBEM VINDO AO SISTEMA ÚNICO DE GESTÃO FLORAL." + '\n Digite sua senha: ')
    
    return us.login(user,pwd)
    
# singup
def singup():
    while True:
        df.Cls()
        name = input(banner+ "\n\nNOVO USUÁRIO" + '\n Antes de começarmos, precisamos saber o seu nome: ')
        df.Cls()
        user = input(banner+ "\n\nNOVO USUÁRIO" + '\n Digite o login que deseja cadastrar: ')
        df.Cls()

        erro = ""
        df.Cls()
        pwd1 = input(banner+ "\n\nNOVO USUÁRIO" + erro + '\n Digite sua senha: ')
        df.Cls()
        pwd2 = input(banner+ "\n\nNOVO USUÁRIO" + '\n Confirme sua senha: ')

        if pwd1 == pwd2:
            tentativa = us.cadastro_cliente(name,user,pwd1)
            if tentativa != False:
                op = df.options(banner + "\n\nCadastro efetuado com sucesso.",['Continuar'])
                break
            else:
                op = df.options(banner + "\n\nOPS!! Algo deu errado, tentar novamente?",['Sim','Não'])
                if op == 0:
                    pass
                else:
                    break
        else:
            erro = col.color("\n AS SENHAS NÃO CORRESPONDEM. TENTE NOVAMENTE.",'vermelho',negrito=True)


        #ir para procedimento de singup
        


    # newUser(login,senha)

def MenuPrincipal():
    global user
    opt = ['Minhas coletas','Relatórios','Sair']
    resp = df.options(f'{banner}\n\n Bem vindo, {user[1]}!!\n Selecione a opção que deseja: \n',opt)
    print(resp)

    if resp == 2:
        exit()
    elif resp == 0:
        MinhasColetas()        

def MinhasColetas():
    global user
    # Tela de coletas

    while True:
        coletas = bd.read(user[0])
        ShowColetas(coletas)

        op = df.options(banner,['\nNova coleta','Exibir novamente','Fazer uma pesquisa','Aplicar Filtro','Relatório','Editar coleta','Voltar'])
        if op == 0:
            NewColeta()
        elif op == 1:
            # coleta = ''

            pass
        elif op == 2:
            # Criar função de filtro
            pass
        elif op == 3:
            # Criar função de vários filtros
            pass
        elif op == 4:
            # Relatório
            pass
        elif op == 5:
            # Edição da coleta
            print(banner+ "\n\nNOVO USUÁRIO" + "\nSELECIONE QUAL ENTREGA DESEJA ALTERAR: ")
            coletas=bd.read(user[0])
            coletasfmt = []
            print('ID_user,familia,genero,especie,habito,origem,recursos,referencia,floração')

            for i in range(coletas):
                coletasfmt.append(coletas[0]+","+coletas[1]+","+coletas[2]+","+coletas[3]+","+coletas[4]+","+coletas[5]+","+coletas[6]+","+coletas[7]+","+coletas[8])

            df.options(banner, coletasfmt)
                
            



        
        elif op == 6:
            MenuPrincipal()



def NewColeta():
    global data
    global familia
    global genero
    global espécie
    global hábito
    global origem
    global recurso
    global referencia
    global floração


    dt = datetime.today()
    dt = [f'{dt.day}/{dt.month}/{dt.year}']
    # print(dt)

    data = Escolha('Qual a data da coleta?',dt)

    fam = Unique(bd.read(str(user[0])),3)

    familia = Escolha('Escolha ou escreva a Família da nova coleta: ',fam)

    genero = []

    generos = [generos[4] for generos in bd.read(user[0]) if generos[3] == familia]

    genero = Escolha('Escolha ou escreva o Gênero da nova coleta: ',generos)

    espécies = [espécies[5] for espécies in bd.read(user[0]) if espécies[4] == genero]

    espécie = Escolha('Escolha ou escreva a Espécie da nova coleta: ',espécies)

    hábito = Escolha('Escolha ou escreva o Hábito da coleta:', ['Erva','Trepadeira','Arbusto','Árvore'])
    origem = Escolha('Escolha ou escreva a Origem da coleta:',['Nativa','Exótica','N/Id'])
    recurso = Escolha('Escolha ou escreva o Recurso da coleta:',['Pólen','Néctar','N/Id'])
    referencia = Escolha('Escolha ou escreva a Referência da coleta: ',['N/Id'])
    floração = Escolha('A coleta estava Florida(Fértil)? ',['Sim','Não'])

    registro = data + "," + familia + "," + genero + "," + espécie + "," + hábito + "," + origem + "," + recurso + "," + referencia + "," + floração
    
    bd.insert(user[0],registro)

    # print(registro)
    
    # ShowColetas(generos)

def Unique(bd,index):

    Unique = []

    log.NewLog('main.Unique',bd)

    for Uniq in bd:
        log.NewLog('main.Unique',Uniq)
        if Uniq[index] not in Unique:
            Unique.append(Uniq[index])


    return Unique

def Escolha(cabeçalho,bd):
    global data
    global familia
    global genero
    global espécie
    global hábito
    global origem
    global recurso
    global referencia
    global floração

    escolhas = f"\n\nData: {data} | Fam: {familia} | Gên: {genero} | Esp: {espécie}\nHáb: {hábito} | Ori: {origem} | Rec: {recurso} | Ref: {referencia} | Flor: {floração}\n\n"
    # print(escolhas)
    
    

    dados = ['\nEscrever'] + bd
    # print(dados)
    escolha = df.options(banner + escolhas + cabeçalho,dados)
    
    if escolha == 0:
        escolha = input(banner + '\n' + cabeçalho + '\n').capitalize()
        df.Cls()
    else:
        escolha = dados[escolha]

    return escolha

def ShowColetas(bd):

    titulos = ['ID','Data','Família','Gênero','Espécie','Hábito','Origem','Recurso','Referência','Flor']
    coletas = ""
    
    coletas = coletas + f'{titulos[0]:<3}' + f'{titulos[1]:<12}' + f'{titulos[2]:<15}' + f'{titulos[3]:<15}' + f'{titulos[4]:<15}' + f'{titulos[5]:<15}' + f'{titulos[6]:<15}' + f'{titulos[7]:<15}' + f'{titulos[8]:<15}' + f'{titulos[9]:<15}\n'
    
    for i in bd:

        coletas = coletas + f'{i[0]:<3}' + f'{i[2]:<12}' + f'{i[3]:<15}' + f'{i[4]:<15}' + f'{i[5]:<15}' + f'{i[6]:<15}' + f'{i[7]:<15}' + f'{i[8]:<15}' + f'{i[9]:<15}' + f'{i[10]:<15}\n'

    
    df.Cls()
    print(banner)
    print(coletas)
    input('\nEnter para continuar')

    df.Cls()

def Exit():
    df.Cls()
    print('Muito obrigado por usar o SuGFlora')
    exit()



# NewColeta()
# MinhasColetas()

intro()

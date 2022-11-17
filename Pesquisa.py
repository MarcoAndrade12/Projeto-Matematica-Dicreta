import bd_coletas as bd
import log
#Usado para pesquisa com algum termino unico usado pelo usuario

def pesquisa (valorunico):
    coleta=[coleta for coleta in lista if pesquisa in coleta]
    for i in coleta:
        print (*i, sep =', ')
    

# pesquisa(lista,pesquisaespecial)

#Filtro de pesquisa
# def Filtro(critério):

#     lista = bd.read()
#     filtropesquisa = []
#     pesquisaespecial = input("Digite o nome que gostaria de pesquisar dentro do banco de dados: ")
#     filtropesquisa.append(pesquisaespecial)
#     continuidade = input ("Gostaria de adicionar mais algun termo?Caso não queira digite Não: ")
#     while not continuidade == "Não":
#         pesquisaespecial = input("Digite o nome que gostaria de pesquisar dentro do banco de dados: ")
#         filtropesquisa.append(pesquisaespecial)
#         continuidade = input ("Gostaria de adicionar mais algun termo?Caso não queira digite Não: ")

# def pesquisafiltro(lista,pesquisafiltro):
#     coleta=[coleta for coleta in lista if pesquisafiltro in coleta]
#     for i in coleta:
#         print (*i, sep =', ')
#         for i in coleta:
#             print (*i, sep =', ')

# pesquisafiltro(lista,valor)

#---- Funções----#
# RELATÓRIOS QUANTITATIVOS

    # Total de coletas Geral > Retornar um número total de coletas. ------ Talvez nem precise.

    # Vinicius # Total de coleta por critério > Retornar um número do total de coletas de acordo com um filtro.

# Victor # Frequência de familia/Genero/Espécie > Retorna a quantidade de vezes que aquele critério aparece = Total dele dividido pelo total de coletas.    
def freq(bd,critério):
    try:
        filtro = len([freq for freq in bd if critério in freq])
        coletas = len(bd)-1
        if filtro > 0:
            freq = filtro / coletas
        else:
            freq = 0.0 
            log.NewLog('Pesquisa.freq',f'A consulta da frequência de "{critério}" retornou 0.0. Ou sua escrita está errada, ou realmente não existe no banco de dados.')
        return freq
    except:
        log.NewLog('Pesquisa.freq',f'Erro ao tentar retornar a frequência do critério "{critério}". Provavelmente ele não existe no banco de dados fornecido para a função ou sua escrita está errada ou o banco de dados está em branco.')
        
        return False


    # Stephanie # Total de coletas identificadas para cada critério.
    # Stephanie # Total de coletas não identificadas para cada critério.

# RELATÓRIOS ESTATÍSTICOS
    
    # Robson # Quantidade de coletas totalmente identificadas em % > Conta quantas coletas estão 100% identificadas e divide pela quantidade de coletas
    # Robson # Quantidade de coletas em % para um critério > Conta quantas coletas de um critério estão 100% identificadas e divide pela quantidade de coletas


#banco de dados
#leitura
import Defs as df

def read(ID_user):
    # Abre o banco de dados das coletas e retorna ao programador uma lista contendo todas as coletas.
    # Retorna junto o cabeçalho do arquivo.txt se tiver.

    coletas=open("coletas.txt","r")
    
        # Abre o arquivo em modo de leitura e armazena ele na variável coleta
    lista_all=[]
        # Cria uma lista temporária para armazenar uma lista com as coletas
    for i in coletas:
        # print(i)
        # Passa dentro de coletas e pega cada uma das linhas em formato string

        coleta = i.strip("\n").split(",")
        if coleta[1] == ID_user:
            lista_all.append(coleta)
            # Transforma a string da linha em uma lista e retira o caractere especial \n

    # print(lista_all)
    return lista_all
        # Retorna ao programador que chamou a função, uma lista com todas as coletas do arquivo.txt

#insert

def insert(ID_user,coleta):
    # Função para inserir apenas UMA coleta no banco de dados.
    bd=open("coletas.txt","a")
        # abre o arquivo coletas.txt em modo append
    registro = "\n" + str(df.NextId(read(ID_user))) + ',' + ID_user + "," + coleta
        # Cria um registro que será armazenado como nova coleta
        # Se trata de uma string na estrutura que nosso banco de dados exige
        # Antes, ele procura qual o próximo Id da coleta a ser inserida e coloca junto da string.
    bd.write(registro)
        # Escreve a nova coleta no banco de dados na próxima linha do arquivo.
    return read(ID_user) 
        # Faz novamente a leitura do banco de dados atualizado e retorna a nova versão.


#insert("familia,genero,especie,habito,origem,recursos,referencia,floração")
bd = 'ID_user,familia,genero,especie,habito,origem,recursos,referencia,floração'
# print(insert(bd))


# editar()
#editar coleta
# Id, Coluna, Novainformação
# 1° Percorrer toda lista e verificar se o ID é == ao informado pelo usuário.
# Enquanto percorre a lista, se o id não for ==, você insere a linha em uma lista.
#tenho que criar uma função e depois um For que procura o que esta na lista e modifica
# def editar(ID):
#     coletas = read()
#     coletas[ID] = ""
#     return read()



def editar(ID_user,newColeta):
    # newColeta precisa ser uma lista
    arqAntigo = read(ID_user)
    newLista = ''

    for coleta in arqAntigo:

        if coleta[0] == newColeta[0]:
            newLista = newLista + newColeta
        else:
            newLista.append(coleta)
        
    print('\n')
    print(newLista)
        

    print(newLista)
    arquivo = open('nome.txt', 'w')
     # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo) 
       # escreva o conteúdo criado anteriormente nele.
        

# editar('002',['2','002','Asteraceeeee'])

# print(editar())








#coleta=excluir 

# meuArquivo = open('nome.txt', 'r')
# nome = meuArquivo.readlines()
# for nome in nome:
#     print(meuArquivo))





# def excluir(ID):

#     coletas = read()
#     coletas[ID] = ""

#     for read1 in coletas:
#         print(read1)
    
# print(excluir(bd))
import os
from pynput import keyboard
import color as col
import time
import curses
from curses import wrapper

def Cls(): 
    # Função para limpar o console, feito dessa forma para facilitar a escrita do código.
    os.system('cls' if os.name == 'nt' else 'clear')

def Div(): 
    # Função para criar uma divisão no console, para facilitar a criação de cabeçalhos
    print("="*30)

def NextId(bd): 
    # Função que retorna qual é o próximo Id a ser inserido em um banco de dados
    # OBS: Recebe um banco de dados em lista onde o primeiro item de cada "linha" deve ter um ID.
    
    id = 0 
    # Variável onde será inserido o número do Id
    for i in bd: 
        # For para passar em todas as linhas do banco de dados inserido
 
        if i[0] != "ID": 
            # Para cada linha, verifica se a 'coluna' 0, que deve ter a informação do ID é diferente de 'ID". Isso serve para descartar a primeira      
            # ..linha da lista, que geralmente é apenas um cabeçalho.
            try:
                if id < int(i[0]): 
                    # Verifica se o id é menor que o id da linha atual.
                    id = int(i[0]) 
                        # se o id for menor que a linha atual, ele substitui seu valor pelo valor do ID da linha e assim mantém sempre o maior número até 
                        #..que passe por todas as linhas do banco de dados.
            except:
                print("error")      
    return id+1 
        # Como queremos que ele retorne apenas o próximo ID, ele pega o maior id do banco de dados e soma +1 e retorna para o usuário.

def main(cabeçalho,opções,select):
    
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        
    nop = len(opções) 
        
    stdscr.clear()

    stdscr.addstr(cabeçalho)
    
    for i in range(0,nop): 
        if i == nop-1:
            txt = '\n' + opções[i] + '\n'
        else:
            txt = '\n' + opções[i]
        
        if i == select:
            stdscr.addstr(txt, 256 )
            stdscr.refresh()
            
        else:
            
            stdscr.addstr(txt)
            stdscr.refresh()
        
    
    key = stdscr.getch()
    curses.endwin()

    if key == 65:
        return 'cima'
    if key == 66:
        return 'baixo'
    if key == 10:
        return 'enter'

def options(cabeçalho,opções):

    select = 0
    nop = len(opções)

    while True:

        selec = main(cabeçalho,opções,select)

        if selec == 'enter':
            break

        elif selec == 'cima':
            select -= 1

        elif selec == 'baixo':
            select += 1
    
        if select < 0:
        
            select = nop-1 
            
        elif select > nop-1:
        
            select = 0

    return select

# print(options(cabeçalho,texto))


            
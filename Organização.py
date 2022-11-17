
# Usuários > BD_Users | Id, Nome, Senha || Vinicius

  -----Funções banco de dados Usuários-----
  # def newUser
  # def dropUser
  # def editUser
  # def AllUsers
  # def getUser
 
  -----Funções de usuário----
  # def Logar 
  # def Deslogar
  # def EditProfile 
  # def DeleteProfile




# Tela Login:
    - Logar
        E= Entrar com Login;
        E= Entrar com Senha;
        
    - Cadastrar-Se
        E= Entrar com Nome;
        E= Entrar com Login;
        E= Entrar com Senha;
        E= Confirmação dos dados;

    - Fechar
        E= Confirmação


# Tela Menu > Lista de opções || **Stephanie**
    - Conta
        - Editar conta
            E= Entrar com Login (Se for editar um usuário terceiro, se em branco: editar ele mesmo) *Para administradores
                #-Opções de edição-#
                - Nome
                    E= Novo Nome
                - Login
                    E= Novo Login
                - Senha
                    E= Antiga Senha (Para verificar se é ele mesmo editando)
                    E= Nova Senha
                    E= Confirmação da Senha

                - Rule (para administradores)
                    E= Número da nova regra de usuário.
        - Apagar conta
            E= Entrar com Login (Se for excluir um usuário terceiro, se em branco: ecluir ele mesmo) *Para administradores
                E= Entrar com senha do usuário logado.
                E= Confirmar exclusão. (Se não confirmar, voltar ao menu principal)
        - Voltar

    - Projetos
        C= Lista dos Projetos
        - Editar Projeto
            C= Lista de campos
            - Editar Campo
                - Adicionar Coleta
                    E= Dados da nova coleta
                    Loop

                - Editar Coleta
                    E= Lista de Ids a serem alterados
                    C= Mostra as coletas selecionadas
                    E= Campo a ser alterado
                    E= Nova informação do Campo
                    Loop

                - Ecluir Coleta
                    E= Lista de Ids a serem ecluídos
                    C= Mostra as coletas selecionadas
                    E= Confirmação da exclusão

                - Voltar



            - Excluir Campo
            - Voltar
        - Relatório de Projetos
            - Relatório Geral
                E= Relatório de qual projeto?
                E= Aplicar filtro?
                    E= Entrada do filtro (Campo: Filtro Campo: Filtro... etc) **Verificar como será esse filtro
                C= Mostrar as coletas
                C= Mostrar o relatório
                E= Confirmação se deseja exportar
                S= Exportação do peojeto em txt

            - Relatório Quantitativo
                E= Relatório de qual projeto?
                E= Aplicar filtro?
                    E= Entrada do filtro (Campo: Filtro Campo: Filtro... etc) **Verificar como será esse filtro
                C= Mostrar as coletas
                C= Mostrar o relatório
                E= Confirmação se deseja exportar
                S= Exportação do peojeto em txt

            - Relatório Estatístico
                E= Relatório de qual projeto?
                E= Aplicar filtro?
                    E= Entrada do filtro (Campo: Filtro Campo: Filtro... etc) **Verificar como será esse filtro
                C= Mostrar as coletas
                C= Mostrar o relatório
                E= Confirmação se deseja exportar
                S= Exportação do peojeto em txt
            
            

        - Excluir Projeto
        - Voltar

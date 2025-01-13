import os

livrosLidos2k25 = [{'autor':'George Orwell', 'titulo':'A Revolução dos Bichos', 'pagina atual':'48', 'data de inicio': '10/01/2025', 'data de finalizacao': '??/??/??', 'tempo de leitura total':'1 hora e 9 minutos'}, {'autor':'George Orwell', 'titulo':'A Revolução dos Bichos', 'pagina atual':'48', 'data de inicio': '10/01/2025', 'data de finalizacao': '??/??/??', 'tempo de leitura total':'1 hora e 9 minutos'}]

# Voltar na lista de restaurante para colocar o status

def exibir_nome_app():
    '''Essa função exibe o nome do Aplicativo.'''

    print('''
    🅱🅻🅸🅱🅻🅸🅾🆃🅴🅲🅰 🅳🅾 🅻🅰🅱🆄
    ''')

def exibir_menu():
    '''Essa função exibe o menu de opções do aplicativo'''
    print('1. Cadastrar Livro')
    print('2. Listar Livros')
    print('3. Definir Status dos Livros')
    print('4. Sair\n')

def voltar_ao_menu():
    '''Essa função exibe uma mensagem e aguarda o usuário digitar qualquer tecla para voltar ao menu.
    
    Input: 
    - Qualquer tecla

    Output:
    - Menu do aplicativo

    '''
    input('\nDigite qualquer tecla para voltar ao menu.\n')
    main()

def exibir_subtitulo(subtitulo):
    '''Essa função exibe um subtitulo com base no texto passado.'''
    os.system('cls')
    traco = '-' * (len(subtitulo) + 2)
    print(f'{traco}')
    print(f'|{subtitulo}|')
    print(f'{traco}')
    print()

def cadastrar_livros():
    '''Essa função cadastra um restaurante na lista de restaurantes.
    
    Inputs:
    - Nome do Autor do Livro: str
    - Titulo da obra: str
    - Página Atual do Livro: int


    Output:
    - Livro Colocado na Lista de Dicionario de Livros
    - Mensagem de Sucesso

    '''
    exibir_subtitulo('Bem Vindo ao Cadastro de Novos Livros! Parabéns por Começar Mais uma Jornada!!!')
    autor_do_livro = input('Digite o nome do autor do livro: ')
    titulo_do_livro = input(f'Digite o título da obra do autor {autor_do_livro}: ')
    pagina_atual = input 

def listar_livros():
    pass

def definir_status_do_livro():
    pass

def encerrar_programa():
   '''Essa função encerra o aplicativo.'''
   exibir_subtitulo('Encerrando o Programa! Não Esqueça de Voltar com Resultados e Mais Livros!')



def opcao_invalida():
    '''Essa função exibe uma mensagem de opção inválida volta ao menu através da função "voltar_ao_menu".'''
    print('\nOpção Inválida!\n')
    voltar_ao_menu()

def escolher_opcao(): 
    '''Essa função aguarda o usuário escolher uma opção do menu e chama a função correspondente a opção escolhida.
    
    Input:
    - Opção Escolhida: int

    Output:
    - Função correspondente a opção escolhida
    - Ou erro
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_livros()
        elif opcao_escolhida == 2:
            listar_livros()
        elif opcao_escolhida == 3:
            definir_status_do_livro()
        elif opcao_escolhida == 4:
            encerrar_programa()
    except:
            opcao_invalida()


def main():
    '''Essa função é a função principal do aplicativo.
    '''
    os.system('cls')
    exibir_nome_app()
    

if __name__ == '__main__':
    main()
import os

livrosLidos2025 = [
    {
        'autor': 'George Orwell',
        'titulo': 'A Revolução dos Bichos',
        'data_de_inicio': '10/01/25',
        'data_de_finalizacao': '??/??/??',
        'tempo_de_leitura_total': '182',
        'pagina_atual': 76,
        'status': 'Lendo'
    }
]

def exibir_nome_app():
    """
    Exibe o nome do aplicativo em formato ASCII art.
    """
    print('''
    
█▄▄ █ █▄▄ █░░ █ █▀█ ▀█▀ █▀▀ █▀▀ ▄▀█   █▀▄ █▀█   █░░ ▄▀█ █▄▄ █░█
█▄█ █ █▄█ █▄▄ █ █▄█ ░█░ ██▄ █▄▄ █▀█   █▄▀ █▄█   █▄▄ █▀█ █▄█ █▄█
    ''')

def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    print('1. Cadastrar Livro')
    print('2. Listar Livros')
    print('3. Alterar os Dados das Leituras')
    print('4. Sair\n')

def voltar_ao_menu():
    """
    Retorna ao menu principal após exibir uma mensagem ao usuário.
    """
    input('\nDigite qualquer tecla para voltar ao menu.\n')
    main()

def exibir_subtitulo(subtitulo):
    """
    Exibe um subtítulo formatado.
    """
    os.system('cls')
    traco = '-' * (len(subtitulo) + 2)
    print(f'{traco}')
    print(f'|{subtitulo}|')
    print(f'{traco}')
    print()

def cadastrar_livros():
    """
    Permite ao usuário cadastrar novos livros na lista `livrosLidos2025`.
    """
    exibir_subtitulo('Bem Vindo ao Cadastro de Novos Livros! Parabéns por Começar Mais uma Jornada!!!')
    autor_do_livro = input('Digite o nome do autor do livro: ')
    titulo_do_livro = input(f'Digite o título da obra do autor {autor_do_livro}: ')
    pagina_atual = input(f'Digite a página atual do livro {titulo_do_livro}: ')
    data_de_inicio = input(f'Digite a data de início da leitura do livro {titulo_do_livro}, no formato "dia/mês/ano": ')
    tempo_de_leitura_total = input(f'Digite o tempo total de leitura do livro {titulo_do_livro}, em minutos: ')
    livrosLidos2025.append({
        'autor': autor_do_livro,
        'titulo': titulo_do_livro,
        'data_de_inicio': data_de_inicio,
        'data_de_finalizacao': '',
        'tempo_de_leitura_total': f'{tempo_de_leitura_total} minutos',
        'pagina_atual': pagina_atual,
        'status': 'Lendo'
    })
    print(f'\nO livro {titulo_do_livro}, do autor {autor_do_livro}, foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_livros():
    """
    Lista todos os livros cadastrados na lista `livrosLidos2025`.
    """
    exibir_subtitulo('Listando Livros Cadastrados')
    if not livrosLidos2025:
        print('Nenhum livro cadastrado ainda.')
    else:
        for idx, livro in enumerate(livrosLidos2025, start=1):
            autor_livro = livro['autor']
            titulo_livro = livro['titulo']
            data_inicio = livro['data_de_inicio']
            data_finalizacao = livro['data_de_finalizacao']
            pagina_atual = livro['pagina_atual']
            status = livro['status']
            # Verifica se a data de finalização é vazia ou inválida
            if not data_finalizacao or data_finalizacao == '??/??/??':
                data_finalizacao_str = ''
                
            else:
                data_finalizacao_str = f' - Data de Finalização: {data_finalizacao}' 

            print(f'{idx}. Autor: {autor_livro} - Título: {titulo_livro} - Data de Início: {data_inicio}{data_finalizacao_str} - Página Atual: {pagina_atual} - Status: {status} - Tempo de Leitura Total: {livro["tempo_de_leitura_total"]} minutos')
    voltar_ao_menu()

def alterar_dados_das_leituras():
    """
    Permite ao usuário alterar os dados de um livro específico na lista `livrosLidos2025`.
    """
    exibir_subtitulo('Alteração de Dados das Leituras')
    autor_do_livro = input('Digite o nome do autor do livro que deseja alterar: ')
    titulo_do_livro = input(f'Digite o titulo da obra do autor {autor_do_livro} que deseja alterar: ')
    for livro in livrosLidos2025:
        if livro['autor'] == autor_do_livro and livro['titulo'] == titulo_do_livro:
            pagina_atual = input(f'Digite a nova página atual do livro {titulo_do_livro}: ')
            tempo_de_leitura_total = input(f'Digite o novo tempo total de leitura do livro {titulo_do_livro}, em minutos: ')
            data_de_finalizacao = input(f'Digite a data de finalização da leitura do livro {titulo_do_livro}, no formato "dia/mês/ano", caso não tenha finalizado apenas clique enter, ou escreva "??/??/??": ')
            if not data_de_finalizacao:
                data_de_finalizacao = ''
                status = 'Lendo'
            else:
                status = 'Finalizado'
            livro['pagina_atual'] = pagina_atual
            livro['tempo_de_leitura_total'] = f'{tempo_de_leitura_total} minutos'
            livro['data_de_finalizacao'] = data_de_finalizacao
            livro['status'] = status
            print(f'\nOs dados do livro {titulo_do_livro}, do autor {autor_do_livro}, foram alterados com sucesso!\n')
        else: 
            print('O Livro não foi encontrado...')
    voltar_ao_menu()

def encerrar_programa():
    """
    Exibe uma mensagem de encerramento do programa.
    """
    exibir_subtitulo('Encerrando o Programa! Não Esqueça de Voltar com Resultados e Mais Livros!')

def opcao_invalida():
    """
    Exibe uma mensagem de erro ao selecionar uma opção inválida e retorna ao menu.
    """
    print('\nOpção Inválida!\n')
    voltar_ao_menu()

def escolher_opcao():
    """
    Processa a escolha do usuário no menu principal.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_livros()
        elif opcao_escolhida == 2:
            listar_livros()
        elif opcao_escolhida == 3:
            alterar_dados_das_leituras()
        elif opcao_escolhida == 4:
            encerrar_programa()
    except:
            opcao_invalida()

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    os.system('cls')
    exibir_nome_app() 
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
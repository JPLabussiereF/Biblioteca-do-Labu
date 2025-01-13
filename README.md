# Gerenciador de Leituras 2025

Este projeto foi criado com o objetivo de praticar habilidades de programação em Python. Ele consiste em um gerenciador de leituras, onde é possível cadastrar livros, listar os livros cadastrados, alterar os dados das leituras e encerrar o programa.

## Funcionalidades

- **Exibir Nome do Aplicativo**: Mostra o nome do programa.
- **Exibir Menu**: Apresenta as opções principais do aplicativo.
- **Cadastrar Livros**: Permite adicionar novos livros à lista de leituras.
- **Listar Livros**: Mostra todos os livros cadastrados com seus respectivos detalhes.
- **Alterar Dados das Leituras**: Atualiza informações de um livro cadastrado, como página atual, tempo total de leitura e data de finalização.
- **Encerrar Programa**: Finaliza o programa com uma mensagem de despedida.

## Estrutura do Código

O programa está dividido em funções que gerenciam as diferentes funcionalidades:

- `exibir_nome_app()`: Exibe o nome do aplicativo.
- `exibir_menu()`: Mostra as opções do menu principal.
- `voltar_ao_menu()`: Retorna ao menu principal após uma interação.
- `exibir_subtitulo(subtitulo)`: Exibe um subtítulo formatado para organizar as telas do programa.
- `cadastrar_livros()`: Permite ao usuário adicionar novos livros na lista de leituras.
- `listar_livros()`: Lista todos os livros cadastrados com seus detalhes.
- `alterar_dados_das_leituras()`: Permite alterar informações de livros já cadastrados.
- `encerrar_programa()`: Finaliza o programa e exibe uma mensagem.
- `opcao_invalida()`: Lida com entradas inválidas do usuário.
- `escolher_opcao()`: Processa a escolha do usuário no menu principal.
- `main()`: Função principal que controla o fluxo do programa.

## Como Executar

1. Certifique-se de ter o Python 3 instalado no seu computador.
2. Baixe ou clone este repositório.
3. Navegue até o diretório onde o arquivo está localizado.
4. Execute o programa com o comando:

```bash
python <nome_do_arquivo>.py
```

## Estrutura da Lista de Livros

Os livros cadastrados são armazenados em uma lista chamada `livrosLidos2025`. Cada livro é representado como um dicionário com os seguintes campos:

- `autor`: Nome do autor do livro.
- `titulo`: Título da obra.
- `data_de_inicio`: Data de início da leitura (formato "dia/mês/ano").
- `data_de_finalizacao`: Data de finalização da leitura (ou "??/??/??" se não finalizado).
- `tempo_de_leitura_total`: Tempo total de leitura em minutos.
- `pagina_atual`: Página atual da leitura.
- `status`: Status da leitura ("Lendo" ou "Finalizado").

## Aprendizados

Este projeto foi desenvolvido para consolidar os seguintes conceitos em Python:

- Estruturas de dados: listas e dicionários.
- Manipulação de strings e entrada do usuário.
- Estruturação de código em funções.
- Controle de fluxo com condicionais e laços de repetição.
- Boas práticas de programação, como organização de funções e utilização de docstrings.

## Melhorias Futuras

- Adicionar persistência de dados para salvar as informações em um arquivo (como JSON ou CSV).
- Implementar uma interface gráfica para facilitar o uso do programa.
- Permitir a remoção de livros da lista.
- Realizar validação de entradas para evitar erros.

## Contribuição

Este projeto é um exercício prático e está aberto a sugestões e melhorias. Caso tenha alguma ideia ou encontre um problema, fique à vontade para abrir uma issue ou enviar um pull request.

Desenvolvido com o objetivo de aprimorar minhas habilidades em Python!!

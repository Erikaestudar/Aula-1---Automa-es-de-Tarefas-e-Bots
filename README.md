# Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web usando Python e a biblioteca `pyautogui`.

## Visão Geral

O objetivo principal é abrir o navegador, acessar uma página de login, autenticar e cadastrar produtos automaticamente com base nos dados do arquivo `produtos.csv`.

## Arquivos do Projeto

- `codigo.py`: script principal de automação que faz login e cadastra cada produto a partir de `produtos.csv`.
- `auxiliar.py`: utilitário para capturar a posição do mouse na tela. Muito útil para ajustar coordenadas de clique.
- `pegar_posicao.py`: script simples que imprime a posição atual do mouse após 5 segundos.
- `gabarito.py`: versão de referência da automação com os passos principais detalhados.
- `produtos.csv`: base de dados de exemplo com os produtos a cadastrar.

## Dependências

Instale as bibliotecas necessárias antes de rodar o projeto:

```bash
pip install pyautogui pyperclip pandas
```

> Observação: em alguns casos, `pyautogui` requer pacotes adicionais como `pillow`.

## Como Funciona

1. O script abre o navegador Google Chrome.
2. Acessa o link de login:
   `https://dlp.hashtagtreinamentos.com/python/intensivao/login`
3. Faz login com o e-mail `pythonimpressionador@gmail.com` e a senha especificada no próprio código.
4. Carrega a planilha `produtos.csv` usando `pandas`.
5. Itera por cada linha do arquivo, preenchendo campos no formulário e submetendo o cadastro.
6. Após cada cadastro, o script dá scroll para voltar ao início da tela.

## Estrutura do arquivo `produtos.csv`

O CSV deve conter as colunas:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

## Como Executar

1. Ajuste o ambiente de execução e ative sua virtualenv se quiser.
2. Verifique a resolução do monitor.
3. Se necessário, use `auxiliar.py` ou `pegar_posicao.py` para capturar coordenadas de clique corretas.
4. Execute:

```bash
python codigo.py
```

## Atenção / Recomendações

- A automação depende de posições de clique fixas na tela. Se o layout ou a resolução mudar, será necessário ajustar os valores `x` e `y` no código.
- Para interromper o `pyautogui`, mova o cursor para o canto superior esquerdo da tela (0,0).
- Não execute o script enquanto estiver usando o computador para outras tarefas, pois ele controla o mouse e o teclado.

## Melhorias Possíveis

- Substituir coordenadas fixas por detecção de imagens ou elementos visuais.
- Usar tratamento de exceções para detectar quando o site não carrega corretamente.
- Tornar usuário e senha parâmetros de configuração.
- Ler outros formatos de base de dados, como Excel (`.xlsx`).

## Referências

- `pyautogui` documentation: https://pyautogui.readthedocs.io
- `pandas` documentation: https://pandas.pydata.org

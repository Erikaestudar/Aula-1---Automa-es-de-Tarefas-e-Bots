# Documentação do Projeto

## Descrição

Este projeto é um exemplo de automação de tarefas com Python voltado para cadastro de produtos em um sistema web. Ele demonstra o uso de `pyautogui` para controlar o mouse e o teclado, e `pandas` para ler dados de uma planilha CSV.

## Objetivo

Automatizar o processo repetitivo de cadastro de produto a partir de uma base de dados, reduzindo o trabalho manual e garantindo consistência no preenchimento dos campos.

## Componentes Principais

### `codigo.py`

- Script principal.
- Abre o navegador e acessa a URL de login.
- Faz login automático.
- Lê `produtos.csv` usando `pandas`.
- Preenche os campos do formulário do sistema com os valores de cada produto.
- Pressiona `Enter` para submeter cada produto.

### `auxiliar.py`

- Script auxiliar para capturar coordenadas de tela.
- Utiliza `pyautogui.position()` para mostrar onde o mouse está posicionado.
- Ajuda a ajustar as coordenadas de clique do script principal.

### `pegar_posicao.py`

- Versão simplificada de captura de posição.
- Aguarda 5 segundos e imprime a posição atual do mouse.

### `gabarito.py`

- Exemplo estruturado com comentários e passos organizados.
- Serve como roteiro para entendimento da automação.

## Requisitos

- Python 3.8+ recomendado.
- Bibliotecas:
  - `pyautogui`
  - `pyperclip`
  - `pandas`

## Instalação

```bash
pip install pyautogui pyperclip pandas
```

## Configuração

1. Abra `codigo.py` e verifique as coordenadas de clique (`x`, `y`).
2. Ajuste as coordenadas quando necessário usando `auxiliar.py`.
3. Confirme o caminho e formato de `produtos.csv`.
4. Caso utilize uma senha diferente, altere o valor no script.

## Execução

No diretório do projeto, execute:

```bash
python codigo.py
```

## Observações Importantes

- A automação é sensível à interface do site e ao posicionamento dos campos.
- Alterações no layout do site podem quebrar a execução.
- Evite mover manualmente o mouse durante a execução.
- Para parar o script, leve o mouse ao canto superior esquerdo da tela.

## Uso no GitHub

Este arquivo pode ser usado como documentação complementar no GitHub. Ele explica o propósito do projeto, o funcionamento interno e como preparar o ambiente.

### Sugestão de Publicação

- Adicione `README.md` como página inicial do repositório.
- Inclua `DOCUMENTACAO.md` como material de referência para usuários e avaliadores.
- Se desejar, crie um `docs/` com versões traduzidas ou guias adicionais.

## Possíveis Extensões

- criar interface de configuração para credenciais e URLs;
- validar se o site carregou antes de digitar;
- registrar logs de cada produto cadastrado;
- tratar casos de erro como campos obrigatórios vazios ou falha de rede.

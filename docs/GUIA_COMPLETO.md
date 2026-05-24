# Guia Completo de Uso

## Introdução

Este guia oferece instruções passo a passo para executar o projeto de automação de cadastro de produtos. Siga cada etapa cuidadosamente para garantir o funcionamento correto.

## Pré-requisitos

### Sistema Operacional

- Windows 7 ou superior
- Resolução de tela: 1920x1080 (recomendado)

### Software Necessário

- **Python 3.8 ou superior** instalado no sistema
- **Google Chrome** instalado e funcionando
- **Gerenciador de pacotes pip** (incluído com Python)

### Verificar Instalação do Python

Abra o PowerShell ou Command Prompt e execute:

```bash
python --version
```

Se retornar a versão do Python, a instalação está correta. Caso contrário, baixe em [python.org](https://www.python.org).

## Passo 1: Preparar o Ambiente

### 1.1 Clonar ou Baixar o Repositório

Se o projeto está no GitHub:

```bash
git clone <URL-DO-REPOSITORIO>
cd <nome-do-diretorio>
```

Se for um arquivo ZIP, extraia para uma pasta de sua escolha e navegue até ela.

### 1.2 Criar Ambiente Virtual (Recomendado)

Em sistemas Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Em sistemas macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.3 Instalar Dependências

Com o ambiente virtual ativado, instale as bibliotecas:

```bash
pip install pyautogui pyperclip pandas
```

Caso tenha problemas, instale também:

```bash
pip install pillow
```

Verifique a instalação:

```bash
pip list
```

Você deve ver `pyautogui`, `pyperclip` e `pandas` na lista.

## Passo 2: Preparar Dados

### 2.1 Estrutura do Arquivo CSV

O arquivo `produtos.csv` deve conter as colunas exatas:

```
codigo,marca,tipo,categoria,preco_unitario,custo,obs
```

### 2.2 Formato dos Dados

Exemplo válido:

```csv
MOLO000251,Logitech,Mouse,1,25.95,6.50,
MOLO000192,Logitech,Mouse,2,19.95,5.00,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,Conferir estoque
```

**Regras importantes:**

- `codigo`: identificador único (texto/números)
- `marca`: nome do fabricante (texto)
- `tipo`: tipo de produto (texto)
- `categoria`: categoria ou versão (número ou texto)
- `preco_unitario`: preço de venda (número decimal com ponto)
- `custo`: custo do produto (número decimal com ponto)
- `obs`: observações opcionais (pode estar vazio)

### 2.3 Validar o CSV

Abra o arquivo em Excel ou abra o Python e execute:

```python
import pandas as pd
df = pd.read_csv("produtos.csv")
print(df.head())
print(df.info())
```

Isso mostrará os primeiros 5 produtos e o tipo de dados.

## Passo 3: Ajustar Coordenadas de Clique

Este é o passo mais importante. As coordenadas variam conforme a resolução da tela.

### 3.1 Capturar Coordenadas

Execute o script auxiliar:

```bash
python auxiliar.py
```

O script aguardará 5 segundos. Dentro desse tempo:

1. Posicione o mouse sobre o ponto desejado.
2. Deixe o script terminar.
3. As coordenadas (x, y) serão exibidas no terminal.

### 3.2 Localizar os Campos Necessários

Você precisa das coordenadas dos seguintes elementos na página de cadastro:

1. **Campo de Código** - onde o código do produto é digitado
2. **Botão de Envio** - onde você clica para registrar o produto

### 3.3 Atualizar o Código

Abra `codigo.py` e localize estas linhas:

```python
pyautogui.click(x=865, y=394)  # Clique do campo de código
```

Substitua pelos valores capturados:

```python
pyautogui.click(x=<SUA_COORDENADA_X>, y=<SUA_COORDENADA_Y>)
```

**Importante:** As coordenadas no exemplo podem não funcionar em sua tela. Capture sempre os valores específicos do seu ambiente.

## Passo 4: Testar a Automação

### 4.1 Teste Rápido (Recomendado)

Antes de rodar a automação completa, teste com apenas um produto:

1. Crie um arquivo `teste.csv` com uma única linha:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
TEST001,Marca,Tipo,1,10.00,5.00,Teste
```

2. Modifique `codigo.py` para ler `teste.csv`:

```python
table = pd.read_csv("teste.csv")
```

3. Execute:

```bash
python codigo.py
```

4. Observe se funciona corretamente.

### 4.2 Teste com Múltiplos Produtos

Se o teste com um produto funcionou:

1. Restaure a leitura do `produtos.csv` original.
2. Modifique `codigo.py` para processar apenas as 3 primeiras linhas:

```python
for line in table.index[:3]:  # Apenas 3 primeiros
```

3. Execute novamente.

### 4.3 Execução Completa

Quando tudo estiver funcionando:

```bash
python codigo.py
```

## Passo 5: Executar em Background (Opcional)

Se quiser rodar o script sem ocupar o terminal:

No Windows, crie um arquivo `executar.bat`:

```batch
@echo off
python codigo.py
pause
```

Clique duas vezes no arquivo `.bat`.

## Pausar ou Interromper a Execução

### Parada de Emergência

Se o script sair do controle:

1. **Leve o mouse para o canto superior esquerdo da tela** (posição 0,0).
2. `pyautogui` detectará e pausará automaticamente.

Ou:

1. Pressione `Ctrl + C` no terminal.
2. O script será interrompido imediatamente.

## Troubleshooting Rápido

| Problema                                           | Solução                                                    |
| -------------------------------------------------- | ---------------------------------------------------------- |
| "ModuleNotFoundError: No module named 'pyautogui'" | Execute `pip install pyautogui`                            |
| Cliques acontecem no lugar errado                  | Recapture as coordenadas com `auxiliar.py`                 |
| Site não carrega                                   | Aumente o `time.sleep()` após abrir o navegador            |
| Campos não são preenchidos                         | Confirme que o campo está ativo (clicado) antes de digitar |
| Erro de autenticação                               | Verifique e-mail e senha no código                         |

Para problemas mais detalhados, consulte [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Próximas Etapas

Depois de dominar a automação básica, você pode:

1. Adicionar tratamento de erros
2. Implementar logging de execução
3. Parametrizar credenciais em arquivo `.env`
4. Usar web scraping com Selenium para mais robustez

Consulte os arquivos de documentação adicional para mais detalhes.

# Estrutura do Projeto

Documentação detalhada de cada arquivo e componente do projeto.

## Arquitetura Geral

```
projeto-automacao/
│
├── README.md                           # Descrição geral
├── DOCUMENTACAO.md                     # Documentação principal
│
├── codigo.py                           # Script principal
├── auxiliar.py                         # Capturador de coordenadas
├── pegar_posicao.py                    # Alternativa simplificada
├── gabarito.py                         # Versão de referência
│
├── produtos.csv                        # Base de dados
│
└── docs/                               # Documentação detalhada
    ├── GUIA_COMPLETO.md               # Passo a passo
    ├── CONFIGURACAO_COORDENADAS.md    # Ajuste de coordenadas
    ├── TROUBLESHOOTING.md             # Resolução de problemas
    └── ESTRUTURA_PROJETO.md           # Este arquivo
```

## Descrição dos Arquivos

### `codigo.py` - Script Principal

**Responsabilidade:** Executar toda a automação de cadastro de produtos.

**Fluxo de Execução:**

```
1. Inicializa pyautogui.PAUSE
2. Define a URL de login
3. Abre o navegador Chrome
4. Navega para o site de login
5. Faz login com credenciais
6. Carrega produtos.csv
7. Para cada produto:
   a. Clica no campo de código
   b. Preenche todos os campos
   c. Submete o formulário
   d. Volta ao topo da página
8. Fim
```

**Principais Funções/Métodos Usados:**

```python
pyautogui.press("win")              # Abre menu iniciar
pyautogui.write("chrome")           # Digita "chrome"
pyautogui.press("enter")            # Pressiona Enter
pyautogui.click(x, y)               # Clica em coordenadas
pyautogui.write("texto")            # Digita texto
pyautogui.press("tab")              # Navega entre campos
pyautogui.press("enter")            # Submete formulário
pyautogui.scroll(5000)              # Faz scroll para cima
```

**Variáveis Importantes:**

```python
pyautogui.PAUSE = 0.5               # Pausa entre ações
link = "https://..."                # URL do sistema
login = "email@..."                 # E-mail de autenticação
table = pd.read_csv(...)            # DataFrame de produtos
```

**Como Modificar:**

- Alterar credenciais: encontre as variáveis `login` e senha
- Alterar URL: modifique a variável `link`
- Ajustar velocidade: altere `pyautogui.PAUSE`
- Ajustar coordenadas: use `auxiliar.py` e atualize os valores `pyautogui.click(x=..., y=...)`

### `auxiliar.py` - Capturador de Coordenadas

**Responsabilidade:** Capturar a posição exata do mouse na tela.

**Uso:**

```bash
python auxiliar.py
```

**Tempo de Espera:** 5 segundos

**Saída:** Exibe as coordenadas (x, y) onde o mouse estava posicionado

**Código Principal:**

```python
import time
import pyautogui

time.sleep(5)
print(pyautogui.position())  # Retorna (x, y)
```

**Quando Usar:**

1. Configurar coordenadas de clique pela primeira vez
2. Trocar de monitor ou resolução
3. Alterar o zoom do navegador
4. Precisar ajustar pontos específicos

### `pegar_posicao.py` - Alternativa Simplificada

**Responsabilidade:** Mesmo que `auxiliar.py`, forma alternativa.

**Diferença:** Usa `scroll()` adicional para teste.

**Quando Usar:** Se `auxiliar.py` não funcionar por algum motivo.

### `gabarito.py` - Versão de Referência

**Responsabilidade:** Mostrar a estrutura ideal da automação com comentários.

**Uso:** Consulta e aprendizado.

**Diferenças de `codigo.py`:**

- Mais comentários explicativos
- Passos numerados (Passo 1, 2, 3...)
- Estrutura mais organizada
- Pode ter coordenadas diferentes

**Quando Usar:**

1. Para entender a lógica geral
2. Como referência ao refatorar `codigo.py`
3. Para aprender boas práticas
4. Se `codigo.py` ficar corrompido, use como base para recriar

### `produtos.csv` - Base de Dados

**Responsabilidade:** Armazenar os dados dos produtos a cadastrar.

**Formato:** Comma-Separated Values (CSV)

**Estrutura:**

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,Conferir estoque
```

**Colunas:**

| Coluna | Tipo | Exemplo | Obrigatória |
|--------|------|---------|-------------|
| `codigo` | String | MOLO000251 | Sim |
| `marca` | String | Logitech | Sim |
| `tipo` | String | Mouse | Sim |
| `categoria` | String/Int | 1 | Sim |
| `preco_unitario` | Float | 25.95 | Sim |
| `custo` | Float | 6.50 | Sim |
| `obs` | String | Conferir estoque | Não (pode estar vazio) |

**Como Adicionar Produtos:**

1. Abra `produtos.csv` em Excel ou editor de texto
2. Adicione uma nova linha
3. Preencha os dados conforme o formato
4. Salve o arquivo

**Como Criar de Novo:**

```python
import pandas as pd

dados = {
    'codigo': ['NOVO001', 'NOVO002'],
    'marca': ['Marca A', 'Marca B'],
    'tipo': ['Tipo X', 'Tipo Y'],
    'categoria': [1, 2],
    'preco_unitario': [10.00, 20.00],
    'custo': [5.00, 10.00],
    'obs': ['', 'Observação']
}

df = pd.DataFrame(dados)
df.to_csv('produtos.csv', index=False)
```

## Fluxo de Dados

```
produtos.csv
    ↓
pandas.read_csv()
    ↓
DataFrame (table)
    ↓
for linha in table.index:
    ↓
pega valores: codigo, marca, tipo, categoria, preco_unitario, custo, obs
    ↓
pyautogui digita/clica
    ↓
Site recebe dados
    ↓
Produto cadastrado
```

## Configurações Importantes

### `pyautogui.PAUSE`

```python
pyautogui.PAUSE = 0.5  # 500ms entre ações
```

**Propósito:** Dar tempo ao sistema de processar cada ação.

**Ajustes:**
- `0.3`: Muito rápido (pode falhar)
- `0.5`: Padrão (equilibrado)
- `1.0`: Lento (mais confiável, mas demora mais)

### Coordenadas de Clique

Cada clique precisa de coordenadas específicas:

```python
# Campo de código
pyautogui.click(x=865, y=394)

# Após cada campo, Tab para ir ao próximo:
pyautogui.press("tab")
```

**Mapa de Campos (aproximado):**

1. Código → `click(x=865, y=394)`
2. Marca → `press("tab")`
3. Tipo → `press("tab")`
4. Categoria → `press("tab")`
5. Preço → `press("tab")`
6. Custo → `press("tab")`
7. Obs → `press("tab")`
8. Enviar → `press("enter")`

### URLs e Credenciais

```python
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "pythonimpressionador@gmail.com"
# senha está hardcoded no código (não recomendado para produção)
```

## Dependências do Projeto

### Python
- Versão: 3.8+
- Download: https://www.python.org

### Bibliotecas
- **pyautogui**: Controla mouse e teclado
- **pyperclip**: Acessa área de transferência
- **pandas**: Manipula arquivos CSV

### Instalação

```bash
pip install pyautogui pyperclip pandas pillow
```

### Sistema Operacional
- Windows 7 ou superior
- Screen resolution: 1920x1080 (recomendado)

## Extensões Possíveis

### 1. Usar Selenium (Mais Robusto)

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(link)
# Localize elementos com XPath ou CSS
elemento = driver.find_element("id", "campo_codigo")
elemento.send_keys("NOVO001")
```

### 2. Adicionar Logging

```python
import logging

logging.basicConfig(filename='automacao.log', level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Iniciando processo")
logger.error("Erro ao fazer login")
```

### 3. Tratamento de Erros

```python
try:
    pyautogui.click(x, y)
except Exception as e:
    print(f"Erro: {e}")
    # Continua ou interrompe
```

### 4. Arquivo de Configuração

```python
# config.py
CONFIG = {
    "SITE_URL": "https://...",
    "EMAIL": "usuario@email.com",
    "SENHA": "senha",
    "PAUSAR_ENTRE_ACOES": 0.5
}
```

### 5. Interface Gráfica

```python
import tkinter as tk

def iniciar_automacao():
    # Rodar codigo.py
    pass

root = tk.Tk()
tk.Button(root, text="Iniciar", command=iniciar_automacao).pack()
root.mainloop()
```

## Checklist para Novo Desenvolvedor

- [ ] Python 3.8+ instalado
- [ ] Bibliotecas instaladas (`pip install ...`)
- [ ] Arquivo `produtos.csv` existe e tem dados
- [ ] Coordenadas capturadas com `auxiliar.py`
- [ ] `codigo.py` atualizado com coordenadas corretas
- [ ] Credenciais verificadas
- [ ] Teste com 1 produto (OK)
- [ ] Teste com 3 produtos (OK)
- [ ] Execução completa
- [ ] Logs ou screenshots capturados para análise

## Perguntas Frequentes

**P: Posso rodar em MacOS/Linux?**  
R: Parcialmente. `pyautogui` funciona, mas as coordenadas e ações específicas podem variar.

**P: E se o site mudar?**  
R: Será necessário ajustar as coordenadas e possivelmente o fluxo de cliques.

**P: Como faço backup dos dados?**  
R: Copie `produtos.csv` ou use Git para versionamento.

**P: Posso usar outro navegador?**  
R: Sim, altere o `pyautogui.write("chrome")` para outro navegador disponível.

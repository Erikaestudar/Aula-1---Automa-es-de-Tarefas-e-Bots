# Resolução de Problemas (Troubleshooting)

Guia para diagnosticar e resolver problemas comuns ao executar a automação.

## Problemas de Instalação

### "python: comando não encontrado" ou "python is not recognized"

**Diagnóstico:**
```bash
python --version
```

**Solução:**
1. Reinstale Python em https://www.python.org
2. Durante a instalação, **MARQUE** a opção "Add Python to PATH"
3. Reinicie o computador
4. Tente novamente

### "No module named 'pyautogui'"

**Causa:** As bibliotecas não foram instaladas corretamente.

**Solução:**

```bash
# Ativar ambiente virtual (se usar)
venv\Scripts\activate

# Instalar novamente
pip install pyautogui pyperclip pandas --upgrade

# Verificar instalação
pip list | findstr pyautogui
```

Se ainda não funcionar:

```bash
# Desinstalar e reinstalar
pip uninstall pyautogui -y
pip install pyautogui
```

### "No module named 'pandas'"

**Solução:**

```bash
pip install pandas --upgrade
```

### "No module named 'pillow'"

Às vezes, `pyautogui` precisa de `pillow`:

```bash
pip install pillow
```

## Problemas Durante a Execução

### O Script Não Inicia

**Verificar:**
1. O arquivo `codigo.py` existe?
2. Está no diretório correto?
3. A sintaxe Python está correta?

**Testar:**

```bash
python -m py_compile codigo.py
```

Se não houver erro, o arquivo está válido.

### O Navegador Não Abre

**Causa:** Chrome não está instalado ou não está no PATH.

**Verificar:**
```bash
where chrome
```

**Solução:**

1. Instale o Google Chrome em https://www.google.com/chrome
2. Ou altere o código para usar outro navegador:

```python
# Para Firefox:
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
```

### O Site Não Carrega

**Causa:** Tempo de espera insuficiente.

**Solução:**

Aumente o `time.sleep()` após abrir o navegador:

```python
# De:
time.sleep(3)

# Para:
time.sleep(5)  # ou mais se necessário
```

### Cliques Acontecem no Lugar Errado

**Causa:** Coordenadas incorretas para sua resolução de tela.

**Solução:**

1. Abra arquivo `auxiliar.py`
2. Execute para capturar as coordenadas corretas
3. Atualize `codigo.py` com os novos valores

```python
# Teste primeiro:
pyautogui.moveTo(x, y)
time.sleep(2)
# Veja se o mouse vai ao lugar certo antes de clicar
```

### Campos Não São Preenchidos Corretamente

**Causa 1:** Campo não está ativado (não foi clicado antes).

**Solução:**

```python
pyautogui.click(x=960, y=540)  # Clicar no campo
time.sleep(0.2)  # Aguardar ativação
pyautogui.write("texto")  # Escrever
```

**Causa 2:** Velocidade muito rápida.

**Solução:**

Aumente o `pyautogui.PAUSE`:

```python
# De:
pyautogui.PAUSE = 0.5

# Para:
pyautogui.PAUSE = 1.0  # Mais lento = mais confiável
```

**Causa 3:** Campo contém caracteres especiais ou números decimais.

**Solução:**

Use `pyperclip` para colar em vez de digitar:

```python
import pyperclip

valor = "25.95"
pyperclip.copy(valor)
pyautogui.click(x=960, y=540)
pyautogui.hotkey("ctrl", "v")
```

### Erro: "FileNotFoundError: produtos.csv not found"

**Causa:** O arquivo `produtos.csv` não está no diretório correto.

**Solução:**

1. Verifique se `produtos.csv` está na mesma pasta que `codigo.py`
2. Ou especifique o caminho completo:

```python
table = pd.read_csv(r"C:\caminho\completo\produtos.csv")
```

### Erro: "KeyError: 'codigo'" ou Similar

**Causa:** O arquivo CSV não tem a coluna especificada.

**Solução:**

1. Abra `produtos.csv` em Excel
2. Verifique se as colunas estão exatamente assim:
   - `codigo`
   - `marca`
   - `tipo`
   - `categoria`
   - `preco_unitario`
   - `custo`
   - `obs`
3. Sem espaços extras, sem acentos desnecessários

Teste com:

```python
import pandas as pd
df = pd.read_csv("produtos.csv")
print(df.columns)  # Mostra os nomes das colunas
```

### Erro: "Timeout" ou Demora Excessiva

**Causa:** Site lento ou conexão lenta.

**Solução:**

Aumente os tempos de espera:

```python
# Após abrir navegador:
time.sleep(5)  # Ao invés de 3

# Após login:
time.sleep(4)  # Ao invés de 3

# Entre ações:
pyautogui.PAUSE = 1.0  # Ao invés de 0.5
```

## Problemas de Interrupção

### "O script não para ao mover mouse para (0,0)"

**Causa:** Proteção não ativada ou mouse muito rápido.

**Solução:**

Pressione `Ctrl + C` no terminal para forçar a parada:

```bash
# Terminal mostrará:
^C
KeyboardInterrupt
```

Se isso não funcionar, feche a janela do terminal ou use Task Manager.

### "Preciso parar o script meio da execução"

**Opção 1:** Parada de Emergência (mouse para 0,0)
- Leve o mouse para o **canto superior esquerdo** da tela

**Opção 2:** Terminal
- Pressione `Ctrl + C` na janela do terminal

**Opção 3:** Força Bruta
- Abra Task Manager (Ctrl + Shift + Esc)
- Procure por "Python"
- Clique em "End Task"

## Problemas de Login

### "Erro ao fazer login" ou página de erro aparece

**Causa 1:** E-mail ou senha incorretos.

**Solução:**

1. Verifique as credenciais no código:

```python
login = "pythonimpressionador@gmail.com"
```

2. Teste manualmente no navegador antes de rodar o script

**Causa 2:** Site detectou automação.

**Solução:**

1. Aumente o tempo de espera após digitar credenciais:

```python
time.sleep(2)  # Antes de clicar em login
```

2. Adicione delays aleatórios:

```python
import random
time.sleep(random.uniform(2, 4))  # Entre 2 e 4 segundos
```

## Problemas Específicos do pyautogui

### Mensagem: "WARNING: Library not found"

**Causa:** Dependência visual (pillow) não instalada.

**Solução:**

```bash
pip install pillow
```

### Movimentos de Mouse Erráticos

**Causa:** Configurações do SO interfem.

**Solução:**

1. Feche outros programas que usem mouse (jogos, programas de automação)
2. Desative aceleração do mouse em Configurações > Dispositivos > Mouse

## Problemas de CSV/Dados

### Valores Aparecem como "NaN"

**Causa:** Células vazias interpretadas como não-número.

**Verificar:**

```python
import pandas as pd
df = pd.read_csv("produtos.csv")
print(df.info())
print(df.isnull())
```

**Solução no código:**

```python
obs = str(table.loc[line, "obs"])
if obs != "nan":
    pyautogui.write(obs)
```

### Acentos ou Caracteres Especiais Não Funcionam

**Solução:**

Use `pyperclip` ao invés de `pyautogui.write()`:

```python
import pyperclip

texto = "São Paulo"
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
```

## Monitorar Execução

### Adicionar Logs para Debug

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Iniciando automação...")
logger.debug(f"Clicando em: ({x}, {y})")
logger.info(f"Produto {i} cadastrado com sucesso")
```

### Capturar Screenshot do Erro

```python
import pyautogui
import datetime

pyautogui.screenshot(f"erro_{datetime.datetime.now()}.png")
```

## Quando Pedir Ajuda

Se o problema persistir, forneça:

1. **Versão do Python:** `python --version`
2. **Versão do Windows:** `winver`
3. **Resolução da tela:** Configurações > Exibição
4. **Output do erro:** Copie a mensagem completa
5. **Log de execução:** Se tiver criado logs

## Links Úteis

- [Documentação pyautogui](https://pyautogui.readthedocs.io)
- [Documentação pandas](https://pandas.pydata.org/docs)
- [Stack Overflow - Tag pyautogui](https://stackoverflow.com/questions/tagged/pyautogui)

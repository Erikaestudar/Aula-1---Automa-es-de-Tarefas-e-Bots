# Configuração de Coordenadas

## O Que São Coordenadas?

As coordenadas (x, y) representam a posição de um ponto na tela:

- **x**: distância em pixels da borda esquerda
- **y**: distância em pixels da borda superior

Por exemplo:

- (0, 0) = canto superior esquerdo
- (960, 540) = centro da tela (em resolução 1920x1080)
- (1920, 1080) = canto inferior direito (em resolução 1920x1080)

## Por Que Precisamos de Coordenadas?

A automação precisa saber **exatamente onde clicar** na tela. Como cada monitor tem uma resolução diferente, as coordenadas variam de computador para computador.

## Método 1: Usar o Script `auxiliar.py`

### Passo a Passo

1. Abra PowerShell/Terminal no diretório do projeto.

2. Execute:

```bash
python auxiliar.py
```

3. O script aguardará 5 segundos. Durante este período:
   - Mova o mouse para o ponto desejado
   - Deixe o mouse parado

4. Após 5 segundos, o script exibirá:

```
(1234, 567)
```

Anote essas coordenadas.

### Exemplos de Campos para Capturar

#### Campo de Código do Produto

1. Abra o site de cadastro no navegador.
2. Localize o campo "Código" no formulário.
3. Execute `auxiliar.py` e coloque o mouse **dentro do campo de entrada**.
4. Anote as coordenadas exibidas.
5. Adicione ao `codigo.py`:

```python
# Encontrar esse trecho:
pyautogui.click(x=865, y=394)  # Campo de Código

# Substituir pelo seu valor:
pyautogui.click(x=1234, y=567)  # Campo de Código
```

#### Botão de Envio/Cadastro

1. Procure o botão "Enviar", "Cadastrar" ou "Confirmar".
2. Execute `auxiliar.py` e coloque o mouse **sobre o botão**.
3. Anote as coordenadas.
4. Adicione ao `codigo.py` (se necessário ajustar):

```python
# Se houver um clique específico no botão:
pyautogui.click(x=1500, y=800)  # Botão Enviar
```

> **Nota:** No código atual, o botão é acionado com `pyautogui.press("enter")`, então talvez não seja necessário capturar sua coordenada.

## Método 2: Manual com Mouse.py (Alternativa)

Se preferir uma abordagem mais interativa:

1. Instale a biblioteca:

```bash
pip install mouse
```

2. Crie um script `capturar_mouse.py`:

```python
import mouse
import time

print("Mova o mouse para o ponto desejado e pressione ESPAÇO")
print("Pressione ESC para sair\n")

try:
    while True:
        if mouse.is_pressed('space'):
            x, y = mouse.get_position()
            print(f"Coordenadas capturadas: ({x}, {y})")
            time.sleep(0.5)

        if mouse.is_pressed('esc'):
            break
except KeyboardInterrupt:
    print("Captura interrompida")
```

3. Execute:

```bash
python capturar_mouse.py
```

## Método 3: Usando Inspetor de Elementos (Web)

Se o site usa formulários HTML padrão, você pode:

1. Abra o navegador.
2. Pressione `F12` para abrir o Inspetor de Elementos.
3. Use o seletor para identificar o elemento desejado.
4. Anote o `id`, `name` ou `class`.

Isso ajuda a entender melhor a estrutura do site (informação complementar).

## Verificar as Coordenadas

Após capturar e adicionar ao código:

1. Crie um script de teste `teste_clique.py`:

```python
import pyautogui
import time

# Suas coordenadas
x_campo = 1234
y_campo = 567

print("Movendo mouse para a coordenada...")
pyautogui.moveTo(x_campo, y_campo)
time.sleep(2)

print("Clicando...")
pyautogui.click()
time.sleep(1)

print("Teste concluído")
```

2. Execute:

```bash
python teste_clique.py
```

3. Verifique se o mouse vai para o lugar correto.

## Casos Especiais

### Campo de E-mail no Login

Geralmente é um campo text:

```python
pyautogui.click(x=960, y=540)  # Campo de e-mail
time.sleep(0.3)
pyautogui.write("seu_email@exemplo.com")
pyautogui.press("tab")  # Ir para próximo campo
```

### Campo de Senha

Vem logo após o e-mail:

```python
pyautogui.write("sua_senha")
pyautogui.press("tab")  # Ir para próximo campo (botão)
```

### Botão de Login

Pode ser clicado ou acionado com Enter:

```python
# Opção 1: Clique direto
pyautogui.click(x=955, y=638)

# Opção 2: Usando Enter (se o campo de senha está ativo)
pyautogui.press("enter")
```

## Problemas Comuns e Soluções

### Problema: Coordenadas "Saltam" Após Atualizar

**Causa:** Zoom do navegador alterado

**Solução:**

1. Pressione `Ctrl + 0` no navegador para resetar o zoom a 100%
2. Recapture as coordenadas

### Problema: Script Clica no Lugar Errado

**Causa:**

- Resolução da tela mudou
- Janela do navegador foi movida
- Zoom alterado

**Solução:**

1. Maximize a janela do navegador
2. Confirme a resolução em Configurações > Exibição
3. Recapture as coordenadas

### Problema: Coordenadas São Números Muito Grandes

**Causa:** Você pode estar em um monitor secundário ou ter múltiplos monitores

**Solução:**

1. Execute a automação no monitor principal
2. Ou adapte o código para detectar o monitor

## Dicas Finais

- ✅ **Sempre** recapture coordenadas se a resolução ou zoom mudar
- ✅ Capture coordenadas **no centro** dos elementos, não na borda
- ✅ Deixe uma margem de segurança (pelo menos 10 pixels do centro)
- ✅ Teste sempre com um produto antes de rodar em lote
- ❌ Não confie em coordenadas capturadas em outro computador

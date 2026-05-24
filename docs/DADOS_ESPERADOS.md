# Formato de Dados Esperados

Guia detalhado sobre o formato esperado do arquivo `produtos.csv` e como preparar seus dados.

## Estrutura do CSV

### Cabeçalho Obrigatório

O arquivo **deve** conter exatamente estas colunas na primeira linha:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
```

**Importante:**

- Sem espaços extras ao redor dos nomes
- Sem acentos
- Maiúsculas/minúsculas como mostrado
- Ordem exata (não pode mudar)

### Validação de Cabeçalho

Para verificar se o cabeçalho está correto:

```python
import pandas as pd

df = pd.read_csv("produtos.csv")
print(df.columns.tolist())
# Esperado: ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs']
```

## Descrição das Colunas

### 1. `codigo` (String)

**Descrição:** Identificador único do produto

**Tipo:** Texto ou números (aceita ambos)

**Exemplos válidos:**

- `MOLO000251`
- `123456`
- `NOVO-001`
- `SKU_MOUSE_001`

**Exemplos inválidos:**

- (deixar em branco)
- `NULL`
- `nan`

**Comprimento:** Sem limite, mas recomenda-se até 50 caracteres

**Como preencher:**

```csv
codigo
MOLO000251
CAHA000251
BOHA000252
```

### 2. `marca` (String)

**Descrição:** Nome do fabricante ou produtor

**Tipo:** Texto simples

**Exemplos válidos:**

- `Logitech`
- `Hashtag`
- `Samsung`
- `LG`
- `Multilaser`
- `Apple`

**Exemplos inválidos:**

- (deixar em branco)
- `123` (números puros não recomendados)

**Comprimento:** Até 100 caracteres recomendado

**Como preencher:**

```csv
marca
Logitech
Hashtag
Samsung
```

### 3. `tipo` (String)

**Descrição:** Tipo/Categoria do produto

**Tipo:** Texto simples

**Exemplos válidos:**

- `Mouse`
- `Camisa`
- `Televisao`
- `Teclado`
- `Monitor`
- `Bone`

**Comprimento:** Até 50 caracteres recomendado

**Como preencher:**

```csv
tipo
Mouse
Camisa
Televisao
```

### 4. `categoria` (String ou Número)

**Descrição:** Subcategoria ou variante do produto

**Tipo:** Número (1, 2, 3...) ou Texto

**Exemplos válidos (numéricos):**

- `1`
- `2`
- `3`
- `5`

**Exemplos válidos (textuais):**

- `Preto`
- `Branco`
- `Grande`
- `Premium`

**Recomendação:** Use números para melhor compatibilidade

**Como preencher (numéricos):**

```csv
categoria
1
2
3
1
```

**Como preencher (textuais):**

```csv
categoria
Preto
Branco
Grande
```

### 5. `preco_unitario` (Float/Decimal)

**Descrição:** Preço de venda unitário

**Tipo:** Número decimal

**Formato:** Use **PONTO** como separador decimal (não vírgula)

**Exemplos válidos:**

- `25.95`
- `100.00`
- `19.99`
- `1250.50`

**Exemplos inválidos:**

- `25,95` (vírgula - será interpretado como separador CSV)
- `25` (falta casas decimais, mas funciona)
- `R$ 25.95` (caracteres não numéricos)

**Faixa recomendada:** 0.01 até 999999.99

**Como preencher:**

```csv
preco_unitario
25.95
19.95
25.00
820.00
```

### 6. `custo` (Float/Decimal)

**Descrição:** Custo unitário de compra

**Tipo:** Número decimal

**Formato:** Use **PONTO** como separador decimal

**Exemplos válidos:**

- `6.50`
- `5.00`
- `172.20`
- `3000.00`

**Exemplos inválidos:**

- `6,50` (vírgula)
- Deixar em branco (se usado no cálculo de margem)

**Recomendação:** Sempre menor ou igual ao `preco_unitario`

**Como preencher:**

```csv
custo
6.50
5.00
11.00
172.20
```

### 7. `obs` (String - OPCIONAL)

**Descrição:** Observações ou anotações sobre o produto

**Tipo:** Texto simples ou vazio

**Exemplos válidos:**

- (deixar vazio)
- `Conferir estoque`
- `Troca de fornecedor`
- `Promoção até 30/04`
- `Necessita calibragem`

**Exemplos inválidos:**

- Nenhum (pode estar vazio)

**Limite:** Até 500 caracteres recomendado

**Como preencher:**

```csv
obs
(deixar vazio)
Conferir estoque
(deixar vazio)
Troca de fornecedor
```

## Exemplo Completo

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
MOLO000192,Logitech,Mouse,2,19.95,5.00,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,Conferir estoque
CAHA000252,Hashtag,Camisa,2,25.00,11.00,
MOMU000111,Multilaser,Mouse,1,11.99,3.40,
BOHA000251,Hashtag,Bone,1,25.00,11.00,
TELG000821,LG,Televisao,1,820.00,172.20,
TESA000125,Samsung,Televisao,5,1260.00,378.00,Equipamento premium
```

## Criando o CSV do Zero

### Opção 1: Excel

1. Crie uma nova planilha
2. Na primeira linha, escreva os cabeçalhos:
   - A1: `codigo`
   - B1: `marca`
   - C1: `tipo`
   - D1: `categoria`
   - E1: `preco_unitario`
   - F1: `custo`
   - G1: `obs`

3. Preencha os dados a partir de A2
4. Salve como **CSV UTF-8** (arquivo > salvar como > tipo CSV)
5. Se perguntado sobre formato, escolha "CSV"

### Opção 2: Editor de Texto

1. Abra Bloco de Notas
2. Escreva:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
PROD001,Marca,Tipo,1,10.00,5.00,
PROD002,Marca,Tipo,2,15.00,7.50,Observacao
```

3. Salve com extensão `.csv`
4. **Importante:** Salve como UTF-8 ou ANSI (não Unicode)

### Opção 3: Python/Pandas

```python
import pandas as pd

dados = {
    'codigo': ['NOVO001', 'NOVO002', 'NOVO003'],
    'marca': ['Marca A', 'Marca B', 'Marca C'],
    'tipo': ['Tipo X', 'Tipo Y', 'Tipo Z'],
    'categoria': [1, 2, 1],
    'preco_unitario': [10.00, 20.00, 15.00],
    'custo': [5.00, 10.00, 7.50],
    'obs': ['', 'Observacao', '']
}

df = pd.DataFrame(dados)
df.to_csv('produtos.csv', index=False)
print("Arquivo criado com sucesso!")
```

## Validação de Dados

### Script de Verificação

```python
import pandas as pd

# Ler arquivo
df = pd.read_csv('produtos.csv')

# Verificar colunas
colunas_esperadas = ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs']
if list(df.columns) != colunas_esperadas:
    print("❌ Colunas incorretas!")
    print(f"Esperado: {colunas_esperadas}")
    print(f"Obtido: {list(df.columns)}")
else:
    print("✅ Colunas corretas")

# Verificar linhas
print(f"Total de produtos: {len(df)}")

# Verificar campos obrigatórios vazios
campos_obrigatorios = ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo']
for campo in campos_obrigatorios:
    vazios = df[campo].isnull().sum()
    if vazios > 0:
        print(f"⚠️  Campo '{campo}' tem {vazios} linhas vazias")
    else:
        print(f"✅ Campo '{campo}' OK")

# Verificar tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

# Mostrar primeiras linhas
print("\nPrimeiros 3 produtos:")
print(df.head(3))
```

## Problemas Comuns na Criação

### Erro: "Coluna não encontrada"

**Causa:** Nome da coluna está incorreto ou espaços extras

**Solução:**

```python
# Verificar nomes exatos
df = pd.read_csv('produtos.csv')
print(df.columns.tolist())
```

### Erro: Números decimais com vírgula

**Causa:** Arquivo salvo em região que usa vírgula

**Solução:**

```python
# Substituir vírgula por ponto
df = pd.read_csv('produtos.csv')
df['preco_unitario'] = df['preco_unitario'].astype(str).str.replace(',', '.')
df['custo'] = df['custo'].astype(str).str.replace(',', '.')
df.to_csv('produtos.csv', index=False)
```

### Erro: Linhas em branco ou caracteres especiais

**Causa:** Espaços extras ou encoding incorreto

**Solução:**

```python
# Limpar espaços e ler com encoding correto
df = pd.read_csv('produtos.csv', encoding='utf-8-sig', skipinitialspace=True)
df = df.dropna(how='all')  # Remove linhas completamente vazias
df.to_csv('produtos.csv', index=False)
```

## Importar de Outras Fontes

### De Excel (`.xlsx`)

```python
import pandas as pd

# Ler Excel
df = pd.read_excel('dados.xlsx', sheet_name='Produtos')

# Verificar colunas
print(df.columns.tolist())

# Salvar como CSV
df.to_csv('produtos.csv', index=False)
```

### De Google Sheets

1. Abra a planilha
2. Arquivo > Fazer download > CSV
3. Renomeie para `produtos.csv`
4. Valide o formato

### De Banco de Dados SQL

```python
import pandas as pd
import sqlite3

# Conectar ao banco
conn = sqlite3.connect('database.db')

# Query
query = "SELECT codigo, marca, tipo, categoria, preco_unitario, custo, obs FROM produtos"
df = pd.read_sql_query(query, conn)

# Salvar como CSV
df.to_csv('produtos.csv', index=False)
conn.close()
```

## Dicas de Melhor Prática

✅ **Faça:**

- Use pontos para decimais (25.95)
- Nomes de colunas exatamente como especificado
- Verifique se há duplicatas de código
- Mantenha backup do original

❌ **Evite:**

- Vírgulas em valores numéricos (25,95)
- Espaços extras ao redor dos dados
- Usar caracteres especiais em `codigo`
- Misturar números e texto em colunas numéricas (exceto `obs`)

## Teste Antes de Usar

Sempre execute este teste antes de rodar a automação:

```bash
python
```

```python
import pandas as pd

df = pd.read_csv('produtos.csv')
print(f"✅ Arquivo carregado com {len(df)} produtos")
print(f"✅ Colunas: {list(df.columns)}")
print(df.head(3))
```

Se funcionar sem erros, seus dados estão prontos!

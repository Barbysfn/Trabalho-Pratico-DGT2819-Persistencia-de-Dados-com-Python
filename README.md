# DGT2819 – Persistência de dados com Python

Trabalho prático **"Colocando tudo em ordem e guardando"** – Desenvolvimento Full Stack (Estácio).

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `array.sort.py` | Microatividade 1 – ordenação com o método nativo `sort` (crescente e decrescente), com números e strings |
| `bubble.sort.py` | Microatividade 2 – algoritmo Bubble Sort |
| `selection.sort.py` | Microatividade 3 – algoritmo Selection Sort |
| `ler.txt.py` + `loremipsum.txt` | Microatividade 4 – leitura de arquivo com `open` e com `with` |
| `escrever.txt.py` → `texto.txt` | Microatividade 5 – escrita de uma lista em arquivo |
| `documento.txt` | Texto de entrada do trabalho prático (termos jurídicos) |
| `kdd_comparacao.py` | Trabalho prático, etapas a–h – compara Bubble Sort, Selection Sort e `sort` |
| `kdd.py` | Trabalho prático, etapa i – versão final, só com o método escolhido |
| `palavras_ordenadas.txt` | Saída do `kdd.py`: glossário com as palavras ordenadas |

## Como executar

Requisito: Python 3 instalado. Execute os scripts a partir da pasta do projeto:

```bash
python array.sort.py
python bubble.sort.py
python selection.sort.py
python ler.txt.py
python escrever.txt.py

# Comparação de performance (todos os métodos de uma vez)
python kdd_comparacao.py

# Ou um método por vez, como pede a etapa h do roteiro
python kdd_comparacao.py bubble
python kdd_comparacao.py selection
python kdd_comparacao.py sort

# Versão final: ordena e gera palavras_ordenadas.txt
python kdd.py
```

## Resultado da comparação

Ordenando as 454 palavras do `documento.txt`:

| Método | Tempo aproximado |
|---|---|
| `sort` (nativo do Python) | ~0,0004 s |
| Bubble Sort | ~0,14 s |
| Selection Sort | ~0,14 s |

Os tempos variam de máquina para máquina, mas a diferença é sempre grande: o `sort` foi cerca de **350 vezes mais rápido**.

Isso acontece porque Bubble Sort e Selection Sort fazem uma quantidade de comparações que cresce com o quadrado do tamanho da lista (O(n²)), enquanto o `sort` do Python usa o algoritmo **Timsort** (O(n log n)), implementado em C. Por isso o `sort` foi o método escolhido para a versão final (`kdd.py`).

## Decisões de implementação

- As palavras são convertidas para minúsculas e têm a pontuação removida, para que "Contrato," e "contrato" sejam tratadas como a mesma palavra.
- A comparação ignora acentos (`chaveOrdenacao`); sem isso, palavras como "à" e "ação" iriam para o final da lista, depois do "z".
- No `kdd_comparacao.py`, cada método ordena uma **cópia** da mesma lista, para a comparação ser justa.
- O `palavras_ordenadas.txt` traz cada palavra uma única vez, já que ele é a base de um glossário.

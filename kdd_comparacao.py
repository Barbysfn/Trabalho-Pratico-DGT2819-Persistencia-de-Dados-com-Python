# Trabalho Prático | Colocando tudo em ordem e guardando
# Etapas a até h: leitura do txt, separação em palavras e comparação
# de performance entre Bubble Sort, Selection Sort e o método nativo sort.
#
# Uso:
#   python kdd_comparacao.py            -> executa os três métodos
#   python kdd_comparacao.py bubble     -> executa só o Bubble Sort
#   python kdd_comparacao.py selection  -> executa só o Selection Sort
#   python kdd_comparacao.py sort       -> executa só o sort nativo

import string
import sys
import time
import unicodedata

ARQUIVO_ENTRADA = "documento.txt"


def limparPalavra(palavra):
    """Remove pontuação das pontas e deixa a palavra em minúsculas."""
    return palavra.strip(string.punctuation + "“”‘’«»").lower()


def chaveOrdenacao(palavra):
    """Remove os acentos só para comparar, assim 'ação' fica junto de 'acordo'
    e não depois do 'z' (sem isso, letras acentuadas vão para o fim)."""
    semAcento = unicodedata.normalize("NFD", palavra)
    return "".join(c for c in semAcento if unicodedata.category(c) != "Mn")


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if chaveOrdenacao(array[j]) > chaveOrdenacao(array[j + 1]):
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


def selectionSort(array):
    for i in range(len(array)):
        indiceMenor = i
        for j in range(i + 1, len(array)):
            if chaveOrdenacao(array[indiceMenor]) > chaveOrdenacao(array[j]):
                indiceMenor = j
        array[i], array[indiceMenor] = array[indiceMenor], array[i]


def ordenarComSort(array):
    array.sort(key=chaveOrdenacao)


# a. Variável do tipo lista
palavras = list()

# b. Leitura do arquivo com "with", linha a linha
with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # c. Separa cada linha em palavras com split
        for palavra in linha.split():
            palavra = limparPalavra(palavra)
            # d. Adiciona cada palavra à lista
            if palavra:
                palavras.append(palavra)

print(f"Total de palavras lidas: {len(palavras)}\n")

# e. Métodos de ordenação a comparar
metodos = {
    "bubble": ("Bubble Sort", bubbleSort),
    "selection": ("Selection Sort", selectionSort),
    "sort": ("sort (nativo do Python)", ordenarComSort),
}

# h. Permite executar um método por vez, passando o nome na linha de comando
escolhidos = sys.argv[1:] or list(metodos.keys())

resultados = {}
for chave in escolhidos:
    nome, funcao = metodos[chave]

    # Cada método recebe uma cópia, para todos ordenarem a mesma lista original
    copia = palavras.copy()

    # g. Tempo de execução = momento final - momento inicial
    inicio = time.perf_counter()
    funcao(copia)
    fim = time.perf_counter()
    tempo = fim - inicio
    resultados[nome] = tempo

    # f. Imprime o resultado da ordenação e o tempo de execução
    print(f"===== {nome} =====")
    print(copia)
    print(f"Tempo de execução: {tempo:.6f} segundos\n")

if len(resultados) > 1:
    print("===== Resumo da comparação =====")
    for nome, tempo in sorted(resultados.items(), key=lambda item: item[1]):
        print(f"{nome:<25} {tempo:.6f} s")
    maisRapido = min(resultados, key=resultados.get)
    print(f"\nMétodo mais rápido: {maisRapido}")

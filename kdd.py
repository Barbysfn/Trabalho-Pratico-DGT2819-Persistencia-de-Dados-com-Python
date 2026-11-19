# Trabalho Prático | Colocando tudo em ordem e guardando
# Versão final (etapa i): depois de comparar a performance em
# kdd_comparacao.py, o método nativo "sort" foi o escolhido por ser o mais
# rápido. Bubble Sort e Selection Sort foram removidos deste script.

import string
import time
import unicodedata

ARQUIVO_ENTRADA = "documento.txt"
ARQUIVO_SAIDA = "palavras_ordenadas.txt"


def limparPalavra(palavra):
    """Remove pontuação das pontas e deixa a palavra em minúsculas."""
    return palavra.strip(string.punctuation + "“”‘’«»").lower()


def chaveOrdenacao(palavra):
    """Remove os acentos só para comparar, mantendo a ordem alfabética correta."""
    semAcento = unicodedata.normalize("NFD", palavra)
    return "".join(c for c in semAcento if unicodedata.category(c) != "Mn")


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

# e. Ordenação com o método escolhido: sort nativo
inicio = time.perf_counter()
palavras.sort(key=chaveOrdenacao)
fim = time.perf_counter()

# f. Impressão do resultado e do tempo de execução
print(palavras)
print(f"\nTotal de palavras: {len(palavras)}")
print(f"Tempo de execução do sort: {fim - inicio:.6f} segundos")

# i. Cria um novo txt com as palavras ordenadas (uma por linha).
#    Como é a base de um glossário, cada palavra aparece só uma vez.
glossario = list()
for palavra in palavras:
    if palavra not in glossario:
        glossario.append(palavra)

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as arquivoSaida:
    for palavra in glossario:
        arquivoSaida.write(palavra + "\n")

print(f"\nArquivo '{ARQUIVO_SAIDA}' criado com {len(glossario)} palavras únicas.")

# Microatividade 2: algoritmo de ordenação Bubble Sort


# a. Método que recebe, como parâmetro, o array a ser ordenado
def bubbleSort(array):
    # b. Primeiro laço: itera sobre os elementos do array
    for i in range(len(array)):
        # c. Segundo laço: percorre os elementos de dois em dois (adjacentes).
        #    A cada passada, o maior valor "borbulha" para o final,
        #    por isso não é preciso olhar os últimos i elementos.
        for j in range(0, len(array) - i - 1):
            # d. Se o elemento j for maior que o j+1, troca os dois de lugar
            if array[j] > array[j + 1]:
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


# e. Array de números com 15 posições
numeros = [64, 34, 25, 12, 22, 11, 90, 5, 77, 43, 18, 59, 3, 81, 37]
print("Array original:", numeros)

# f. Aplicação do método bubbleSort
bubbleSort(numeros)

# g. Impressão do array ordenado
print("Array ordenado (Bubble Sort):", numeros)

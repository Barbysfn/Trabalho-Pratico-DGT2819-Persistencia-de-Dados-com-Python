# Microatividade 3: algoritmo de ordenação Selection Sort

# a. Array populado com 15 números inteiros, sem ordenação
array = [29, 10, 14, 37, 13, 88, 2, 61, 45, 7, 99, 23, 50, 1, 72]
print("Array original:", array)

# b. Primeiro laço: itera sobre os elementos do array
for i in range(len(array)):
    # c. Variável que guarda a posição do menor elemento encontrado
    indiceMenor = i

    # d. Segundo laço: percorre do elemento i + 1 até o fim do array
    for j in range(i + 1, len(array)):
        # e. Se o elemento na posição indiceMenor for maior que o da posição j...
        if array[indiceMenor] > array[j]:
            # f. ...a posição j passa a ser a do menor elemento
            indiceMenor = j

    # g. Troca o elemento da posição i com o menor elemento encontrado
    array[i], array[indiceMenor] = array[indiceMenor], array[i]

# h. Impressão do array ordenado
print("Array ordenado (Selection Sort):", array)

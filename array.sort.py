# Microatividade 1: ordenação de um array utilizando o método nativo "sort"

# a. Array de 15 posições com números inteiros, não ordenados
numeros = [42, 7, 93, 15, 68, 3, 81, 29, 56, 11, 74, 38, 90, 22, 5]
print("Array original:", numeros)

# b. Ordenação crescente com o método sort
numeros.sort()

# c. Impressão do array ordenado de forma crescente
print("Ordem crescente:", numeros)

# d. Ordenação decrescente passando key=None e reverse=True
numeros.sort(key=None, reverse=True)

# e. Impressão do array ordenado de forma decrescente
print("Ordem decrescente:", numeros)

print()

# f. Array de strings, repetindo os passos acima
campos = ["rg", "nome", "cpf", "dataNascimento"]
print("Array de strings original:", campos)

campos.sort()
print("Ordem crescente:", campos)

campos.sort(key=None, reverse=True)
print("Ordem decrescente:", campos)

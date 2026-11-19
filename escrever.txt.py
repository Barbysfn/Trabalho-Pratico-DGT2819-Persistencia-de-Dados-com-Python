# Microatividade 5: escrita de dados em um arquivo externo

# a. Abre (e cria, já que ainda não existe) o arquivo texto.txt para escrita
arquivo = open("texto.txt", "w", encoding="utf-8")

# b. Cria uma lista usando a sintaxe list()
texto = list()

# c. Adiciona algumas frases à lista com o método append
texto.append("Python é uma linguagem versátil.\n")
texto.append("Persistir dados é guardar informações para usar depois.\n")
texto.append("Arquivos txt são uma forma simples de persistência.\n")

# d. Escreve, no arquivo aberto, o conteúdo da lista
arquivo.writelines(texto)
arquivo.close()

print("Arquivo texto.txt criado com sucesso!")

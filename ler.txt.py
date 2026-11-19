# Microatividade 4: leitura de dados a partir de um arquivo externo

# Variável que recebe, com o método open, o arquivo txt
arquivo = open("loremipsum.txt", "r", encoding="utf-8")
conteudo = arquivo.read()

# Imprime todo o conteúdo do arquivo
print("=== Conteúdo completo ===")
print(conteudo)

# Imprime apenas a primeira linha
print("=== Primeira linha ===")
print(conteudo.splitlines()[0])

# Imprime apenas os 3 primeiros caracteres
print("=== 3 primeiros caracteres ===")
print(conteudo[:3])

# Fecha o arquivo aberto sem o "with"
arquivo.close()

# Agora com a instrução "with": o arquivo é fechado automaticamente
print("\n=== Leitura usando with ===")
with open("loremipsum.txt", "r", encoding="utf-8") as arquivoWith:
    conteudoWith = arquivoWith.read()
print(conteudoWith)

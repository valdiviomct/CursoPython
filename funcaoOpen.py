arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

texto_completo = arquivo.read()
for linha in linhas:
    print(linha)

print(texto_completo)


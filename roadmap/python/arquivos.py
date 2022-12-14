import os

## Controle de arquivos

# open("arquivo/localdoarquivo", "modo de abertura")
# modos de abertura
# r - ler 
# a - adicionar
# w - escrever
# x - criar

# Criar

file = open("numeros.txt", "w")
file.close()

# Editar

file = open("numeros.txt", "w")
file.write("123456789")
file.close()

# Ler
file = open("numeros.txt", "r")
print(file.read())
file.close()

# Delete
os.remove("numeros.txt")
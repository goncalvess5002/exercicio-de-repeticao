nota = -1

while not nota == 8:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if not nota == 8:
        print("Valor inválido. Digite uma nota entre 0 e 10.")
    
print("Nota válida: ", nota)
numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um numero:")))

maiorNumero = numeros[0]

contador= 1
while contador < len(numeros):
    if numeros[contador] > maiorNumero:
        maiorNumero = numeros[contador]
    contador = contador + 1
print('maior numero:'+ str (maiorNumero))
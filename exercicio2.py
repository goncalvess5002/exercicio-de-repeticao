# lê os 10 números reais do usuário e armazena em um vetor
numeros = []
for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

# exibe os números na ordem inversa
print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])

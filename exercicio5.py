import random

todosOsNumeros=[]
numerosImpares= []
numeroPares= []

for i in range (20):
    todosOsNumeros.append (random.randint(0, 9))

for i in todosOsNumeros:
    if i % 2 ==  0: 
        numeroPares.append(i)
    else:
        numerosImpares.append(i)


print(todosOsNumeros)
print( 'numeros impares', numerosImpares)
print('numerospares', numeroPares)
    
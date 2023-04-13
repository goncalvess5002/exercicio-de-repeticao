idade = [66, 78, 88, 77, 20]
altura = [1.56, 1.9, 1.8, 1.2, 1.3]
alturaVazia = []
idadeVazia = []
print(idade)
print(altura)

for i in range(5):
    idadeVazia.append(idade.pop())
    alturaVazia.append(altura.pop())

print(idadeVazia)
print(alturaVazia)


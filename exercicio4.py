listadeconsoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'w', 'z']
listaADescobrie = ['a','f','h','j','e','b','p','l',]

for letra in listaADescobrie:
    for vogal in listadeconsoantes:
        if letra == vogal:
            print(letra)

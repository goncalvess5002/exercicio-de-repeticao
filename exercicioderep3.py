sexo = ['m','f']
estadocivil = ['s','c','v','d']

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de 3 caracteres!")

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18 and idade <= 200:
        break
    else:
        print("Você deve ter pelo menos 18 anos.")
        

while True:
    salario = int(input("Digite seu salario: "))
    if salario > 0 and idade <= 1000000:
        break
    else:
        print("Seu salário deve ser maior que R$0.")
        
while True:
    genero = str(input("Digite seu genero sexual (m,f): "))
    if genero in sexo:
        break
    else:
        print("Você deve escolher um dos generos apresentados.")

while True:
    estado = str(input("Digite seu estado civil (s,c,v,d): "))
    if estado in estadocivil:
        break
    else:
        print("Você deve escolher uma das opções apresentadas acima.")
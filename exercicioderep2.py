nome = []
senha = []

while nome == [] or senha == []:
    nomepessoa = str(input("Digite o nome de usuário: "))
    nome.append(nomepessoa)
    senhapessoa = str(input("Digite a senha: "))
    senha.append(senhapessoa)
    while senha == nome:
        senhapessoa = str(input("Senha invalida, a senha não pode ser o seu nome de login, digite a senha: "))
        senha = [senhapessoa]
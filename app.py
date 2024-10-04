usuarios = []

while True:
    # Dicionário
    usuario = {}
    
    # Fazendo o input para os dados do usuário
    usuario['Nome'] = input("Digite o nome: ")
    usuario['Idade'] = int(input("Digite a idade: "))
    usuario['CPF'] = input("Digite o CPF: ")
    usuario['E-mail'] = input("Digite o e-mail: ")
    usuario['Profissão'] = input("Digite a profissão: ")
    usuario['Tipo Sanguíneo'] = input("Digite o tipo sanguíneo: ")
    usuario['Peso'] = float(input("Digite o peso (kg): "))
    usuario['Altura'] = float(input("Digite a altura (m): "))
    
    # Adicionando o dicionário à lista de usuários
    usuarios.append(usuario)
    
    # Perguntando se deseja cadastrar outro usuário
    continuar = input("Deseja cadastrar outro usuário? (s/n): ")
    if continuar.lower() != 's':
        break

for usuario in usuarios:
    # Exibindo os dados de todos os usuários cadastrados
    print("\nDADOS DO USUARIO:\n")
    print(f"Nome do usuario: {usuario.get('Nome')}.")
    print(f"idade do usuario: {usuario.get('Idade')}.")
    print(f"CPF: {usuario.get('CPF')}.")
    print(f"E-mail:{usuario.get('E-mail')}.")
    print(f" profissao do usuario: {usuario.get('Profissão')}.")
    print(f" tipo sanguineo do usuario: {usuario.get('Tipo Sanguíneo')}.")
    print(f" peso do usuario: {usuario.get('Peso')}.")
    print(f" altura do usuario: {usuario.get('Altura')}.")
    print(f"\n{'-'*30}")

# for usuario in usuarios:
#     for dicionario, valor in usuario.campos():
#         print(f"{dicionario}: {valor}")
#     print()  

print("Programa encerrado")



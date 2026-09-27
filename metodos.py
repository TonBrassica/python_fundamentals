# Código para mostrar o nome de uma pessoa com a primeira letra de cada palavra maiúscula usando o método title()
name = "ada lovelace"
print(name.title())

#Código para mostrar o nome com todas as letras maiúsculas usando o método upper()
print(name.upper())

#Código para mostrar o nome com todas as letras minúsculas usando o método lower()
print(name.lower())

#Combinando Strings
First_name = "ada"
Last_name = "lovelace"
Full_name = First_name + " " + Last_name
print(Full_name.title())
print(f"Ola {Full_name.title()}! Como você está?")

#Tabulação
print("Python")
print("\tPython")
print("\t\tPython")

print("\tPython\n\tPython\tPython\nPython\tPython\tPython")

#removendo espaços em branco com o método strip()
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Lembrar de sempre usar aspas duplas para evitar problemas com apóstrofos
message = "One of Python's strengths is its diverse community."
print(message)

#Exercícios do capitulo 2

nome_completo = "ton brassica"
print(f"Olá {nome_completo.title()}, você está aprendendo Python hoje?")

print(nome_completo.upper())
print(nome_completo.lower())

citacao = "Albert Einstein certa vez disse: 'Uma pessoa que nunca cometeu um erro nunca tentou nada novo.'"
print(citacao)

famous_person = "Albert Einstein"
message = f"{famous_person} uma vez disse: 'Uma pessoa que nunca cometeu um erro nunca tentou nada novo.'"
print(message)

input_nome = input("Qual é o seu nome? ")
print(f"Olá {input_nome.strip().title()}, você está aprendendo Python hoje?")

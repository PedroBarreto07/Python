faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f'Faturamento da Empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}')

email_cliente = 'qualqueremail@gmail.com'

# maiúscula
email_cliente = email_cliente.upper()
print(email_cliente)

# minúscula
email_cliente = email_cliente.lower()
print(email_cliente)

# '@'
print(email_cliente.find('@')) # -1 quando nao encontrar

# tamanho do texto
print(len(email_cliente))

# pegar um caractere
print(email_cliente[-2])

#pegar um pedaço do texto
print(email_cliente[:13])

# trocar um pedaço do texto
novo_email = email_cliente.replace('gmail.com','hotmail.com')
print(novo_email)

nome = 'Pedro Barreto'

# Colocando as primeiras letras em maiúsculo

print(nome.capitalize()) #somente primeira letra maiúscula
print(nome.title()) # primeira letra de cada palabra maiúscula

# pegar o servidor do email
posicao_arroba = email_cliente.find('@')
servidor = email_cliente[posicao_arroba:]
print(servidor)

# pegar o 1 nome
posicao_espaco = nome.find(' ')
primeiro_nome = nome[ :posicao_espaco]
print(primeiro_nome)

# pegar o sobrenome
sobrenome = nome[posicao_espaco+1: ]
print(sobrenome)

# casos especiais - formatações númericas em texto
margem_lucro = round (margem_lucro,2)
print(f'Faturamento da Empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem de lucro: {margem_lucro:.0%}')

# inputs
email = input('Escreva seu e-mail: ')
nome = input('Seu primeiro nome: ')

print('Nome:', nome,'Email:', email)

print(f'{nome}, verifique seu email {email} para fazer a confirmação dos seus dados')

# listas
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[ :3])

lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook']

produto_procurado = input('Qual produto vc procura ? ')
produto_procurado = produto_procurado.lower()


print(produto_procurado in lista_produtos)

# adicionar um item
lista_produtos.append('apple watch')
print(lista_produtos)

# remover um item
lista_produtos.remove('apple watch')
lista_produtos.pop(2)
print(lista_produtos)

# editar um item
precos = [1500, 1600, 2100]
precos[0] = precos[0] * 1.5
print(precos)

# contar quantas vezes um item aparece na lista
lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook', 'iphone', 'ipad', 'airpod', 'ipad', 'ipad']
print(lista_produtos.count('ipade'))

# ordenar uma lista
vendas.sort(reverse = True)
print(vendas)

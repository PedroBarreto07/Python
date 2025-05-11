dic_produtos = {'airpod': 2000, 'ipad': 9000, 'iphone': 6000,'macbook': 11000}

# pegar um elemento
print(dic_produtos['airpod'])

# editar um elemento
dic_produtos['iphone'] = dic_produtos['iphone'] * 1.3

print(dic_produtos['iphone'])

# quantidade de itens
print(len(dic_produtos))

# retirar um item do dicionario
dic_produtos.pop('iphone')
print(dic_produtos)

# adicionar um item no dicionario
dic_produtos['apple watch'] = 3000
print(dic_produtos)

# verificar se um item existe no dicionario
if 'ipad' in dic_produtos:
    print('O valor do produto é: ', dic_produtos['ipad'])
else: 
    print('Produto Inexistente')

# verificar se um valor existe nos valores do dicionario
if 9000 in dic_produtos.values(): 
    print('Existe')
else: 
    print('Não existe')

# Exercício 1

nome_produto = input('Nome do produto: ')
preco_produto = input('Preço do produto: ')

nome_produto = nome_produto.lower()
preco_produto = int(preco_produto)
dic_produtos[nome_produto] = preco_produto

nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)
dic_produtos[nome_produto] = preco_produto

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)

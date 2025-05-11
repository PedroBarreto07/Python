# Comparadores no pyhon
# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == exatamente igual
# != diferente

# 1 cenário

vendas = 1500
meta = 1300


if vendas > meta:
    print('Ganhou bônus')
    print('Bateu a meta de vendas')
    bônus = vendas * 0.1
    print('Bônus do vendedor foi de :', bônus)
else:
    print('Vendedor não ganhou bônus')
    print('Não bateu a meta de vendas')

# 2 cenário

vendas = 2100
vendas_empresa = 10000
meta_empresa = 20000
meta_1 = 1300 # ganhar 10%
meta_2 = 2000 # ganhar 13 %

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bônus = vendas * 0.13
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bônus = vendas * 0.1
else:
    bônus = 0

print('O bônus ganho foi de:', bônus)

lista_produtos = ['airpod' , 'ipad', 'iphone', 'macbook']
produto_procurado = input('Escolha um produto: ')
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print('Produto no estoque')
else: 
    print('Produto fora de estoque')

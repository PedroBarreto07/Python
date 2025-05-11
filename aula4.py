lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta:
        bônus = venda * percentual_bonus
    else: 
        bônus = 0
    print(bônus)

lista_precos = [1500, 1000, 800, 3000]

# aliquota1 - IR = 0.2
# aliquota2 - ISS = 0.15
# aliquota3 - CSLL = 0.05

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = preco * 0.2
    else:
        imposto_ir = preco * 0.3
    imposto_iss = preco * 0.15
    imposto_csll = preco * 0.05
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f'O imposto total sobre o produto de R${preco} foi de R${imposto_total}')

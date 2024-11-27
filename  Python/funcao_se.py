Vendas = 1500
meta = 2000

# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente

if Vendas >= meta: 
    print("Vendedor ganhou bonus")
    print("Bateu a meta de vendas")
    bonus = 0.1 * vendas 
    print("Bonus do vendedor: ", bonus)
else:
    print("Vendedor não ganhou bonus")
    print("Não bateu a meta de vendas")

print("Acabou o programa")
# Segundo programa

Vendas = 2500
Meta1 = 1300 # Ganha 10%
Meta2 = 2000 # Ganha 13%

if Vendas >= 2000:
    bonus = 0.13 * Vendas
else:
    if Vendas >= 1300:
         bonus = 0.1 * Vendas
    else:
        bonus = 0
        
print("Bonus: ", bonus)

# Terceiro cenário

vendas = 2500
vendas_empresa = 10000
meta_empresa = 20000
Meta1 = 1300 # Ganha 10%
Meta2 = 2000 # Ganha 13%

if Vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif Vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0


print("Bonus:", bonus)

lista_produtos = ["airpod", "ipad", "iphone", "mackbook"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto em estoque.")
else:
    print("Não temos esse produto em estoque.")



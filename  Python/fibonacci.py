fibonacci ant = atual = numAux = cont = valor = 0

valor = int(input("Digite um número: "))

ant = 0
atual = 1
cont = 1

print(ant)
print(atual)

while (cont < valor):
    numAux = ant + atual
    print(numAux)
    ant = atual
    atual = numAux
    cont = cont + 1
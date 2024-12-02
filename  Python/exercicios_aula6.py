    #media
 
n1 = n2 = m = 0.0

n1 = float(input("Digite o primeiro valor  "))
n2 = float(input("Digite o segundo valor  "))

m = (n1 + n2) /2
print("A média entre ",n1," e ",n2,"é", m)

    #impar ou par

numero = float(input("Digite um número para saber se é impar ou par: "))
resto = numero %2

if resto == 0:
    print("Número é par")
else:
    print("Número é impar")

    #celsius para fahrenheit

def celsius_fahrenheit():
   c = float(input("Digite a temperatura em °c "))
   f = float((9 * c) / 5) + 32

   return print("A temperatura em fahrenheit: {0}°F".format(f))

    #fatorial de um numero

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = 5
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é", resultado)
  
    #palíndromo

def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("Digite uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")

        #quantidade de vogais 
    
def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    vogais = 'aeiou'
    return {i: string.count(i) for i in vogais}

print(conta_vogais("sofia linda"))

    #maior elemento

def maximum(lista): 
    max = float('-inf')
    for item in lista:
        try:
            valor = int(item)
            if valor > max:
                max = valor
        except:
            pass
    return max

print(maximum(['4', '07', '08', '2017', '364', '355673087875675']))
print(maximum(['4', '07', '08', '355673087875675', 'a', '2017']))

    #ordem crescente

crescente = []
for c in range(0,3):
  numero = int(input("Digite um valor: "))
  if c == 0 or numero > crescente[-1]:
    crescente.append(numero)
  else:
    posição = 0
    while posição < len(crescente):
      if numero <= crescente[posição]:
        crescente.insert(posição,numero)
        break
      posição = posição + 1 
print(f"Ordem crescente -->{crescente}<--")

    #numero primo

number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print('primo')
else:
  print('nao primo')

    #juros compostos

capital_inicial = float(input('Digite o depósito inicial: R$'))
i = float(input('Agora, digite a taxa de juros de uma poupança: '))
i = (i/100) # Definindo o valor de i separadamente para deixar o código mais limpo
t = 1   # Contador dos meses
aporte = 0 # Não coloque c2. É muito confuso.

while t < 24:
    if t == 1:
        m = capital_inicial + (capital_inicial * i) # Ou: m = capital_inicial * (1 + i)
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')
    else:
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')

    t = t + 1 # Mesma coisa escrever: t += 1

    op = input(f'Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]
    while op != 'S' and op != 'N':
        op = input(f'OPÇÃO INVÁLIDA! Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]

    if op == 'S':
        aporte = float(input(f'Digite o valor do depósito do {t}° mês: R$'))
    else:
        aporte = 0

    m = m + (m * i) + aporte # Ou: m = m * (1 + i) + aporte

ganho_com_juros = m - capital_inicial # (montante final - capital inicial)
print(f'No total, a quantidade de reais ganha com os JUROS COMPOSTOS será igual a R${ganho_com_juros}')

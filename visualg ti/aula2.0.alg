algoritmo "calculoIMC"
// Fun��o :
// Autor :
// Data : 21/11/2024
// Se��o de Declara��es 
var
   nome: Caractere
   imc, peso, altura: Real

inicio
// Se��o de Comandos 
 Escreval ("digite o seu nome")
 Leia (nome)
 Escreval ("digite o seu peso: ")
 Leia (peso)
 Escreval ("Digite a sua altura: ")
 Leia (Altura)
 imc<- peso / (altura * altura)
 Escreval(" o IMC de ", nome, " � ", imc)
 Escreval(" tabelas de imc")
 Escreval(" Menor que 18,5 magreza")
 Escreval(" Entre 18,5 e 24,9 normal")
 Escreval(" Entre 25,0 e 29,9	Sobrepeso")
 Escreval(" Entre 30,0 e 39,9	Obesidade")
 Escreval(" Maior que 40,0	Obesidade Grave")
fimalgoritmo

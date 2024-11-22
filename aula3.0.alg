gitalgoritmo "calcParcelas"
// Fun��o :
// Autor :
// Data : 22/11/2024
// Se��o de Declara��es 
var
   valorEmp, juros, parcelas,  rJuros, resposta:Real

inicio
// Se��o de Comandos
   Escreval("Quanto vou pagar de empr�stimo? R$ ")
   Leia(ValorEmp)
   Escreval()
   Escreval("Qual o valor dos juros cobrados pelo banco em % ")
   Leia(juros)
   Escreval()
   Escreval(" Quantas parcelas quero dividir para pagar?")
   Leia(parcelas)
   rJuros<-((valorEmp * juros) /100)
   Escreval()
   Escreval()
   Escreval("O valor dos meus juros ser� de R$",rJuros:5:2)
   resposta <- (rJuros + valorEmp) / parcelas
   Escreval()
   Escreval()
   Escreval()
   Escreval()
   Escreval("O valor das ", parcelas, "parcelasque terei que pagar � de R$ ", resposta:5:2)
fimalgoritmo

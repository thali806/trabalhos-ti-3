algoritmo "bascara"
// Fun��o :
// Autor :
// Data : 25/11/2024
// Se��o de Declara��es 
var
   a, b, c, xm, xn, d, r, dn: Real
   
inicio
// Se��o de Comandos 
   Escreval("Digite o valor de a: ")
   Leia(a)
   Escreval
   Escreval
   Escreval("Digite o valor de b: ")
   Leia(b)
   Escreval
   Escreval
   Escreval("Digite o valor de c: ")
   Leia(c)
   Escreval
   Escreval
   d<-((b*b)-(4*a*c))
   Escreval("Delta: ",d)
   se d<0 entao
      dn <- -(d)
      d <- dn
      r <- RaizQ(d)
      Escreval("Raiz de Delta: ", r)
      xm <-((-b + (r)) /(2*a))
      Escreval
      Escreval
      Escreval("O valor de X' �: ",xm, "!")
      Escreval
      Escreval
      cn <- ((-b - (r) / (2*a))
      Escreval("O valor de x'' �: ",xn, "!"
   senao
      r <- RaizQ(d)
      Escreval("Raiz de Delta: ",r)
      xm  <- ((-b +  (r) )) / (2*a))
      Escreval("O valor de X' �: ", xm)
      Escreval
      Escreval
      xn <- ((-b - (r) ) / (2*a))
      Escreval("O valor de X'' �: ",xn)
   fimse
fimalgoritmo

#Henrique de Carvalho Andreata
import sys

#Buscamos apenas um caminho
#Para o Backtracking, utilizo um Map salvando os resultados de somas que ja foram feitas, o qual verificamos antes de fazer novas somas para puxar diretamente o valor.
def sub_faz_soma(Guiche, tarifa, index, soma, fichas): 
    if soma == tarifa:
        print("Conseguimos somar o valor desejado com as fichas",fichas)
        exit()
        
    if index < 0:
        if(len(fichas)==0):
            print("Nao e possivel somar o valor")
        else:
            fichas.pop()
        return False

    if soma > tarifa:
        if(len(fichas)==0):
            print("Nao e possível somar o valor")
        else:
            soma = soma - Guiche[index]
            fichas.pop()
        return False

    fichas.append(Guiche[index])

    sub_faz_soma(Guiche, tarifa, index-1, soma+Guiche[index],fichas)
    sub_faz_soma(Guiche, tarifa, index-1, soma, fichas)

def faz_soma(Guiche, tarifa):
    sub_faz_soma(sorted(Guiche), tarifa, len(Guiche)-1, 0, [])


GuicheOriginal = list(map(int, sys.argv[1:]))
faz_soma(GuicheOriginal[1:], GuicheOriginal[0])

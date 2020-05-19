import codificacion as C
import Tableaux as T
import Tseytin as Ts
import DPLL1 as D
import main2 as M
Nc = 10      #Número de columnas (No queremos ni la columna 0 ni la fila 0)
Nf = 10      #Número de filas    (Por eso vamos hasta 10)
Np = 10     #Número de posibles números

letrasProposicionales = [chr(x) for x in range(256, 1300)]
def crea_regla1():
    temp = ""
    result = ""
    primera_casilla = True
    count=0
    for f in range (1,Nf):
        for c in range (1,Nc):
            primera_cl = True
            for p in range (1,Np):
                clausula = chr(C.codifica3(c,f,0,Nc,Nf,Np)+256) + "-"
                clausula += chr(C.codifica3(c,f,p,Nc,Nf,Np)+256) + "Y"

                for o in range(1,Np):
                    if (p!=o):
                        #print((C.codifica3(c,f,o,Nc,Nf,Np))+256)
                        clausula += chr((C.codifica3(c,f,o,Nc,Nf,Np))+256) +"-"+ "Y"
                if primera_cl:
                    temp = clausula
                    primera_cl = False
                else:
                    temp += clausula + "O"
            if primera_casilla:
                result = temp
                primera_casilla=False
            else:
                result += temp + "Y"


    return result

#def crea_regla4():
#    for c in range (1,Nc):
#        for p in range(No):

# REGLA 3 CADA FILA DEBE CONTENER LOS NUMEROS DEL 1 AL 9 UNA SOLA VEZ
def regla3():
    taux = ""
    aux = ""
    First_c = True
    regla_3 = chr(C.codifica3(1, 1, 1, Nf, Nc, Np)+256) +"Y"
    for i in range(1,Nf):
        c = True
        for j in range(1,Nc):
            for k in range(1, Np):
                regla_3 = chr(C.codifica3(i, j, 0, Nf,Nc, Np)+256)
                regla_3 += chr(C.codifica3(i, j, k, Nf, Nc, Np)+256) +"Y"
                for l in range(1,Np):
                    if (j != l):
                        regla_3 += chr(C.codifica3(i, j, l, Nf, Nc, Np)+256) +"-"+"Y"
                if c:
                    taux += regla_3
                    c = False
                else:
                    taux += regla_3 + "O"
            if First_c:
                aux = taux
            else:
                aux += taux + "Y"
    return aux

# #REGLA 2 CADA REGION DEBE CONTENER LOS NUMEROS DEL 1 AL 9 UNA SOLA VEZ
def regla2():
    taux = ""
    aux = ""
    First_c = True
    for i in range(1, Nc):
        for j in range (1,Nf):
            c = True
            for k in range(1, Np):
                regla_2 = chr(C.codifica3(i, j, k, Nc, Nf, Np)+256)
                regla_2 += chr(C.codifica3(i, j, k, Nc, Nf, Np)+256) +"Y"
                for l in range(2,Np):
                    if(j != i+3):
                        if(k != j+3):
                            regla_2 += chr(C.codifica3(i, j, l, Nc, Nf, Np)+256)+"-"+ "Y"
                if c:
                    taux += regla_2
                    c = False
                else:
                    taux += regla_2 + "O"
            if First_c:
                aux = taux
            else:
                aux += taux + "Y"
    return aux


#print(crea_regla1())
regla_final = crea_regla1() + regla2() + "Y" + regla3() + "Y"
a = T.String2Tree(regla_final)
print(T.Inorder(a))
b= T.Inorder(a)
c = Ts.Tseitin(b,letrasProposicionales)
d = Ts.formaClausal(c)
e = D.DPLL(d,{})

print (c)
#crea_regla1()

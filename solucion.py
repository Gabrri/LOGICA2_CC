import codificacion as C
import Tableaux as T
Nc = 9      #Número de columnas
Nf = 9      #Número de filas
Np = 10     #Número de posibles números

letrasProposicionales = [chr(x) for x in range(256, 1300)]
def crea_regla1():
    temp = ""
    result = ""
    primera_casilla = True
    for f in range (Nf):
        for c in range (Nc):
            primera_cl = True
            for p in range (1,Np):
                clausula = chr(C.codifica3(c,f,0,Nc,Nf,Np)+256)
                clausula += chr(C.codifica3(c,f,p,Nc,Nf,Np)+256) + "Y"

                for o in range(1,Np):
                    if (p!=o):
                        #print((C.codifica3(c,f,o,Nc,Nf,Np))+256)
                        clausula += chr((C.codifica3(c,f,o,Nc,Nf,Np))+256) +"-"+ "Y"
                if primera_cl:
                    temp += clausula
                    primera_cl = False
                else:
                    temp += clausula + "O"
            if primera_casilla:
                result = temp
            else:
                result += temp + "Y"

    return result

def crea_regla4():
    for c in Nc:
        for p in No:


#print(crea_regla1())

a = T.String2Tree(crea_regla1())
print(T.Inorder(a))
#crea_regla1()

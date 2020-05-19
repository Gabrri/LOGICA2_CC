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

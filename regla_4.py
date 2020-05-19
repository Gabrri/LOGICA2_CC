def regla4():
    taux = ""
    aux = ""
    First_c = True
    for i in range(1,Nf):
        c = True
        for j in range(1,Nc):
            for k in range(1, Np):
                regla_4 = chr(C.codifica3(i, j, k, Nf,Nc, Np)+256)
                regla_4 += chr(C.codifica3(i, j, k, Nf, Nc, Np)+256) +"Y"
                for l in range(1,Np):
                    if (i != l):
                        regla_4 += chr(C.codifica3(i, j, l, Nf, Nc, Np)+256) +"-"+"Y"
                if c:
                    taux += regla_4
                    c = False
                else:
                    taux += regla_4 + "O"
            if First_c:
                aux = taux
            else:
                aux += taux + "Y"
    return aux

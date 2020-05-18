import codificacion as C
import visualizacion as V
import tableaux as T

Nc = 9 # Numero de casillas
Nt = 10 # Numero de turnos

def crea_regla1():
    # Creamos la regla de que debe haber por lo menos un caballo en cada turno

    inicial_regla = True
    for t in range(Nt):

        inicial_clausula = True
        for c in range(Nc):
            if inicial_clausula:
                clausula = chr(C.codifica(c, t, Nc, Nt) + 256)
                inicial_clausula = False
            else:
                clausula += chr(C.codifica(c, t, Nc, Nt) + 256) + "O"

        if inicial_regla:
            regla1 = clausula
            inicial_regla = False
        else:
            regla1 += clausula + "Y"

    return regla1

Regla1 = crea_regla1()
I = T.Tableaux(Regla1)
print('Hay', len(I), 'soluciones')
if len(I) > 0:
    print('Nos quedamos con una')
    I1 = [T.Inorder(x) for x in I[52]]
    print(I1)
    V.dibujar_tablero(I1, Nc, Nt)

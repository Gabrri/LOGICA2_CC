import codificacion as C
import visualizacion as V
#import tableaux as T

##################################################################
letrasProposicionales = [chr(i) for i in range(256, 1000)]
Nfilas = 3 # Numero de filas
Ncolumnas = 4 # Numero de columnas

letras = []
#print("\n\nfilas x columnas")
#for i in range(Nfilas):
#    for j in range(Ncolumnas):
#        v1 = C.codifica(i, j, Nfilas, Ncolumnas)
#        cod = chr(v1 + 256)
#        print(cod, end = " ")
#        letras.append(cod)
#    print("")
#
#print("************")
#
#for l in letras:
#    f, c = C.decodifica(ord(l) - 256, Nfilas, Ncolumnas)
#    print(l, "Se decodifica como:", f, c)


######################################################
letrasProposicionales = [chr(i) for i in range(256, 1000)]
Nfilas = 9
Ncolumnas = 9
Nobjeto = 10


letras = []
print(C.codifica3(2,1,3,Nfilas,9,10))
print(C.decodifica3(193,9,9,10)[1])

#print("\n\n(filas x columnas) x objetos")
#for i in range(Nfilas):
#    for j in range(Ncolumnas):
#        for o in range(Nobjeto):
#            v1 = C.codifica(i, j, Nfilas, Ncolumnas)
#            v2 = C.codifica(v1, o, Nfilas * Ncolumnas, Nobjeto)
#            cod = chr(v2 + 256)
#            print(cod, end = " ")
#            letras.append(cod)
#        print("")
#
#print("************")
#
#for l in letras:
#    v1, o = C.decodifica(ord(l) - 256, Nfilas * Ncolumnas, Nobjeto)
#    f, c = C.decodifica(v1, Nfilas, Ncolumnas)
#    print(l, "Se decodifica como:", f, c, o)

######################################################
#letrasProposicionales = [chr(i) for i in range(256, 1000)]
#Nfilas = 3
#Ncolumnas = 3
#Nobjeto = 3
#Nturnos = 2
#
#letras = []
#print("\n\n((filas x columnas) x objeto) x turno")
#for i in range(Nfilas):
#    for j in range(Ncolumnas):
#        for o in range(Nobjeto):
#            for t in range(Nturnos):
#                v1 = C.codifica(i, j, Nfilas, Ncolumnas)
#                v2 = C.codifica(v1, o, Nfilas * Ncolumnas, Nobjeto)
#                v3 = C.codifica(v2, t, Nfilas * Ncolumnas * Nobjeto, Nturnos)
#                cod = chr(v3 + 256)
#                print(cod, end = " ")
#                letras.append(cod)
#            print("")

#print("************")
#
#for l in letras:
#    v2, t = C.decodifica(ord(l) - 256, Nfilas * Ncolumnas * Nobjeto, Nturnos)
#    v1, o = C.decodifica(v2, Nfilas * Ncolumnas, Nobjeto)
#    f, c = C.decodifica(v1, Nfilas, Ncolumnas)
#    print(l, "Se decodifica como:", f, c, o, t)

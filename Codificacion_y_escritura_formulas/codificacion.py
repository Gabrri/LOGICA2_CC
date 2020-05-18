# Codificacion y decodificacion de una tabla de Nf filas y Nc columnas

def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c

    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)

    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla

    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)

    f = int(n / Nc)
    c = n % Nc
    return f, c

def codifica3(f, c, o, Nf, Nc, No):
    # Funcion que codifica tres argumentos
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((o >= 0) and (o <= No - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(v1, o, Nf * Nc, No)
    return v2

def decodifica3(x, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, o

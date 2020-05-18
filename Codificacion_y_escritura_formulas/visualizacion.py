#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla y un turno;
# el literal P(c,t) es positivo sii hay un caballo en la casilla c en el turno t.

import codificacion as C

# Formato de la entrada: - las letras proposionales;
#                        - solo se aceptan literales que son str de longitud 1

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(I):
    # Visualiza un tablero dada una interpretacion I
    # Input:
    #   - I, una interpretacion I como diccionario
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./3
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(\
                                    (0, step), \
                                    step, \
                                    step,\
                                    facecolor='cornsilk')\
                                    )
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
            facecolor='cornsilk'))
    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='lightslategrey'))

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de caballo
    arr_img = plt.imread("caballo.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.1)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]

    # K = I.keys()
    # f = [x for x in K if I[x]==1]
    f = I

    for l in f:
        c, t = C.decodifica(ord(l) - 255, 9, 2)
        ab = AnnotationBbox(imagebox, direcciones[c], frameon=False)
        axes.add_artist(ab)
        #plt.show()
        fig.savefig("Soluciones/Tablero_" + str(t) + ".png")

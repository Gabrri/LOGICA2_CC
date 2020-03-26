#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"



def polaco(formula):
    if(len(formula)<=2): return formula
    elif(not(main(formula))):
        derecha = ""
        for b in range(2, len(formula)-1):
                derecha+=formula[b]

        return formula[main(formula)] + polaco(derecha)

    else:
            izquierda = ""
            derecha = ""

            for a in range(0, main(formula)):
                izquierda+=formula[a]

            for b in range(main(formula)+1, len(formula)):
                derecha+=formula[b]

            izquierda_nueva = izquierda
            derecha_nueva = derecha

            if(izquierda[0]=='(' and izquierda[len(izquierda)-1]==')'):
                izquierda_nueva = ""
                for a in range(1, len(izquierda)-1):
                    izquierda_nueva+=izquierda[a]

            if(derecha[0]=='(' and derecha[len(derecha)-1]==')'):
                derecha_nueva = ""
                for b in range(1, len(derecha)-1):
                    derecha_nueva+=derecha[b]

            print("izquierda: " + izquierda_nueva)
            print("derecha: " + derecha_nueva)

            return formula[main(formula)] + polaco(izquierda_nueva) + polaco(derecha_nueva)

def polacoInverso(polaco, referencia):
        if(referencia == (len(polaco)-1)): return polaco[referencia]
        else:
                return polacoInverso(polaco, referencia+1) + polaco[referencia]


def String2Tree(A, LetrasProposicionales):

    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in LetrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
    return Pila[-1]

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	return False

def es_literal(D):
	I = D.copy()
	for i in I:
		if(i[0] == '-'):
			I.pop(i)
			i = Complemento(i)
			if(I.get(i) == 0):
				I[i[0]] = 1
			return True       
			else:
				I[i[0]] = 0
	return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	return False

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas

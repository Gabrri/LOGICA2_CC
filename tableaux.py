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

def imprime_tableau(tableau):
	primero = True
	for H in tableau:
		if primero == True:
			cadena = '[' + imprime_hoja(H)
			primero = False
		else:
		 cadena += ", " + imprime_hoja(H)
	return cadena + "]"

def par_complementario(l):
	#Dada una función de literales h, verifica si en h hay por lo menos un par complementario
	temp= []
	for q in lista:
		if q.right != None:
			letra = q.label + q.right.label
		else:
			letra = q.label
		noletra = "-" + letra
		prov = letra[1:]
		if prov in temp or noletra in temp:
			return True
		temp.append(letra)
	return False

def es_literal(D):
	#Dada una fórmula A verifica si A es un literal
	if A.label in letrasProposicionales:
		return True
	elif A.label == "-":
		if A.right.label in letrasProposicionales:
			return True
	else:
		return False

def no_literales(l):
	#Dada una lista de fórmulas h, verifica si en h hay alguna fórmula que no es literales
	for q in lista:
		if not literal(q):
			return False
	return True


def alfa_beta(a):
	if a.label == '-':
		if a.right.label == '-':
			return '1ALFA'
		elif a.right.label == 'O':
			return '3ALFA'
		elif a.right.label == '>':
			return '4ALFA'
		elif a.right.label == 'Y':
			return '1BETA'
	else:
		if a.label == 'Y':
			return '2ALFA'
		elif a.label == 'O':
			return '2BETA'
		elif a.label == '>':
			return '3BETA'

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):
arbol = StringtoTree(formula, letrasProposicionales)
lista = [[arbol]]
open = []
open = regla_aprop(lista)
if len(open) > 0:
	return "La formula es abierta."
else:
	return "La formula es cerrada."

	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas

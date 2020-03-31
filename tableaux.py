
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

"""
Los conectivos que se van a utilizar
"""
neg = "-"
Y = "Y"
O = "O"
ent = ">"
conectivosBinarios = [O, Y, ent]


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
def Atomos(f):
        if f.right == None:
                return [f.label]
        elif f.label == neg:
                return Atomos(f.right)
        elif f.label in conectivosBinarios:
                return Atomos(f.left) + Atomos(f.right)
        
def string2Tree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!
#Crea una formula como tree dada una formula
        #como cadena escritra en notacion POLACA INVERSA
        #Input: A, Lista de caracteres con una formula escrita en notacon polaca iinversa
        #LetrasProposicionales, lista de letras proposicionales
#output: formula como tree
    
    
    pila = []
    for c in A:
            
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
            #print(inorder(Tree(c,None,None)))
        elif c == neg:
            FormulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(FormulaAux)
        elif c in conectivosBinarios:
            FormulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(FormulaAux)
    
    return pila[-1]


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
        for elemento in l:
                for segundoElem in l:
                        if elemento.label == neg:
                                #en el caso donde el primero fuese una negacion
                                if elemento.right.label == segundoElem.label:
                                        return True
                        
                        if segundoElem.label == neg:
                                if elemento.label == segundoElem.right.label:
                                        return True

        return False


def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
        #ahora debo detectar como tal si bien sea es la letra o contiene una negacio
        if(f.label == neg):
                if f.right.label in letrasProposicionales:
                        return True
        if f.label in letrasProposicionales:
                return True

        return False
def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
        for elemento in l:
                #revisar en casa una de las forumas contenidas en l
                if (not(es_literal(elemento))):
                        return False
        return True


def clasifica_y_extiende(f):
        # clasifica una fórmula como alfa o beta y extiende listaHojas
        # de acuerdo a la regla respectiva
        # Input: f, una fórmula como árbol
        # Output: no tiene output, pues modifica la variable global listaHojas
        global listaHojas
        #ya como tal flata es reemplazar por cada una de ellas su forma cambiada
        #la cosa es que va a a entrar como una lista de listas
    
        #tengo una lista de f en cada sublista hay una formula

        if f.label == neg:
                if f.right.label == neg:
                        print("1a")
                        #caso de que sea 1a entonces solo se remplaza
                        contador = 0
                        for formula in listaHojas:
                                if f == formula[0]:
                                        listaHojas[contador] = [f.right.right]
                                contador+= 1
                elif f.right.label == O:
                        print("3a")
                        #es la negacion del primero y la del segundo
                        contador = 0
                        for formula in listaHojas:
                                if f == formula[0]:
                    
                                        listaHojas[contador] = [Tree(neg,None ,f.right.left), Tree(neg, None, f.right.right)]
                    
                                contador +=1
                elif f.right.label == ent:
                        print("4a")
                        contador = 0
                        for formula in listaHojas:
                                if f == formula[0]:
                                        listaHojas[contador] = [f.right.left, Tree(neg, None, f.right.right)]
                                contador +=1
                elif f.right.label == Y:
                        print("1b")
                        #quiere decir que estamos en el caso 1b
                        listaHojas.remove([f])
                        listaHojas.append([Tree(neg, None, f.right.left)])
                        listaHojas.append([Tree(neg, None, f.right.right)])
                
                
        elif f.label == Y:
                print("2a")
                #en el caso de ser 2a debe buscarlo en la lista y cambiaor
                contador = 0
                for formula in listaHojas:

                        if f == formula[0]:
                                #quiero borrar la anterior y meter esta
                                #para lograrlo debo acceder a los que estan a los lados
                                listaHojas[contador] = [f.left,f.right] 
                        contador += 1
            
        elif f.label == O:
                print("2b")
        
                #ya identificamos como tal la fomurla ahora es cuando se divide
                #listaHojas[contador] = [f.left], [f.right]
                
                
                listaHojas.remove([f])
                listaHojas.append([f.left])
                listaHojas.append([f.right])
        
        elif f.label == ent:
                print("3b")
                listaHojas.remove([f])
                listaHojas.append([Tree(neg, None, f.left)])
                listaHojas.append([f.right])
                       
         

def Tableaux(f):

        # Algoritmo de creacion de tableau a partir de lista_hojas
        
	# Imput: - f, una fórmula como string en notación polaca inversa

	# Output: interpretaciones: lista de listas de literales que hacen

	#		 verdadera a f

        global listaHojas
        
        global listaInterpsVerdaderas
        
        A = string2Tree(f)

        listaHojas = [[A]]
        #print(Inorder(listahojas[0][0]))
        

        while len(listaHojas) > 0 :

                hojas = choice(listaHojas)
                #print("prueba q")
                #print(Inorder(hojas[0]))
                if not no_literales(hojas) :
                        #print("no literales")
                        for tree in hojas:
                                #print("primer tree")
                                #print(Inorder(tree))
                                clasifica_y_extiende(tree)

                                

                else:
                        
                        if par_complementario(hojas):
                                #print("hey par complementario")
                                listaHojas.remove(hojas)

                        else:

                                listaInterpsVerdaderas.append(hojas)

                                listaHojas.remove(hojas)

        return listaInterpsVerdaderas

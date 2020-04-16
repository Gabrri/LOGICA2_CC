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


#
#def polaco(formula):
#    if(len(formula)<=2): return formula
#    elif(not(main(formula))):
#        derecha = ""
#        for b in range(2, len(formula)-1):
#                derecha+=formula[b]
#
#        return formula[main(formula)] + polaco(derecha)
#
#    else:
#            izquierda = ""
#            derecha = ""
#
#            for a in range(0, main(formula)):
#                izquierda+=formula[a]
#
#            for b in range(main(formula)+1, len(formula)):
#                derecha+=formula[b]
#
#            izquierda_nueva = izquierda
#            derecha_nueva = derecha
#
#            if(izquierda[0]=='(' and izquierda[len(izquierda)-1]==')'):
#                izquierda_nueva = ""
#                for a in range(1, len(izquierda)-1):
#                    izquierda_nueva+=izquierda[a]
#
#            if(derecha[0]=='(' and derecha[len(derecha)-1]==')'):
#                derecha_nueva = ""
#                for b in range(1, len(derecha)-1):
#                    derecha_nueva+=derecha[b]
#
#            print("izquierda: " + izquierda_nueva)
#            print("derecha: " + derecha_nueva)
#
#            return formula[main(formula)] + polaco(izquierda_nueva) + polaco(derecha_nueva)
#
#def polacoInverso(polaco, referencia):
#        if(referencia == (len(polaco)-1)): return polaco[referencia]
#        else:
#                return polacoInverso(polaco, referencia+1) + polaco[referencia]


def String2Tree(A):
    global letrasProposicionales
    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
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
#
#print(string2Tree('rq O -p∧',letrasProposicionales))
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
	for q in l:
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


p = Tree('p',None,None)
np = Tree('-',None,p)
nnp = Tree('-',None,np)
q = Tree('q',None,None)
nq = Tree('-',None,q)



def es_literal(A):
	#Dada una fórmula A verifica si A es un literal
    if A.right == None:
        return A.label in letrasProposicionales
    elif A.left == None:
        return A.right.label in letrasProposicionales
    return False

def no_literales(l):
	#Dada una lista de fórmulas h, verifica si en h hay alguna fórmula que no es literales
	for q in l:
		if not es_literal(q):
			return False
	return True

#print(par_complementario([p,q]))
#print(no_literales([p,q])) 

#nopoq = Tree('-',None, Tree('O',p,q))
#print(Inorder(nnp))

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
	elif a.label == 'Y':
		return '2ALFA'
	elif a.label == 'O':
		return '2BETA'
	elif a.label == '>':
		return '3BETA'
#print(alfa_beta(Tree('>',q,p)))

def clasifica_y_extiende(f):
    # clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
    global listaHojas
    for a in listaHojas:
        for i in a:
#            print(Inorder(i))
#            

            if Inorder(i) == Inorder(f) and alfa_beta(f) == '1ALFA':
	            a.remove(i)
	            new = f.right.right
	            a.append(new)
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '2ALFA':
                a.remove(i)
                new1 = i.left
                new2 = i.right
                a.append(new1)
                a.append(new2)
#                break
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '3ALFA':
                a.remove(i)
                new1 = Tree('-',None,i.right.left)
                new2 = Tree('-',None,i.right.right)
                a.append(new1)
                a.append(new2)
#	            a.insert(i,[new1,new2])
            
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '4ALFA':
                a.remove(i)
                new1 = f.right.left
                new2 = Tree('-',None,f.right.right)
                a.append(new1)
                a.append(new2)
                
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '1BETA':
                a.remove(i)
                new1 = Tree('-',None,f.right.left)
                new2 = Tree('-',None,f.right.right)
                hoja_nueva = a.copy()
                hoja_nueva.append(new2)
                a.append(new1)
                listaHojas.append(hoja_nueva)
                
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '2BETA':
                a.remove(i)
                new1 = i.left
                new2 = i.right
                hoja_nueva = a.copy()
                hoja_nueva.append(new2)
                a.append(new1)
                listaHojas.append(hoja_nueva)
                
            elif Inorder(i) == Inorder(f) and alfa_beta(f) == '3BETA':
                a.remove(i)
                new1 = Tree('-',None,f.left)
                new2 = i.right
                hoja_nueva = a.copy()
                hoja_nueva.append(new2)
                a.append(new1)
                listaHojas.append(hoja_nueva)
                

#ki = Tree('O',q,p)

#print (listaHojas)
#
#print("---------------------------")
#print (listaHojas)
#listaHojas= [[p],[Tree('-',None,Tree('Y',q,p)),q]]
#for i in listaHojas:
#    for j in i:
#        print (Inorder(j))
#print("-------")  
#clasifica_y_extiende(Tree('-',None,Tree('Y',q,p)))
#print("-------")	
#for i in listaHojas:
#    print(".......")
#    for j in i:
#        print (Inorder(j))



#def Tableaux(f):
#    arbol = String2Tree(formula, letrasProposicionales)
#    lista = [[arbol]]
#    open = []
#    open = regla_aprop(lista)
#    if len(open) > 0:
#    	return "La formula es abierta."
#    else:
#    	return "La formula es cerrada."
#
#    	global listaHojas
#    	global listaInterpsVerdaderas
#
#    	A = string2Tree(f)
#    	listaHojas = [[A]]
#
#    	return listaInterpsVerdaderas

def Tableaux(f):
	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
     global listaHojas
     global listaInterpsVerdaderas

     A = String2Tree(f)
     listaHojas = [[A]] 

     while (len(listaHojas) > 0):
         hoja = choice(listaHojas)
#         print(len(listaHojas))
#         for i in hoja:
#             print(Inorder(i))
         if no_literales(hoja):
             if par_complementario(hoja):
#                 print("e")
                 listaHojas.remove(hoja)
             else:
#                 print("i")
                 listaHojas.remove(hoja)
                 listaInterpsVerdaderas.append(hoja)
         else:
            for tree in hoja:
#                print(Inorder(tree))
                clasifica_y_extiende(tree)

     return listaInterpsVerdaderas
#print (listaInterpsVerdaderas)
#print(listaHojas)
#listaHojas= [[p],[Tree('Y',q,p),q]]
#print(Tableaux(listaHojas))
#print(choice(listaHojas))
print(Inorder(String2Tree("pq>-rO")))
#lista=[[(String2Tree("pqY"))]]
#for i in lista:
#    print(i)
#lol = Tableaux("b-aYzyOOvt-Ox-u>Osr>qpOOOO-")
#for i in lol:
#    print(imprime_hoja(i))
#    for j in i:
#
#        print(Inorder(j))
#    print("--------------------")
#print(listaHojas)
     
 
    
# AQUÍ SE PONE LA FÓRMULA
formula = ("pq>-rO")
ta = Tableaux(formula)

# Imprime el resultado en consola
if len(ta) == 0:
    print('La fórmula es insatisfacible')
else:
    print('La fórmula es satisfacible.')
    print('Las hojas abiertas del tableaux son:')
    for l in ta:
        print(imprime_hoja(l))

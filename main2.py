# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==5 or len(A)==8), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')
    #print(B)
    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(1300, 5000)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    #  IMPLEMENTAR AQUI ALGORITMO TSEITIN
    #=================|Inicio de implementación|=========================
    #===========================|AUTOR: ESTEFANIA LAVERDE|==================================
    L=[]#Inicializamos lista de conjunciones||aquí se guardan todos los <>
    Pila=[]#Inicializamos Pila
    I=-1#Inicializamos contador de variables nuevas
    s=A[0]#Inicializamos símbolo de trabajo

    while len(A)>0:
        if (s in letrasProposicionalesA or s in letrasProposicionalesB) and len(Pila)!=0 and Pila[-1]=='-': #Si s es un átomo y Pila no vacía y Pila[-1] = ’¬’
            I+=1
            Atomo = letrasProposicionalesB[I]
            Pila=Pila[0:-1]#Se van eliminando caracteres uno por uno
            Pila.append(Atomo)
            L.append(Atomo+"<>"+"-"+s)
            A=A[1:]
            if len(A)>0:
                s=A[0]
        elif s==")":#Para las formulas con conectores binarios
            w=Pila[-1]
            u=Pila[-2]#El conector binario
            v=Pila[-3]
            Pila=Pila[:len(Pila)-4]
            I+=1
            Atomo=letrasProposicionalesB[I]
            L.append(Atomo+"<>"+"("+v+u+w+")")
            s= Atomo
        else:
            Pila.append(s)
            A=A[1:]
            if len(A)>0:
                s=A[0]
    B=""
    if I<0:
        Atomo=Pila[-1]
    else:
        Atomo=letrasProposicionalesB[I]

    for x in L:

        y=enFNC(x)
        #print(y)
        B+="Y"+y


    B= Atomo+B

    print("todos los iff: ",L)
    #print(B)
    return B

    #=================|Fin de implemetación|================================
    pass

#========================|PRUEBA|===============================
#letrasProposicionalesprubeaA=["p","q","r"]
#f="-p"
#print(Tseitin(f,letrasProposicionalesprubeaA))
#===========================|LA PRUEBA FUNCIONA|===========================

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula sin paréntesis
# Output: L (lista), lista de literales
# Se asume que cada literal es un solo caracter
def Clausula(C):

    #  IMPLEMENTAR AQUI ALGORITMO CLAUSULA
    #===============================|INICIO DE IMPLEMENTACIÓN|==========================
    #===============================|AUTOR: JULIAN CASTRO|===========================================
    L=[]
    while len(C)>0:

        s=C[0]
        if s=="-":
            L.append(s+C[1])
            C=C[3:]
        else:
            L.append(s)
            C=C[2:]
    return L
    #===============================|FIN DE IMPLEMENTACIÓN|=============================
    pass
#========================|PRUEBA|===============================
#clausula="ĀY-ĀO-pYĀOp"
#print(Clausula(clausula))
#===========================|LA PRUEBA FUNCIONA|===========================

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC y sin paréntesis
# Output: L (lista), lista de listas de literales
def formaClausal(A):

    #  IMPLEMENTAR AQUI ALGORITMO FORMA CLAUSAL
    #===============================|INICIO DE IMPLEMENTACIÓN|=============================
    #===============================|AUTOR: JULIAN CASTRO|===============================================
    L=[]
    i=0

    while len(A)>0:
        if i>=len(A):
            L.append(Clausula(A))
            A=[]
        else:
            if A[i]=="Y":
                L.append(Clausula(A[:i]))
                A=A[i+1:]
                i=0
            else:
                i+=1
    return L
    #===============================|FIN DE IMPLEMENTACIÓN|================================
    pass
#


#print(Tseitin("(((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӧYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӦYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӥYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӤYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӣYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӢYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӡYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӠYӞ)))))))))O((-ӦY(-ӥY(-ӤY(-ӣY(-ӢY(-ӡY(-ӠY(-ӟY(ӟYӞ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӝYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӜYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӛYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӚYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(әYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӘYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӗYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӖYӔ)))))))))O((-ӝY(-ӛY(-ӚY(-әY(-ӘY(-ӗY(-ӖY(-ӕY(ӕYӔ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӓYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӒYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӑYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӐYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӏYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӎYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӍYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӌYӊ)))))))))O((-ӓY(-ӒY(-ӐY(-ӏY(-ӎY(-ӍY(-ӌY(-ӋY(ӋYӊ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӉYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӈYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӇYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӆYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӅYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӄYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӃYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӂYӀ)))))))))O((-ӉY(-ӈY(-ӇY(-ӅY(-ӄY(-ӃY(-ӂY(-ӁY(ӁYӀ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҿYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҾYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҽYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҼYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(һYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҺYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҹYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҸYҶ)))))))))O((-ҿY(-ҾY(-ҽY(-ҼY(-ҺY(-ҹY(-ҸY(-ҷY(ҷYҶ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҵYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҴYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҳYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҲYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ұYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҰYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(үYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҮYҬ)))))))))O((-ҵY(-ҴY(-ҳY(-ҲY(-ұY(-үY(-ҮY(-ҭY(ҭYҬ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҫYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҪYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҩYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҨYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҧYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҦYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҥYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ҤYҢ)))))))))O((-ҫY(-ҪY(-ҩY(-ҨY(-ҧY(-ҦY(-ҤY(-ңY(ңYҢ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҡYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҠYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҟYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҞYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҝYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҜYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(қYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҚYҘ)))))))))O((-ҡY(-ҠY(-ҟY(-ҞY(-ҝY(-ҜY(-қY(-ҙY(ҙYҘ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(җYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҖYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҕYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҔYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ғYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҒYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ґYҎ)))))))))O((-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҐYҎ)))))))))O(-җY(-ҖY(-ҕY(-ҔY(-ғY(-ҒY(-ґY(-ҐY(ҏYҎ)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))Y((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(҃YѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(҂YѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ҁYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ҀYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ѿYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ѾYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ѽYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ѼYѺ)))))))))O((-҂Y(-ҁY(-ҀY(-ѿY(-ѾY(-ѽY(-ѼY(-ѻY(ѻYѺ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѹYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѸYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѷYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѶYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѵYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѴYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѳYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѲYѰ)))))))))O((-ѹY(-ѷY(-ѶY(-ѵY(-ѴY(-ѳY(-ѲY(-ѱY(ѱYѰ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѯYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѮYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѭYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѬYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѫYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѪYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѩYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѨYѦ)))))))))O((-ѯY(-ѮY(-ѬY(-ѫY(-ѪY(-ѩY(-ѨY(-ѧY(ѧYѦ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѥYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѤYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѣYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѢYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѡYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѠYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(џYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ўYќ)))))))))O((-ѥY(-ѤY(-ѣY(-ѡY(-ѠY(-џY(-ўY(-ѝY(ѝYќ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(ћYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(њYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(љYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(јYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(їYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(іYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(ѕYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(єYђ)))))))))O((-ћY(-њY(-љY(-јY(-іY(-ѕY(-єY(-ѓY(ѓYђ)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(ёYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(ѐYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(яYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(юYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(эYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(ьYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(ыYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(ъYш)))))))))O((-ёY(-ѐY(-яY(-юY(-эY(-ыY(-ъY(-щY(щYш)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(чYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(цYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(хYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(фYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(уYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(тYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(сYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(рYо)))))))))O((-чY(-цY(-хY(-фY(-уY(-тY(-рY(-пY(пYо)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(нYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(мYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(лYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(кYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(йYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(иYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(зYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(жYд)))))))))O((-нY(-мY(-лY(-кY(-йY(-иY(-зY(-еY(еYд)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(гYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(вYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(бYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(аYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(ЯYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(ЮYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(ЭYЪ)))))))))O((-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(ЬYЪ)))))))))O(-гY(-вY(-бY(-аY(-ЯY(-ЮY(-ЭY(-ЬY(ЫYЪ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))",[chr(x) for x in range(256, 1300)] ))

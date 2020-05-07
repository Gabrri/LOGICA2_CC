 def ClaUnitaria(U):
	flag=False
	posicion=-1
	for a in range(len(U)):
		if(len(U[a])==0): return (True,False,posicion)
		elif(len(U[a])==1):
			flag=True
			posicion=a
	return (False,flag,posicion)

def ClaUnit(S):
	for i in S:
		if(len(i) == 1): return True
	return False

def Complemento(L):
	if(L[0] == '-'):
		return L.replace('-','')
	else:
		return '-' + L

def removeCl(S ,l):
	S.remove(l)
	if(len(l)>=1):
		if(l[0] == '-'): L = l.replace('-','')
		else: L = l[0]
		for i in S:
			if(L in i): S.remove(i)

	return S

def removeComp(S,L):
	if(len(L)>=1):
		l = L[0]
		l = Complemento(l)
		for i in S:
			if(l in i):
				i.remove(l)
	return S

def unitPropagate(S,I):
	vacia,unitaria,posicion=ClaUnitaria(S)
	while(vacia==False and ClaUnit(S)):
		for i in S:
			S=removeCl(S,i)
			S=removeComp(S,i)
			if(len(i)==0): return 'Error',I
			if(i[0] == '-'):
				I[Complemento(i[0])] = 0
			else:
				I[i[0]] = 1
	return S, I

def literalDicc(D):
	I = D.copy()
	for i in I:
		if(i[0] == '-'):
			I.pop(i)
			i = Complemento(i)
			if(I.get(i) == 0):
				I[i[0]] = 1
			else:
				I[i[0]] = 0
	return I

def DPLL(S,I):
	S,I=unitPropagate(S,I)
	if(S == 'Error'): return 'Insatisfacible' , '{}'
	if(len(S) == 0):
		return 'Satisfacible' , literalDicc(I)
	for i in S:
		if(len(i) == 0):
			return 'Insatisfacible' , '{}'
	L = S[0]
	L = Complemento(Complemento(L[0]))
	IP = I.copy()
	if(L[0] == '-'):
		IP[Complemento(L[0])] = 0
	else:
		IP[L[0]] = 1
	SLOCO = S.copy()
	SLOCO.append(L[0])

	sati,i=DPLL(SLOCO,IP)
	if(sati == 'Satisfacible'):
		return 'Satisfacible' , literalDicc(IP)
	else:
		STAMAL = S.copy()
		STAMAL.append(Complemento(L[0]))
		IPP = I.copy()
		if(L[0] == '-'):
			IPP[Complemento(L[0])] = 1
		else:
			IPP[L[0]] = 0
	return DPLL(STAMAL,IPP) 

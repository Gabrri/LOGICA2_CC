import copy
def unitPropagate(S,I):
    count=0
    #print (S[0])
    while count < len(S):
        #print(count)
        if len(S[count]) == 1:
            l = S[count][0]
            if len(l) == 1:
                c= "-"+l
                I[l] = 1

            else:
                c=l[1]
                I[c] = 0

            for cl in S:
                if c in cl:
                    cl.remove(c)

            pr = count
            it = 0
            while it < len(S):

                if l in S[it]:
                    S.remove(S[it])
                    count -= 1
                    it -=1

                it+=1
            if ((pr - count) > 1):
                count = pr-1
        count += 1


    return S,I

#print(unitPropagate([["p"],["-p","-q"],["p","q"],["p","-q"]],{}))
#print(unitPropagate([['-r']],{'p': 1, 'q': 1}))
#print(len(unitPropagate([],{})[0]))
def DPLL(S,I):

    #Paso 1
    paso1 = unitPropagate(S,I)

    #Paso 2
    for i in paso1[0]:
        if len(i) == 0:
            return "Insatisfacible",{}
    #Paso 3
    if len(paso1[0]) == 0:
        return "Satisfacible",paso1[1]

    #Paso 4
    new_l = str(paso1[0][0][0])
    s_p = copy.deepcopy(paso1[0])
    i_p = paso1[1].copy()
    if len(new_l) == 1:
        new_c= "-"+new_l
        i_p[new_l] = 1

    else:
        new_c=new_l[1]
        i_p[new_l] = 0

    for cl in s_p:
        if new_c in cl:
            cl.remove(new_c)


    it = 0
    while it < len(s_p):
        if new_l in s_p[it]:
            s_p.remove(s_p[it])
            it -=1

        it +=1

    if DPLL(s_p,i_p)[0] == "Satisfacible":
        return "Satisfacible",DPLL(s_p,i_p)[1]

    #Paso 8
    else:
        s_pp = copy.deepcopy(paso1[0])
        i_pp = paso1[1].copy()
        print(s_pp)

        if len(new_l) == 1:
            l_pp= "-"+str(new_l)
            c_pp = new_l
            i_pp[new_l] = 0

        else:
            l_pp=new_l[1]
            c_pp = new_l
            i_pp[new_l] = 1

        for cl in s_pp:
            if c_pp in cl:
                cl.remove(c_pp)
            it2 = 0
            while it2 < len(s_pp):
                if l_pp in s_pp[it2]:
                    s_pp.remove(s_pp[it2])
                    it2 -=1
                it2 +=1
        return DPLL(s_pp,i_pp)


#print(DPLL([["p"],["-p","-q"],["p","q"]],{}))
#

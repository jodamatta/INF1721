def MOM_algo(A,k):
    # se a lista tiver tamanho 1, retornamos o unico elemento
    if len(A) == 1:
        return A[0]

    # dividimos a lista em sublistas de tamanho 5
    sublists_A = []
    for i in range(0, len(A), 5): 
        sublist = []
        for j in range(5):
            index = i + j
            if index >= len(A):
                break
            else:
                sublist.append(A[index])
        sublists_A.append(sublist)
    
    # ordenamos as sublistas
    # como o tamanho das sublistas e sempre 5, a complexidade dessa ordenacao e constante
    sublists_sorted = []
    for i in range(len(sublists_A)):
        aux = sorted(sublists_A[i])
        sublists_sorted.append(aux[len(aux)//2])

    # achamos a mediana das medianas
    mediana = MOM_algo(sublists_sorted, len(sublists_sorted)//2)

    # dividimos A em duas listas
    L = [j for j in A if j < mediana]
    M = [j for j in A if j == mediana]
    R = [j for j in A if j > mediana]

    if k < len(L):
        return MOM_algo(L, k)
    elif k <= len(L) + len(M):
        return mediana
    else:
        return MOM_algo(R, k - len(L) - len(M))
    

def LinearSelection(A,k):
    return MOM_algo(A,k)

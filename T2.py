import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def BubbleSort(A):
    for num in range(len(A) - 1, 0, -1):
      for i in range(num):
        if A[i] > A[i+1]:
          temp = A[i]
          A[i] = A[i+1]
          A[i+1] = temp
    return A

def SortSelection(A,k):
  A_ord = BubbleSort(A)
  return A_ord[k]

tamanhos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
media_tempo_bubble = []
media_tempo_linear = []

for tamanho in tamanhos:
    tempos_bubble = []
    tempos_linear = []
    for t in range(10):
        instance = list(np.random.randint(1, 100000, tamanho))

        # bubble sort selection
        start = time.time()
        mediana = SortSelection(instance, tamanho//2)
        end = time.time()
        tempos_bubble.append(end - start)

        #linear seletion
        start = time.time()
        mediana = LinearSelection(instance, tamanho//2)
        end = time.time()
        tempos_linear.append(end - start) 
        print(t, tamanho)
        
    media_tempo_bubble.append(np.mean(tempos_bubble))
    media_tempo_linear.append(np.mean(tempos_linear))

df_plot = pd.DataFrame({'Tamanho': tamanhos, 'Media de tempo bubble': media_tempo_bubble, "Media de Tempo Linear": media_tempo_linear})

ax = plt.gca()
df_plot.plot(x='Tamanho', y='Media de tempo bubble', ax=ax, label='SortSelection')
df_plot.plot(x='Tamanho', y='Media de Tempo Linear', ax=ax, label='LinearSelection')
plt.ylabel('Tempo Medio')
plt.legend()
plt.show()

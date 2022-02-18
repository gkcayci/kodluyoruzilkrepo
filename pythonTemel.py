# 1) Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5] 

# numot kütüphansei ile
# import numpy as np
# duzlestiren = np.array[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# flat_duzlestiren = duzlestiren.flatten()
# print(flat_duzlestiren)

x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new =[]

def flatten(data):
    for item in data:
        if type(item) == list:
            flatten(item)
        else:
            new.append(item)

flatten(x)
print(new)


# 2) Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

liste = [[1, 2], [3, 4], [5, 6, 7]]
emptyList = []

def Reverse(liste):
    for i in liste:
        if type(i)==list:
            emptyList.append(list(reversed(i)))


Reverse([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(emptyList)))
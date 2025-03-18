import math
from math import sqrt
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# product = lambda x, y : x ** y
# print(product(3, 2))

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))


# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)



# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0


# import random as r

# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# sonlar1 = []
# for son in sonlar:
#     if son%2==0:
#         sonlar1.append(son)
# print(sonlar)
# print(sonlar1)
mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('a'),mevalar))
print(mevalar_b)

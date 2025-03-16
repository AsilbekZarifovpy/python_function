# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 20:50:05 2025

@author: asilbek
"""


# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
    
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho


# savat = []

# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break
# for a in savat:
#     print(a)






# mahsulotlar = {}

# print("Mahsulotlar ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-mahsulot ismini kiriting:"
#     mahsulot = input(savol)
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot]=narh
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break



# print(mahsulotlar)



# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while True:
#     for a in buyurtmalar:
#         if a in mahsulotlar.keys():
#             print(mahsulotlar[a])
#     break




#Functions

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")



# salom_ber("Asilbek")

# def yosh_hisobla(ism, yosh):
#     print(ism, yosh)


# yosh_hisobla(ism=input("ismingiz nma "), yosh=input("Yoshingiz nechida "))

# def hisobla(son1, son2):
#     print(f"Son1 ning Son2-darajasi {(son1**son2)} ga teng ")
    
# hisobla(son1=int(input("1-Sonni kiriting ")),son2=int(input("2-Sonni kiriting ")))


# def qoldiq(son):
#     for n in range(2,10):
#         if son%n == 0:
#             print(n)
        

# qoldiq(14)
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




# 17.03.2025


# def yosh_hisobla(ism, yosh):
#     return ism, yosh


# talaba = yosh_hisobla(ism=input("ismingiz nma "), yosh=input("Yoshingiz nechida "))

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto



# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



# def oraliq(min, max, qadam='1'):
#     sonlar = []
#     while min<=max:
#         sonlar.append(min)
#         min += int(qadam)
#     return sonlar

# son = oraliq(1,25)

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break




#1-Task

# def User(name, familyname, age, location, hometown, pheno_number=None):
#     user = {'name':name,
#             'familyname':familyname,
#             'age':age,
#             'location':location,
#             'hometown':hometown,
#             'pheno_number':pheno_number}
#     return user



# User('Asilbek', 'Zarifov', 21, 'toshkent', 'Kitob')

# print("Saytimizdagi User lar  ro'yxatini shakllantiramiz.")

# users = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     name = input("user ismi ")
#     familyname = input("user familiyasi ")
#     age = input("user yoshi ")
#     location = input("user location ni ")
#     hometown = input("user ning  hometown ")
#     pheno_number = input("user ning  pheno_number ")
#     users.append(User(name, familyname, age, location, hometown, pheno_number))
    
#     javob = input("Yana user qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
 



# def taqqosla(a,b,c):
#     if a>=b and a>=c:
#         print(a)
#     elif b>=a and b>=c:
#         print(b)
#     else:
#         print(c)
 
# taqqosla(1, 5, 3)

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar
            
    
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

    

# def katta_harf(ism):
#     kattalist = []
#     for ism2 in ism:
#         kattalist.append(ism2.capitalize())
#     return kattalist





# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi

# print(summa(1,2,35))

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')


    
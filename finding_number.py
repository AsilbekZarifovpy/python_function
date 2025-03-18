import random

def son_top(x):
    new_son = random.randint(1, x)

    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    n = 0
    while True:
        son = int(input(">>>" ))
        n += 1
        if son > new_son:
            print("Siz katta son kiritdiz ")
        elif son < new_son:
            print("Siz kichik son kiritdiz")
        else:
            print(f"Urra topdiz {n}ta urinishda, {new_son}")
            break
    return n
# son_top(10)

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar
        
# sontop_pc(10)



def yutuq(x):
    yana = True
    while yana:
        taxmin_user = son_top(x)
        taxmin_komp = sontop_pc(x)
        if taxmin_user > taxmin_komp:
            print("Siz yutdingiz Asilbek akasi")
        elif taxmin_user < taxmin_komp:
            print("Man yutdim")
        else:
            print("Dustlik G'alaba qozondi")
yutuq(10)
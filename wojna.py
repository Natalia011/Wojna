# gra wojna - wersja dla dwóch graczy

# ---- tworzenie i tasowanie talii: -------------------
import random
# kolory = ['P', 'T', 'C', 'K']
# figury = list(range(2, 15))
talia = list(range(2, 15)) * 4

# talia = []
# for i in kolory:
#     for j in figury:
#         talia.append([j, i])
random.shuffle(talia)  # symulacja tasowania
print(talia)

# ---- losowanie kart dla graczy: ----------------------
ILOSC_KART = 10
talia_gracz1 = []
talia_gracz2 = []
for k in range(ILOSC_KART):  # rozdaje 10 kart
    karta = talia[k]
    if k % 2 == 0:
        talia_gracz1.append(talia[k])
    else:
        talia_gracz2.append(talia[k])
    talia.remove(talia[k])

print(talia_gracz1)
print(talia_gracz2)
print(len(talia))

# ---- rozgrywka: ----------------------------------------
ile_kart1 = len(talia_gracz1)
ile_kart2 = len(talia_gracz2)
wojna = []
licznik_rund = 0
while ile_kart1 != 0 and ile_kart2 != 0:
    licznik_rund += 1
    k1 = talia_gracz1[0]
    k2 = talia_gracz2[0]
    talia_gracz1.pop(0)
    talia_gracz2.pop(0)
    print('Rozgrywka nr', licznik_rund, ":", k1, "vs.", k2)
    wojna.append(k1)  # karty w aktualnej rozgrywce
    wojna.append(k2)
    if k1 > k2:
        random.shuffle(wojna)
        for k in range(len(wojna)):
            talia_gracz1.append(wojna[k])
        print("Wygrywa gracz 1.")
    elif k2 > k1:
        random.shuffle(wojna)
        for k in range(len(wojna)):
            talia_gracz2.append(wojna[k])
        print("Wygrywa gracz 2.")
    else:
        continue
    wojna = []
    ile_kart1 = len(talia_gracz1)
    ile_kart2 = len(talia_gracz2)

# ---- Podsumowanie: ---------------------------------------
print(50*"-")
print('Koniec gry!')
print(f'Rozgrywka zakończyła się w {licznik_rund} rundach.')
if len(talia_gracz1) == 0:
    print("Zwycięzcą został gracz 2.")
else:
    print("Zwycięzcą został gracz 1.")

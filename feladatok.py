import math
import statistics


def fel1():
    szam = 0
    while szam != 150:
        print(szam, end=", ")
        szam += 2
    print(szam)


def fel2():
    bekeres = 0
    szamokTomb = []
    while bekeres < 11:
        tombSeged = int(input("Kérem, adjon meg egy számot (10x össz.):\t"))
        szamokTomb.append(tombSeged)
        bekeres += 1

    osszeg = 0
    for i in range(len(szamokTomb)):
        if szamokTomb[i] % 3 == 0:
            osszeg += 1
        i += 1

    print(osszeg)


def fel3():
    bekertSzam = int(input("Kérem adjon meg egy számot ami 10-el osztható: "))
    while bekertSzam % 10 != 0:
        bekertSzam = int(input("Kérem adjon meg egy számot ami 10-el osztható: "))
    print(str(bekertSzam) + " osztható 10-el.")


def fel4():
    bekertSzam = 2
    szoveg = ""
    """while bekertSzam % 2 != 0 and ((bekertSzam < -100 or bekertSzam > -9) or (bekertSzam < 9 or bekertSzam > 100)):"""
    while not (bekertSzam % 2 == 0 and ((bekertSzam > -100 and bekertSzam < -9) or (bekertSzam > 9 and bekertSzam < 100))):
        bekertSzam = int(input("Kérem adjon meg egy számot ami két számjegyű és páros: "))
        if bekertSzam < 0:
            bekertSzam *= -1
            szoveg += "-"
    szoveg += str(bekertSzam) + " a megadott kritériumok alapján elfogadott."
    print(szoveg)


def fel5():
    bekertSzam = 0
    while not ((bekertSzam > 9 and bekertSzam < 100) and bekertSzam % 2 == 1):
        bekertSzam = int(input("Kérem adjon meg egy számot ami két számjegyű és páros: "))
    print(str(bekertSzam) + " a megadott kritériumok alapján elfogadott.")


def fel6():
    bekertSzam = int(input("Kérem adjon meg egy számot: "))
    while not(bekertSzam % 3 == 0 or int(math.sqrt(bekertSzam)) == math.sqrt(bekertSzam)):
        bekertSzam = int(input("Kérem adjon meg egy számot: "))
    print(bekertSzam)


def fel7():
    a = int(input("Kérem adjon meg egy számot: "))
    b = int(input("Kérem adjon meg egy számot: "))
    c = int(input("Kérem adjon meg egy számot: "))
    while not(a + b >= c and a + c >= b and b + c >= a):
        print("Nem szerkeszthető, próbáld újra.")
        a = int(input("Kérem adjon meg egy számot: "))
        b = int(input("Kérem adjon meg egy számot: "))
        c = int(input("Kérem adjon meg egy számot: "))
    print("A háromszög megszerkeszthető.")


def fel8():
    szovegBe = str(input("Kérem, gépeljen be egy szöveget.\n\t"))
    while len(szovegBe) < 3:
        print("A szöveg túl rövid, min. 3 karakter legyen.")
        print()
        szovegBe = str(input("Kérem, gépeljen be egy szöveget.\n\t"))
    print("\n\t"+szovegBe.upper())


def fel9():
    szoveg = str(input("Kérem, gépeljen be egy szöveget.\n\t"))
    while not (szoveg == szoveg.lower() and len(szoveg) > 4):
        print("Próbáld újra, kis betűkkel, minimum 4 karaktert.")
        print()
        szoveg = str(input("Kérem, gépeljen be egy szöveget.\n\t"))


def fel10():
    szamok = []
    hozzaAdott = ""
    print("Adjon meg számokat, 0-val jelezze, hogy nem kíván többet beírni.")
    while not (hozzaAdott == 0):
        hozzaAdott = int(input("Kérem, adjon meg egy számot (0-val tud kilépni.)\t"))
        szamok.append(hozzaAdott)
    atlag = []
    for i in range(len(szamok)):
        atlag[i] = statistics.mean(i)

#1. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\penztar.txt', 'r')

#2. feladat

sor_2 = txt.readline()
vasarlasok_szama = 0

while(sor_2!=""):

    if(sor_2 == "F\n"):
        vasarlasok_szama += 1

    sor_2 = txt.readline()

print("2. feladat")
print("A fizetések száma: ", vasarlasok_szama, "\n")
txt.close()

#3. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\penztar.txt', 'r')
elso_kosar_darab = 0
vasarlasok_szama = 0
sor_3 = txt.readline()

while(vasarlasok_szama <1):

    if(sor_3 == "F\n"):
        vasarlasok_szama += 1

    # Ez a feltétel itt nem világos, a while-ciklus csak vasarlasok_szama < 1 esetben fut, konkrétan egyetlen alkalommal, amíg 0.
    # Tehát ez az if sosem kerül kiértékelésre, csak a 0. alkalommal, és akkor csak +1-gyel növeli a termékszámot ->
    # az első kosár tartalma viszont máskor változik, ha megvolt az első vásárlás, de mi van, ha több termék van (nem csak 1 db) az első vásárló kosarában? 
    if vasarlasok_szama == 1:
        elso_kosar_darab += 1

    sor_3 = txt.readline()

print("3. feladat")
print("Az első vásárló",elso_kosar_darab, "darab árucikket vásárolt. ","\n")

txt.close()

#4. feladat

print("4. feladat")
vasarlas_sorszama = input("Adja meg egy vásárlás sorszámát! ") # célszerű már itt integer-ré alakítani
arucikk_neve = input("Adja meg egy árucikk nevét! ")
darabszam = input("Adja meg a vásárolt darabszámot! ")  # célszerű már itt integer-ré alakítani
print("\n")


#5. feladat
# Ez (komplett 5. feladat) szép megoldás!
txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\penztar.txt', 'r') # többszöri újranyitásnál célszerű nem "kódba égetni" az elérési utat, hanem külön string-változóként tárolni
sor_5 = txt.readline()
sorszamok = []
arucikk_neve.lower()
arucikk_neve += "\n"
vasarlasok_szama = 1

while(sor_5!=""):

    if (sor_5 == arucikk_neve and vasarlasok_szama not in sorszamok):
        sorszamok.append(vasarlasok_szama)

    if(sor_5 == "F\n"):
        vasarlasok_szama += 1

    sor_5 = txt.readline()

print("5. feladat")
print("Az első vásárlás sorszáma: ", sorszamok[0])
print("Az utolsó vásárlás sorszáma: ", sorszamok[-1])
print(len(sorszamok),"vásárlás során vettek belőle.", "\n")


txt.close()

#6. fealadat

def ertek(p_darabszam):

    fizetendo = 0

    for i in range(int(p_darabszam)):

        kedvezmeny= min(2, i)
        fizetendo += 500 - kedvezmeny * 50


    return fizetendo

print("6. feladat")
print(darabszam, "darab vételekor fizetendő:", ertek(darabszam), "\n")


#7. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\penztar.txt', 'r')
sor_7 = txt.readline()
vasarlasok_szama = 1
termekek = {}

while (sor_7 != ""):

    if (sor_7 == "F\n"):
        vasarlasok_szama += 1

    elif int(vasarlas_sorszama) == vasarlasok_szama:

        if sor_7.strip() not in termekek.keys():
            termekek[sor_7.strip()] = 1

        else:
            termekek[sor_7.strip()] += 1

    sor_7 = txt.readline()

print("7. feladat")
for i,j in termekek.items():
    print(j, i)

txt.close()

#8. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\penztar.txt', 'r')
osszeg = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\osszeg.txt', 'w')
sor_8 = txt.readline()
adott_kosar_darab_arai = []
osszes_kosar_darabszama = []
termekek = {}

while (sor_8 != ""):

    if sor_8 == "F\n":
        vegosszeg = 0
        for a,b in termekek.items():
            adott_kosar_darab_arai.append(ertek(b))

         # ez jó for-ciklusban is, de lesz egy rövidebb módszer is....
        for c in range(len(adott_kosar_darab_arai)):
            vegosszeg += adott_kosar_darab_arai[c]

        osszeg.write(str(vegosszeg))
        osszeg.write("\n")
        adott_kosar_darab_arai = []
        termekek = {}

    elif sor_8.strip() not in termekek.keys() and sor_8 != "F\n":
        termekek[sor_8.strip()] = 1

    else:
        termekek[sor_8.strip()] += 1

    sor_8 = txt.readline()

osszeg.close()
txt.close()

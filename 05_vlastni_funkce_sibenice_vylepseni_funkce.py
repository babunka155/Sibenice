from obrazek import vykresleni   # vykreslení šibenice pomocí importu vlastního modulu
from slova import vyber_slova   # výběr slova ze samostatného modulu

def generuj_slovo():
    slovo = vyber_slova() # počítač ze seznamu vybere náhodné slovo (import vlastního modulu)
    slovo = slovo.lower()
    hadanka = "_" * len(slovo)   # aby vznikl prostor pro vyplňování hádaných písmen
    return hadanka, slovo

def nacti_pismeno(pouzite_tipy):
    while True:
        tip = input("Jaké tipuješ písmeno? ")
        tip = tip.lower()
        if tip in pouzite_tipy:   # kontrola, aby nebylo znovu zadáno písmeno, které už jednou zadané bylo
            print("Písmeno už bylo jednou zadané.")
        elif len(tip)!=1:   # aby šlo zadat přesně jeden znak
            print("Zadal jsi jiný počet znaků, než je povolený, zkus to znovu.")
        elif tip not in "aábcčdeéěfghiíjklmnoópqrřsštuůúvwxyýzž":   # aby šlo zadat pouze písmeno, jiným zpsobem by to neošetřilo české háčky??
            print("Nezadal jsi písmeno, ale jiný znak (číslice, interpunkční znaménko, atd.), zkus to znovu.")
        else:
            break
    return tip

def zamen_pismeno(slovo, hadanka, tip):
    poradi = 0
    for i in range(slovo.count(tip)):   # pokud hádané písmenko bude ve slově víckrát, tak aby se vyplnilo na všech místech
        poradi = slovo.index(tip, poradi)
        hadanka = hadanka[:poradi] + tip + hadanka[poradi+1:]
        poradi = poradi + 1
    return hadanka

def pouzite(tip, pouzite_tipy):
    if tip not in pouzite_tipy:
        pouzite_tipy.append(tip)  # doplnění tipu do seznamu použitých typů (bez ohledu na jeho úspěšnost)
    return pouzite_tipy

def konec(slovo, hadanka, vyhra, prohra):
    if "_" not in hadanka:   # celé slovo uhádnuté, vyhrál jsi
        vyhra.append(1)
        print("Vyhrál jsi, gratuluji.")
    else:
        prohra.append(1)
        print("Prohrál jsi. Hledané slovo bylo:",slovo)
    return vyhra, prohra

def sibenice():
    print("Vítej ve hře ŠIBENICE.")
    print("Tvým protihráčem bude počítač, který náhodně vybral slovo.")
    hadanka, slovo = generuj_slovo()
    print (hadanka + "\n")

    neuspesne_pokusy = 0   # začínám s 0 trestnými body
    pouzite_tipy = []   # seznam použitých typů (bez ohledu na úspěšnost)
    print("Můžeš začít hádat první písmeno.")

    while "_" in hadanka and neuspesne_pokusy<9:   # cyklus se opakuje, pokud je ještě některé písmenko neuhádnuté a zároveň ještě nezískal 9 trestných bodů
        tip = nacti_pismeno(pouzite_tipy)      
        if tip in slovo:   # když se písmeno ve slově nachází
            hadanka = zamen_pismeno(slovo, hadanka, tip)
            print(hadanka)
        else:   # tipované písmenko se ve slově nenachází
            neuspesne_pokusy = neuspesne_pokusy + 1
            print("Špatně, máš trestný bod, celkem už", neuspesne_pokusy) 
            print(vykresleni(neuspesne_pokusy)) 
            print(hadanka)        
        pouzite(tip, pouzite_tipy)
    konec(slovo, hadanka, vyhra, prohra)

# MAIN funkce
vyhra = []   # statistika výher
prohra = []   # statistika proher
while True:
    sibenice()
    pokracovani = input("Chceš pokračovat v další hře?(ano/ne)") 
    if pokracovani == "ne":
        print("Děkuji za hru.")
        print("Celková statistika tvé hry je", len(vyhra), "výher a", len(prohra), "proher z celkových", len(vyhra)+len(prohra), "her.")
        break

# načítání vykreslené šibenice přes modul nebo přes textový soubor?? jaký je mezi tím rozdíl, příklad DenisaPolesna Github přes textový soubor
# proč nedat opakování do sibenice?? nelíbi se mi, jak to vypadá
# aby se pouzite tipy nahravali jen unikatni hodnoty, jde vyřešit přes množiny, až pochopím předělám, zatím jsem to vyřešila samostatnou funkcí
# predelat, aby kontroly v nacti_pismeno probehly všechny

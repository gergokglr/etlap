vegosszeg = 0

def rendelesMain():
    global vegosszeg
    print(f"Üdvözöljük az étteremben!")
    leves()

def leves():
    global vegosszeg
    levesKerdes = input("Szeretnél kérni levest? (I/N) ")
    if levesKerdes == "I" or levesKerdes == "i":
        milyenLeves = input("Milyen levest szeretnél?" )
        if milyenLeves == "Sajtkrémleves":
            print("Sajtkémleves kiválasztva!")
            vegosszeg += 2000
            foetel()
        elif milyenLeves == "Húsleves":
            print("Húsleves kiválasztva!")
            vegosszeg += 1750
            foetel()
        elif milyenLeves == "Eperkrémleves":
            print("Eperkrémleves kiválasztva!")
            vegosszeg += 1900
            foetel()
        else:
            print("Ilyen levest nem árulunk!")
            leves()
    elif levesKerdes == "N" or levesKerdes == "n":
        foetel()
    else:
        print("Hiba: Kérem válasszon I/N közül!")
        leves()
def foetel():
    global vegosszeg
    foetelKerdes = input("Szeretnél kérni főételt? (I/N) ")
    if foetelKerdes == "I" or foetelKerdes == "i":
        milyenFoetel = input("Milyen főételt szeretnél? ")
        if milyenFoetel == "Brassói":
            print("Brassói kiválasztva!")
            vegosszeg += 2700
            desszert()
        elif milyenFoetel == "Töltött káposzta":
            print("Töltött káposzta kiválasztva!")
            vegosszeg += 2500
            desszert()
        elif milyenFoetel == "Pörkölt tarhonyával":
            print("Pörkölt tarhonyával")
            vegosszeg += 3000
            desszert()
        else:
            print("Ilyen főételt nem árulunk!")
            foetel()
    elif foetelKerdes == "N" or foetelKerdes == "n":
        desszert()
    else:
        print("Hiba! Kérem válasszon I/N közül!")
        foetel()

def desszert():
    global vegosszeg
    desszertKerdes = input("Szeretnél kérni desszertet? (I/N) ")
    if desszertKerdes == "I" or desszertKerdes == "i":
        milyenDesszert = input("Milyen desszertet szeretnél? ")
        if milyenDesszert == "Selymes Créme Brulée":
            print("Selymes Crééme Brulée kiválasztva!")
            vegosszeg += 1900
            nyugta()
        elif milyenDesszert == "Gesztenyekrém meggyel":
            print("Gesztenyekrém meggyel kiválasztva!")
            vegosszeg += 1700
            nyugta()
        elif milyenDesszert == "Palacsinta":
            print("Palacsinta kiválasztva!")
            vegosszeg += 1500
            nyugta()
        else:
            print("Ilyen desszertet nem árulunk!")
            desszert()
    elif desszertKerdes == "N" or desszertKerdes == "n":
        nyugta()
    else:
        print("Hiba! Kérem válasszon I/N közül!")
        desszert()
def nyugta():
    global vegosszeg
    print(f"Köszönjük, hogy nálunk vásárolt! {vegosszeg}Ft")
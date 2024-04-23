from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=10000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=15000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def uj_egyagyas_szoba(self, szobaszam):
        egyagyas_szoba = EgyagyasSzoba(szobaszam)
        self.add_szoba(egyagyas_szoba)

    def uj_ketagyas_szoba(self, szobaszam):
        ketagyas_szoba = KetagyasSzoba(szobaszam)
        self.add_szoba(ketagyas_szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szalloda, szobaszam, datum):
        for szoba in szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        else:
            ar = self.uj_szoba_foglalas(szalloda, szobaszam, datum)
            if ar is not None:
                return ar
            else:
                return None

    def uj_szoba_foglalas(self, szalloda, szobaszam, datum):
        for szoba in szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        else:
            print("Nincs ilyen szobaszámú szoba, új szoba létrehozása.")
            tipus = input("Add meg a szoba típusát (1 - egyágyas, 2 - kétágyas): ")
            if tipus == "1":
                szalloda.uj_egyagyas_szoba(szobaszam)
                ar = 10000
            elif tipus == "2":
                szalloda.uj_ketagyas_szoba(szobaszam)
                ar = 15000
            else:
                print("Hibás típus!")
                return None
            foglalas = Foglalas(szalloda.szobak[-1], datum)
            self.foglalasok.append(foglalas)
            return ar

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

szalloda = Szalloda("Példa Szálloda")
szalloda.add_szoba(EgyagyasSzoba(szobaszam=101))
szalloda.add_szoba(EgyagyasSzoba(szobaszam=102))
szalloda.add_szoba(KetagyasSzoba(szobaszam=201))
foglalas_kezelo = FoglalasKezelo()
foglalas_kezelo.foglalas(szalloda, 101, datetime(2024, 4, 15))
foglalas_kezelo.foglalas(szalloda, 201, datetime(2024, 4, 16))
foglalas_kezelo.foglalas(szalloda, 102, datetime(2024, 4, 17))
foglalas_kezelo.foglalas(szalloda, 102, datetime(2024, 4, 18))
foglalas_kezelo.foglalas(szalloda, 201, datetime(2024, 4, 19))


while True:
    print("\n1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("0. Kilépés")
    valasztas = input("Válassz egy műveletet: ")
   
    if valasztas == "1":
        szobaszam = int(input("Add meg a foglalandó szoba számát: "))
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("A dátum nem lehet múltbéli.")
                continue
        except ValueError:
            print("Hibás dátumformátum.")
            continue
        ar = foglalas_kezelo.foglalas(szalloda, szobaszam, datum)
        if ar is not None:
            print(f"A foglalás sikeres. Az ár: {ar}")
        else:
            print("Nincs ilyen szobaszámú szoba.")

    elif valasztas == "2":
        szobaszam = int(input("Add meg a lemondandó foglalás szoba számát: "))
        datum = input("Add meg a lemondás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            print("Hibás dátumformátum.")
            continue
        for foglalas in foglalas_kezelo.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                foglalas_kezelo.lemondas(foglalas)
                print("A foglalás sikeresen lemondva.")
                break
        else:
            print("Nincs ilyen foglalás.")

    elif valasztas == "3":
        foglalas_kezelo.listaz_foglalasok()

    elif valasztas == "0":
        print("Kilépés.")
        break

    else:
        print("Érvénytelen választás. Kérlek, válassz az elérhető lehetőségek közül.")
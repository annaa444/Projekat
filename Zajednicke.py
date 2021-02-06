import Helper
def Prijava(korisnici):
    i=0
    while i<3:
        user=input("Unesite korisnicko ime: ")
        password=input("Unesite lozinku: ")
        for korisnik in korisnici:
            if korisnik["user"]==user and korisnik["pass"]==password:
                return korisnik
        print("Pogresno korisnicko ime ili lozinka!")
        i+=1
    print("Previse puta ste pogresili lozinku ili korisnicko ime")

def PregledKnjiga(knjige):
    print("1. Ispisi sortirane")
    print("2. Ispisi nesortirane")
    opcija=input("Unesite opciju: ")
    if opcija=="2":
        Helper.StampajKnjige(knjige)
    elif opcija=="1":
        kljuc=input("Unesite po cemu zelite da sortirate[naslov|cena|izdavac|autor|kategorija]: ")
        if Helper.SortirajKnjige(knjige,kljuc):
            Helper.StampajKnjige(knjige)
        else:
            print("Niste uneli validan kljuc")
    else:
        print("Nepostojeca opcija")




def PregledAkcija(akcije,knjige):
    print("1. Ispisi sortirane")
    print("2. Ispisi nesortirane")
    opcija=input("Unesite opciju: ")
    if opcija=="2":
        Helper.StampajAkcije(akcije,knjige)
    elif opcija=="1":
        kljuc=input("Unesite po cemu zelite da sortirate[sifra|datum]: ")
        if Helper.SortirajAkcije(akcije,kljuc):
            Helper.StampajAkcije(akcije,knjige)
        else:
            print("Niste uneli validan kljuc")
    else:
        print("Nepostojeca opcija")


def PretragaKnjiga(knjige):
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu ")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji ")
    print("5. Pretraga po izdavacu ")
    print("6. Pretraga po opsegu cene ")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziKnjige(knjige,"sifra",vrednost)
        Helper.StampajKnjige(pretraga)
    elif opcija=="2":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziKnjige(knjige,"naslov",vrednost)
        Helper.StampajKnjige(pretraga)
    elif opcija=="3":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziKnjige(knjige,"autor",vrednost)
        Helper.StampajKnjige(pretraga)
    elif opcija=="4":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziKnjige(knjige,"kategorija",vrednost)
        Helper.StampajKnjige(pretraga)
    elif opcija=="5":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziKnjige(knjige,"izdavac",vrednost)
        Helper.StampajKnjige(pretraga)
    elif opcija=="6":
        donjaGranica=float(input("Unesite donju granicu cene: "))
        gornjaGranica=float(input("Unesite gornju granicu cene: "))
        vrednost=[donjaGranica, gornjaGranica]
        pretraga=Helper.PretraziKnjige(knjige,"cena",vrednost)
        Helper.StampajKnjige(pretraga)
    else:
        print("Pogresna opcija")
    

def PretragaAkcija(akcije,knjige):
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu ")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji ")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziAkcije(akcije,knjige,"sifra",int(vrednost))
        Helper.StampajAkcije(pretraga,knjige)
    elif opcija=="2":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziAkcije(akcije,knjige,"naslov",vrednost)
        Helper.StampajAkcije(pretraga,knjige)
    elif opcija=="3":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziAkcije(akcije,knjige,"autor",vrednost)
        Helper.StampajAkcije(pretraga,knjige)
    elif opcija=="4":
        vrednost=input("Unesite vrednost pretrage: ")
        pretraga=Helper.PretraziAkcije(akcije,knjige,"kategorija",vrednost)
        Helper.StampajAkcije(pretraga,knjige)
    else:
        print("Pogresna opcija")
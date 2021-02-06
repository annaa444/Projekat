import Helper
import LoadSave
import datetime
def Registracija(korisnici):
    user=input("Unesite korisnicko ime: ")
    if user=="":
        print("Polje ne sme biti prazno")
        return None
    password=input("Unesite lozinku: ")
    if password=="":
        print("Polje ne sme biti prazno")
        return None
    
    for korisnik in korisnici:
        if korisnik["user"]==user:
            print("Zauzeto korisnicko ime: ")
            return None
    ime=input("Unesite ime: ")
    if ime=="":
        print("Polje ne sme biti prazno")
        return None
    prezime=input("Unesite prezime")
    if prezime=="":
        print("Polje ne sme biti prazno")
        return None
    print("1. Prodavac")
    print("2. Menadzer")
    opcija=input("unesite opciju: ")
    while opcija!="1" and opcija!="2":
        print("1. Prodavac")
        print("2. Menadzer")
        opcija=input("unesite opciju: ")
    if opcija=="1":
        uloga="Prodavac"
    else:
        uloga="Menadzer"
    korisnik={"uloga":uloga,"user":user,"pass":password,"ime":ime,"prezime":prezime}
    korisnici.append(korisnik)

        
def PrikaziKorisnike(korisnici):
    print("1. Sortiraj po imenu")
    print("2. Sortiraj po prezimenu ")
    print("3. Sortiraj po tipu korisnika")
    print("4. Prikazi nesortirane ")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        Helper.SortirajKorisnike(korisnici,"ime")
        Helper.StampajKorisnike(korisnici)
    elif opcija=="2":
        Helper.SortirajKorisnike(korisnici,"prezime")
        Helper.StampajKorisnike(korisnici)
    elif opcija=="3":
        Helper.SortirajKorisnike(korisnici,"uloga")
        Helper.StampajKorisnike(korisnici)
    elif opcija=="4":
        Helper.StampajKorisnike(korisnici)
    else:
        print("Pogresna opcija")

def ProdajaMenu():
    print("1. Dodaj u korpu")
    print("2. Prikazi stanje korpe")
    print("3. Potvrdi kupovinu: ")
    print("4. Odustani od kupovine: ")
    opcija=input("Unesite opciju: ")
    return opcija

def DodajUKorpu(korpa,knjige,akcije):
    while True:
        print("1. Dodavanje preko sifre knjiga")
        print("2. Dodavanje preko akcija")
        print("3. Prekini dodavanje")
        opcija=input("Unesite opciju: ")
        if opcija=="1":
            Helper.StampajKnjige(knjige)
            sifra=input("Unesite sifru knjige: ")
            knjiga=Helper.NadjiKnjigu(knjige,sifra)
            if knjiga==None:
                print("Uneli ste id knjige koja ne postoji")
            else:
                kolicina=int(input("Unesite broj primeraka koji kupujete"))
                stavka={"kolicina":kolicina,"jedCena":knjiga["cena"],"sifra":knjiga["sifra"]}
                korpa.append(stavka)
        elif opcija=="2":
            Helper.StampajAkcije(akcije,knjige)
            sifra=int(input("Unesite sifru akcije: "))
            akcija=Helper.NadjiAkciju(akcije,sifra)
            if akcija==None:
                print("Uneli ste nepostojeci id!")
            elif akcija["datum"]<datetime.datetime.now():
                print("Akciji istekao rok")
            else:
                ponude=akcija["ponude"]
                for ponuda in ponude:
                    stavka={}
                    stavka["sifra"]=ponuda["sifra"]
                    stavka["kolicina"]=1
                    stavka["jedCena"]=ponuda["cena"]
                    korpa.append(stavka)
        elif opcija=="3":
            return korpa
        else:
            print("Pogresna opcija")


def Prodaja(knjige,akcije,racuni,prodavac):
    korpa=[]
    ukupna=0
    while True:
        opcija=ProdajaMenu()
        if opcija=="1":
            DodajUKorpu(korpa,knjige,akcije)
        elif opcija=="2":
            u=0
            for stavka in korpa:
                ispis=str(stavka["kolicina"])+" - "+str(stavka["jedCena"])
                u+=stavka["kolicina"]*stavka["jedCena"]
                print(ispis)
            print("Ukupna cena: "+str(u))
        
        elif opcija=="3":
            sifra=Helper.GenerisiSifruRacun(racuni)
            for stavka in korpa:
                ukupna+=stavka["jedCena"]*stavka["kolicina"]
            datum = datetime.datetime.now()
            racun={"sifra":sifra,"prodavac":prodavac["user"],"datum":datum,"stavke":korpa,"cena":ukupna}
            racuni.append(racun)
            return
        elif opcija=="4":
            print("Odustali ste od kupovine")
            return
        else:
            print("Pogresna opcija")

def DodajKnjigu(knjige):
    sifra=input("Unesite sifru knjige: ")
    naslov=input("Unesite naslov knjige: ")
    isbn=input("Unesite isbn knjige: ")
    autor=input("Unesite autora knjige: ")
    brStrana=input("Unesite broj strana: ")
    izdavac=input("Unesite izdavaca: ")
    godina=input("Unesite godinu izdanja: ")
    cena=input("Unesite cenu: ")        
    kategorija=input("Unesite kategoriju: ")
    if sifra=="" or naslov=="" or isbn=="" or autor=="" or brStrana=="" or godina=="" or cena=="" or kategorija=="" or izdavac=="":
        print("Svi podaci moraju biti uneti")
        return
    brStrana=int(brStrana)
    godina=int(godina)
    cena=float(cena)
    knjiga={"obrisan":"0","sifra":sifra,"naslov":naslov,"isbn":isbn,"autor":autor,"izdavac":izdavac,"brStrana":brStrana,"godina":godina,"cena":cena,"kategorija":kategorija}
    knjige.append(knjiga)

def IzmenaKnjige(knjige):
    Helper.StampajKnjige(knjige)
    sifra=input("Unesite sifru knjige koju menjate")
    knjiga=Helper.NadjiKnjigu(knjige,sifra)
    if knjiga==None:
        print("Uneta nepostojeca sifra!!")
        return
    naslov=input("Unesite naslov knjige: ")
    if naslov!="":
        knjiga["naslov"]=naslov
    isbn=input("Unesite isbn knjige: ")
    if isbn!="":
        knjiga["isbn"]=isbn
    autor=input("Unesite autora knjige: ")
    if autor!="":
        knjiga["autor"]=autor
    
    brStrana=input("Unesite broj strana: ")
    if brStrana!="":
        knjiga["brStrana"]=int(brStrana)
    
    izdavac=input("Unesite izdavaca: ")
    if izdavac!="":
        knjiga["izdavac"]=izdavac
    
    godina=input("Unesite godinu izdanja: ")
    if godina!="":
        knjiga["godina"]=int(godina)
    cena=input("Unesite cenu: ")    
    if cena!="":
        knjiga["cena"]=float(cena)    
    kategorija=input("Unesite kategoriju: ")
    if kategorija!="":
        knjiga["kategorija"]=kategorija
    
def ObrisiKnjigu(knjige):
    Helper.StampajKnjige(knjige)
    sifra=input("Unesite sifru knjige koju brisete: ")
    knjiga=Helper.NadjiKnjigu(knjige,sifra)
    if knjiga==None:
        print("Ne postoji knjiga sa unetom sifrom")
        return
    knjiga["obrisan"]=1
    for i in range(len(knjige)):
        if knjige[i]["sifra"]==sifra:
            del knjige[i]
    
def DodavanjeAkcije(akcije,knjige):
    sifra=Helper.GenerisiSifruAkcija(akcije)
    ponude=[]
    while True:
        print("1. Dodaj knjigu u akciju: ")
        print("2. Zavrsi dodavanje: ")
        opcija=input("Unesite opciju: ")
        if opcija=="1":
            Helper.StampajKnjige(knjige)
            sifra=input("Unesite sifru knjige")
            knjiga=Helper.NadjiKnjigu(knjige,sifra)
            if knjiga==None:
                print("Sifra ne postoji!!!")
            else:
                cena=float(input("Unesite novu cenu: "))
                ponuda={"sifra":sifra,"cena":cena}
                ponude.append(ponuda)
        elif opcija=="2":
            if len(ponude)==0:
                print("Niste dodali nijednu knjigu u akciju: ")
                return
            datumStr=input("Unesite datum vazenja akcije [dd/mm/yyyy]")
            datum=datetime.datetime.strptime(datumStr, "%d/%m/%Y")
            sifraAkcija=Helper.GenerisiSifruAkcija(akcije)
            akcija={"sifra":sifraAkcija,"ponude":ponude,"datum":datum}
            akcije.append(akcija)
            return
        else:
            print("Nepostojeca opcija")




        





def KreirajIzvestaj(knjige,racuni):
    print("1. Prodaja svih knjiga")
    print("2. Prodaja svih knjiga odabranog autora")
    print("3. Prodaja svih knjiga odabranog izdavaca")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        for knjiga in knjige:
            brojPodatih=0
            zarada=0
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        brojPodatih+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["jedCena"]
            linija="Naslov: "+knjiga["naslov"]+" | Autor: "+knjiga["autor"]+" | Broj prodatih primeraka: "+str(brojPodatih)+" | Zarada: "+str(zarada)
            print(linija)
    elif opcija=="2":
        autor=input("Unesite autora: ")
        brojPodatih=0
        zarada=0
        for knjiga in knjige:
            if knjiga["autor"].lower()!=autor.lower():
                continue
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        brojPodatih+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["jedCena"]
            linija="Naslov: "+knjiga["naslov"]+"| Autor: "+knjiga["autor"]+"| Broj prodatih primeraka: "+str(brojPodatih)+"| Zarada: "+str(zarada)
            print(linija)
    elif opcija=="3":
        izdavac=input("Unesite izdavaca" )
        brojPodatih=0
        zarada=0
        for knjiga in knjige:
            if knjiga["izdavac"].lower()!=izdavac.lower():
                continue
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        brojPodatih+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["jedCena"]
            linija="Naslov: "+knjiga["naslov"]+"| Autor: "+knjiga["autor"]+"| Broj prodatih primeraka: "+str(brojPodatih)+"| Zarada: "+str(zarada)
            print(linija)


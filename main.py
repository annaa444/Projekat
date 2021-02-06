import LoadSave
import Zajednicke
import Helper
import Posebne
korisniciFile="korisnici.txt"
knjigeFile="knjige.txt"
akcijeFile="akcije.txt"
racuniFile="racuni.txt"


korisnici=[]
knjige=[]
racuni=[]
akcije=[]

def MenadzerMenu():
    print("1. Pregled knjiga")
    print("2. Pretraga knjiga")
    print("3. Pregled akcija")
    print("4. Pretraga akcija")
    print("5. Registracija")
    print("6. Prikaz korisnika")
    print("7. Dodaj akciju")
    print("8. Kreiranje izvestaja")
    print("0. Kraj programa")
    opcija=input("Izaberite opciju: ")
    return opcija

def ProdavacMenu():
    print("1. Pregled knjiga")
    print("2. Pretraga knjiga")
    print("3. Pregled akcija")
    print("4. Pretraga akcija")
    print("5. Prodaja knjiga")
    print("6. Dodavanje knjige")
    print("7. Izmena knjige")
    print("8. Obrisi knjigu")
    print("0. Kraj programa")
    opcija=input("Izaberite opciju: ")
    return opcija

def AdministratorMenu():
    print("1. Pregled knjiga")
    print("2. Pretraga knjiga")
    print("3. Pregled akcija")
    print("4. Pretraga akcija")
    print("5. Registrqacija")
    print("6. Prikaz korisnika")
    print("7. Dodavanje knjige")
    print("8. Izmena knjige")
    print("9. Obrisi knjigu")
    print("0. Kraj programa")
    opcija=input("Izaberite opciju: ")
    return opcija

def main():
    LoadSave.loadKnjige(knjigeFile,knjige)
    LoadSave.loadKorisnici(korisniciFile,korisnici)
    LoadSave.loadAkcija(akcijeFile,akcije)
    LoadSave.loadRacuni(racuniFile,racuni)

    korisnik=Zajednicke.Prijava(korisnici)
    while korisnik==None:
        print("Neuspela prijava")
        korisnik=Zajednicke.Prijava(korisnici)
    if korisnik["uloga"].lower()=="administrator":
        while True:
            opcija=AdministratorMenu()
            if opcija=="1":
                Zajednicke.PregledKnjiga(knjige)
            elif opcija=="2":
                Zajednicke.PretragaKnjiga(knjige)
            elif opcija=="3":
                Zajednicke.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Zajednicke.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Posebne.Registracija(korisnici)
            elif opcija=="6":
                Posebne.PrikaziKorisnike(korisnici)
            elif opcija=="7":
                Posebne.DodajKnjigu(knjige)
            elif opcija=="8":
                Posebne.IzmenaKnjige(knjige)
            elif opcija=="9":
                Posebne.ObrisiKnjigu(knjige)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")
    elif korisnik["uloga"].lower()=="prodavac":
        while True:
            opcija=ProdavacMenu()
            if opcija=="1":
                Zajednicke.PregledKnjiga(knjige)
            elif opcija=="2":
                Zajednicke.PretragaKnjiga(knjige)
            elif opcija=="3":
                Zajednicke.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Zajednicke.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Posebne.Prodaja(knjige,akcije,racuni,korisnik)
            elif opcija=="6":
                Posebne.DodajKnjigu(knjige)
            elif opcija=="7":
                Posebne.IzmenaKnjige(knjige)
            elif opcija=="8":
                Posebne.ObrisiKnjigu(knjige)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")
    else:
        while True:
            opcija=MenadzerMenu()
            if opcija=="1":
                Zajednicke.PregledKnjiga(knjige)
            elif opcija=="2":
                Zajednicke.PretragaKnjiga(knjige)
            elif opcija=="3":
                Zajednicke.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Zajednicke.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Posebne.Registracija(korisnici)
            elif opcija=="6":
                Posebne.PrikaziKorisnike(korisnici)
            elif opcija=="7":
                Posebne.DodavanjeAkcije(akcije,knjige)
            elif opcija=="8":
                Posebne.KreirajIzvestaj(knjige,racuni)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")



    

    LoadSave.saveKnjige(knjigeFile,knjige)
    LoadSave.saveRacuni(racuniFile,racuni)
    LoadSave.saveKorisnici(korisniciFile,korisnici)
    LoadSave.saveAkcije(akcijeFile,akcije)
  

main()

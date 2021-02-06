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
    print("0. Krag programa")
    opcija=input("Izaberite opciju")
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


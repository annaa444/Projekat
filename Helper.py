def SortirajKnjige(knjige,kljuc):
    if kljuc!="naslov" and kljuc!="kategorija" and kljuc!="autor" and kljuc!="izdavac" and kljuc!="cena":
        return False
    for i in range(len(knjige)-1):
        for j in range(i+1,len(knjige)):
            if knjige[j][kljuc]<knjige[i][kljuc]:
                t=knjige[i]
                knjige[i]=knjige[j]
                knjige[j]=t
    return True
def StampajKnjige(knjige):
    for knjiga in knjige:
        ispis=knjiga["sifra"]+"|"+knjiga["naslov"]+"|"+knjiga["autor"]+"|"+knjiga["izdavac"]+"|"+str(knjiga["cena"])+"|"+knjiga["kategorija"]
        print(ispis)
        
def NadjiKnjigu(knjige,sifra):
    for knjiga in knjige:
        if knjiga["sifra"]==sifra:
            return knjiga
    return None
def PretraziKnjige(knjige,kljuc,vrednost):
    pretraga=[]
    for knjiga in knjige:
        if kljuc=="cena":
            if knjiga[kljuc]>=vrednost[0] and knjiga[kljuc]<=vrednost[1]:
                pretraga.append(knjiga)
        else:
            if knjiga[kljuc].lower().find(vrednost.lower())!=-1:
                pretraga.append(knjiga)
    return pretraga

def PretraziAkcije(akcije,knjige,kljuc,vrednost):
    pretraga=[]
    for akcija  in akcije:
        if kljuc=="sifra":
            if vrednost==akcija["sifra"]:
                pretraga.append(akcija)
        elif kljuc=="naslov" or kljuc=="autor" or kljuc=="kategorija":
            ponude=akcija["ponude"]
            for ponuda in ponude:
                sifra=ponuda["sifra"]
                knjiga=NadjiKnjigu(knjige,sifra)
                if knjiga[kljuc].lower().find(vrednost.lower())!=-1:
                    pretraga.append(akcija)
                    break

    return pretraga



def SortirajAkcije(akcije,kljuc):
    if kljuc!="sifra" and kljuc!="datum":
        return False
    for i in range(len(akcije)-1):
        for j in range(i+1,len(akcije)):
            if akcije[j][kljuc]<akcije[i][kljuc]:
                t=akcije[i]
                akcije[i]=akcije[j]
                akcije[j]=t
    return True

def StampajAkcije(akcije,knjige):
    for akcija in akcije:
        linija=str(akcija["sifra"])+"|"
        ponude=akcija["ponude"]
        for ponuda in ponude:
            sifra=ponuda["sifra"]
            knjiga=NadjiKnjigu(knjige,sifra)
            linija+=knjiga["naslov"]+" - "+str(ponuda["cena"])+" "
        datum=akcija["datum"]
        datumStr=datum.strftime('%d/%m/%Y')
        linija+="|"+datumStr+"\n"
        print(linija)


def SortirajKorisnike(korisnici,kljuc):
    if kljuc!="ime" and kljuc!="prezime" and kljuc!="uloga":
        return False
    for i in range(len(korisnici)-1):
        for j in range(i+1,len(korisnici)):
            if korisnici[j][kljuc]<korisnici[i][kljuc]:
                t=korisnici[i]
                korisnici[i]=korisnici[j]
                korisnici[j]=t

def NadjiAkciju(akcije,sifra):
    for akcija in akcije:
        if akcija["sifra"]==sifra:
            return akcija
    return None

def GenerisiSifruRacun(racuni):
    sifre=[]
    if len(racuni)==0:
        return 1
    for racun in racuni:
        sifre.append(racun["sifra"])
    maksSifra=max(sifre)
    return maksSifra+1

def GenerisiSifruAkcija(akcije):
    sifre=[]
    if len(akcije)==0:
        return 1
    for akcija in akcije:
        sifre.append(akcija["sifra"])
    maksSifra=max(sifre)
    return maksSifra+1

def StampajKorisnike(korisnici):
    print("****Korisnici****")
    for korisnik in korisnici:
        linija=korisnik["uloga"]+"|"+korisnik["user"]+"|"+korisnik["ime"]+"|"+korisnik["prezime"]
        print(linija)
    print("******************")

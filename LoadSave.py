import datetime
def saveKorisnici(fileName,korisnici):
    f=open(fileName,"w")
    for korisnik in korisnici:
        linija=korisnik["uloga"]+"|"+korisnik["user"]+"|"+korisnik["pass"]+"|"+korisnik["ime"]+"|"+korisnik["prezime"]+"\n"
        f.write(linija)
    f.close()

def loadKorisnici(fileName,korisnici):
    f=open(fileName,"r")
    sveLinije=f.readlines()
    for linija in sveLinije:
        delovi=linija.strip().split("|")
        korisnik={"uloga":delovi[0],"user":delovi[1],"pass":delovi[2],"ime":delovi[3],"prezime":delovi[4]}
        korisnici.append(korisnik)
    f.close()

def saveKnjige(fileName,knjige):
    f=open(fileName,"w")
    for knjiga in knjige:
        linija=knjiga["sifra"]+"|"+knjiga["naslov"]+"|"+knjiga["isbn"]+"|"+knjiga["autor"]+"|"+knjiga["izdavac"]+"|"+str(knjiga["brStrana"])+"|"+str(knjiga["godina"])+"|"+str(knjiga["cena"])+"|"+knjiga["kategorija"]+"|"+str(knjiga["obrisan"])+"\n"
        f.write(linija)
    f.close()

def loadKnjige(fileName,knjige):
    f=open(fileName,"r")
    sveLinije=f.readlines()
    for linija in sveLinije:
        delovi=linija.strip().split("|")
        if delovi[9]=="1":
            continue
        knjiga={"obrisan":0,"sifra":delovi[0],"naslov":delovi[1],"isbn":delovi[2],"autor":delovi[3],"izdavac":delovi[4],"brStrana":int(delovi[5]),"godina":int(delovi[6]),"cena":float(delovi[7]),"kategorija":delovi[8]}
        knjige.append(knjiga)
    f.close()

def loadAkcija(fileName,akcije):
    f=open(fileName,"r")
    sveLinije=f.readlines()
    for linija in sveLinije:
        listaRecnika=[]
        delovi=linija.strip().split("|")
        ponude=delovi[1].split(",")
        for ponuda in ponude:
            recnik={}
            kljucVrednost=ponuda.split("-")
            recnik["sifra"]=kljucVrednost[0]
            recnik["cena"]=float(kljucVrednost[1])
            listaRecnika.append(recnik)
        dt_object1 = datetime.datetime.strptime(delovi[2], "%d/%m/%Y")
        akcija={"sifra":int(delovi[0]),"ponude":listaRecnika,"datum":dt_object1}
        akcije.append(akcija)
    f.close()

def saveAkcije(fileName,akcije):
    f=open(fileName,"w")
    for akcija in akcije:
        linija=str(akcija["sifra"])+"|"
        ponude=akcija["ponude"]
        for ponuda in ponude:
            linija+=ponuda["sifra"]+"-"+str(ponuda["cena"])
            if ponuda["sifra"]!=ponude[len(ponude)-1]["sifra"]:
                linija+=","
        linija+="|"
        date = akcija["datum"].strftime('%d/%m/%Y')
        linija+=date+"\n"
        f.write(linija)
    f.close()
 
def loadRacuni(fileName,racuni):
    f=open(fileName,"r")
    sveLinije=f.readlines()
    for linija in sveLinije:
        delovi=linija.strip().split("|")
        sifra=int(delovi[0])
        datum = datetime.datetime.strptime(delovi[4], "%d/%m/%Y")
        stavkeRacuna=[]
        stavkeStr=delovi[2].split(",")
        for stavkaStr in stavkeStr:
            stavka={}
            parts=stavkaStr.split("-")
            stavka["sifra"]=parts[0]
            stavka["kolicina"]=int(parts[1])
            stavka["jedCena"]=float(parts[2])
            stavkeRacuna.append(stavka)
        racun={"sifra":sifra,"datum":datum,"prodavac":delovi[1],"stavke":stavkeRacuna,"cena":float(delovi[3])}
        racuni.append(racun)
    f.close()


def saveRacuni(fileName,racuni):
    f=open(fileName,"w")
    for racun in racuni:
        linija=str(racun["sifra"])+"|"+racun["prodavac"]+"|"
        stavke=racun["stavke"]
        i=0
        for stavka in stavke:
            linija+=stavka["sifra"]+"-"+str(stavka["kolicina"])+"-"+str(stavka["jedCena"])
            if i!=len(stavke)-1:
                linija+=","
            i+=1
        linija+="|"+str(racun["cena"])+"|"
        date = racun["datum"].strftime('%d/%m/%Y')
        linija+=date+"\n"
        f.write(linija)
    f.close()
class Autok:
    def __init__(self,sor):
        indulas,cel,rendszam,tel,ferohely = sor.strip().split(";")
        self.indulas = indulas
        self.cel = cel
        self.rendszam = rendszam
        self.tel = tel
        self.ferohely = int(ferohely)


class Igenyek:
    def __init__(self,sor):
        azonosito,indulas,cel,szemelyek = sor.strip().split(";")
        self.azonosito = azonosito
        self.indulas = indulas
        self.cel = cel
        self.szemelyek = int(szemelyek)
        
with open("autok.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    autok = [Autok(sor) for sor in f]
    
print(f"""2.feladat
     {len(autok)} autós hirdet fuvart""")

budapest_miskolc = sum([sor.ferohely for sor in autok if sor.indulas == "Budapest" and sor.cel == "Miskolc"])

print(f"""3.feladat
    Összesen {budapest_miskolc} férőhelyet hirdettek az autósok Budapestről Miskolcra""")

ferohelyek = [sor for sor in autok]

f = max(ferohelyek, key=lambda x:x.ferohely) 

print(f"""4.feladat
    A legtöbb férőhelyet ({f.ferohely}) a {f.indulas}-{f.cel} utvonalon
    ajánlották fel""")

with open("igenyek.csv","r",encoding="latin2") as f2:
    fejlec2 = f2.readline()
    igenyek = [Igenyek(sor) for sor in f2]

#'Indulás;Cél;Rendszám;Telefonszám;Féröhely\n'

#'Azonosító;Indulás;Cél;Személyek\n'
print("5.feladat")
for sor in igenyek:
    azonosito = sor.azonosito
    indulas = sor.indulas
    cel = sor.cel
    szemelyek = sor.szemelyek
    teljesitheto_igenyek = [print(f"    {azonosito} => {sor.rendszam}") for sor in autok if sor.indulas == indulas and sor.cel == cel and sor.ferohely >= szemelyek]
    

with open("utasuzenetek.txt","w",encoding="latin2") as f3:
    for sor in igenyek:
        azonosito = sor.azonosito
        indulas = sor.indulas
        cel = sor.cel
        szemelyek = sor.szemelyek
        for sor in autok:
            rendszam = sor.rendszam
            indulas2 = sor.indulas
            cel2 = sor.cel
            ferohelyek = sor.ferohely
            tel = sor.tel
            if indulas2 == indulas and cel2 == cel and ferohelyek >= szemelyek:
                f3.write(f"{azonosito}: Rendszám: {rendszam}, Telefonszáma: {tel}\n")
            
            
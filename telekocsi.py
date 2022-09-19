#               fuvarozo
#Indulás;      Cél;          Rendszám;         Telefonszám;            Féröhely
#   0            1               2                  3                      4

#__________________________________________________________________________________-

#             potyautasok
#Azonosító;         Indulás;         Cél;             Személyek
#   0                   1              2                 3
        
with open("autok.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    autok = [sor.strip().split(";") for sor in f]
    
print(f"""2.feladat
     {len(autok)} autós hirdet fuvart""")

budapest_miskolc = sum([int(sor[4]) for sor in autok if sor[0] == "Budapest" and sor[1] == "Miskolc"])

print(f"""3.feladat
    Összesen {budapest_miskolc} férőhelyet hirdettek az autósok Budapestről Miskolcra""")

ferohelyek = [sor for sor in autok]

f = max(ferohelyek, key=lambda x:x[4]) 

print(f"""4.feladat
    A legtöbb férőhelyet ({f[4]}) a {f[0]}-{f[1]} utvonalon
    ajánlották fel""")

with open("igenyek.csv","r",encoding="latin2") as f2:
    fejlec2 = f2.readline()
    igenyek = [sor.strip().split(";") for sor in f2]

#'Indulás;Cél;Rendszám;Telefonszám;Féröhely\n'

#'Azonosító;Indulás;Cél;Személyek\n'
print("5.feladat")
for sor in igenyek:
    azonosito = sor[0]
    indulas = sor[1]
    cel = sor[2]
    szemelyek = sor[3]
    teljesitheto_igenyek = [print(f"    {azonosito} => {sor[2]}") for sor in autok if sor[0] == indulas and sor[1] == cel and int(sor[4]) >= int(szemelyek)]
    

with open("utasuzenetek.txt","w",encoding="latin2") as f3:
    #'Azonosító;Indulás;Cél;Személyek\n'
    for sor in igenyek:
        azonosito = sor[0]
        indulas = sor[1]
        cel = sor[2]
        szemelyek = sor[3]
        for sor in autok:
            #'Indulás;Cél;Rendszám;Telefonszám;Féröhely\n'
            rendszam = sor[2]
            indulas2 = sor[0]
            cel2 = sor[1]
            ferohelyek = sor[4]
            tel = sor[3]
            if indulas2 == indulas and cel2 == cel and int(ferohelyek) >= int(szemelyek):
                f3.write(f"{azonosito}: Rendszám: {rendszam}, Telefonszáma: {tel}\n")
            #else:
                #f3.write(f"{azonosito}: Sajnos nem sikerült autót találni\n")   # valamiért ez nem müködik :(
                

            
            
            

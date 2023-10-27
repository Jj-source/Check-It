import re
import numpy as np
import pandas as pd

FILEPAGELLA = '../raw_data/pagellaPolitica_data_24092022.json'

with open(FILEPAGELLA, "r") as json_file:
    lines = json_file.readlines()
    textDate = "\"data_della_dichiarazione\": \"[0-9]* \w* [0-9][0-9][0-9][0-9]\""
    textTitle = "\"title\": {"
    withDate = 0
    articoli = 0
    for str in lines:
        x = re.findall(textDate, str)
        if(x):
            withDate+=1
        y = re.findall(textTitle, str)
        if(y):
            articoli+=1

print("articoli:", articoli)
print("con data:", withDate)
withoutDate = articoli - withDate
print("senza data:", withoutDate)
rate = withDate / withoutDate
print("con data / senza data", rate)

#now we count verdetto verboso vs verdetto sintetico
with open(FILEPAGELLA, "r") as file:
    f = file.read()

t = "\"verdetto\": {\n([ |\t])*\"testo\": \".*?\""
matches = re.finditer(t, f)
counterVerdetti = 0
for match in matches:
    counterVerdetti+= 1


#estrazione titoli per join con dataset precedente

title = "\"title\": {\n([ |\t])*\"rendered\": \".*?\""

TITOLI = "../outputs/titles.txt"
fout = open(TITOLI,"w")

matches = re.finditer(title, f)

titoli = []
for match in matches:
    #match.group(0) contains the matched
    titolo_testo = match.group(0).split("\"rendered\": ", 1)
    fout.write(titolo_testo[1] + "\n")
    titoli.append(titolo_testo[1])

print(articoli == len(titoli))
print("nuovi articoli:", len(titoli))
fout.close()

#arr = np.array(lista)

#ora il file TITOLI contiene per ogni riga un titolo
#facciamo lo stesso con il vecchio dataset
#trasformiamo entrambi gli elenchi in array numpy
#usiamo np.intersect1d(ar1, ar2) per trovare i valori uguali

FILEPAGELLAOLD = "../raw_data/pagella_politica_statements.json"
with open(FILEPAGELLAOLD, "r") as file:
    fileOld = file.read()

OLDTITOLI = "../outputs/titles_old.txt"
fout = open(TITOLI,"w")

oldTitle = "\"title\": \".*?\""
matches = re.finditer(oldTitle, fileOld)

titoliOld = []
for match in matches:
    #match.group(0) contains the matched
    titolo_testo = match.group(0).split("\"title\": ", 1)
    fout.write(titolo_testo[1] + "\n")
    titoliOld.append(titolo_testo[1])

print("old titles:", len(titoliOld))
fout.close()

#tempo di trasformarsi

arrTitoli = np.array(titoli)
arrTitoliOld = np.array(titoliOld)
titoli_comuni = np.intersect1d(titoli, titoliOld)
print("common titles:" , len(titoli_comuni))
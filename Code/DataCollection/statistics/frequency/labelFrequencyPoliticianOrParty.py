import pandas as pd
import json
import politiciansDatabase

# code used to obtain the number of truth labels
# per politician and per political party

FILEDATASET = "../archive/dataset.json"
FILEOUT = "./dataframe.json"
listaEtichette = ["Vero", "C'eri quasi", "Panzana pazzesca", "Ni"]

dataset_file = open(FILEDATASET, 'r')
dataset = json.load(dataset_file)
dataset_file.close()

tabella_giudizi = {
  "Vero" : "",
  "C'eri quasi" : "",
  "Panzana pazzesca" :  "",
  "Ni" :  ""
}

# farei sia map con giudizi per politico che per partito
# numpy array con nomi dei politici che condivide stesso index
# con altro numpy array con il dictionary dei giudizi a loro carico

arrPolitici = []
arrGiudiziPol = []
arrPartiti = []
arrGiudiziParty = []

politiciDB = politiciansDatabase.politiciansDatabase()
counter = 0

for articolo in dataset:
  key = articolo["verdict"]
  if(key in listaEtichette):
    politico = articolo["politician"]
    partito = articolo["political_party"]

    if politico == "":
      counter += 1
      continue
    if(politico in arrPolitici):
      index = arrPolitici.index(politico)
      arrGiudiziPol[index][key] += 1
    else:
      # prima volta che si incontra il politico
      arrPolitici.append(politico)
      giudizi = {"Vero" : 0, "C'eri quasi" : 0, "Panzana pazzesca" :  0, "Ni" :  0}
      giudizi[key] += 1
      arrGiudiziPol.append(giudizi)

    # ora passiamo alla parte dei partiti

    if partito is None or partito == "":
      if politiciDB.lookup(politico):
        partito = politiciDB.getParty(politico)
        print("Trovato : " + politico + " -> "+ partito)
    else:
      politiciDB.addPolitician(politico, partito)

    # abbiamo provato a trovare il partito partendo dal politico

    if(partito in arrPartiti):
      index = arrPartiti.index(partito)
      arrGiudiziParty[index][key] += 1
    else:
      # prima volta che si incontra il partito
      arrPartiti.append(partito)
      giudizi = {"Vero" : 0, "C'eri quasi" : 0, "Panzana pazzesca" :  0, "Ni" :  0}
      giudizi[key] += 1
      arrGiudiziParty.append(giudizi)


#load data into a DataFrame object:
#df = pd.DataFrame(tabella_giudizi)
dati = {}

dati["arrPolitici"] = arrPolitici
dati["arrGiudiziPol"] = arrGiudiziPol
dati["arrPartiti"] = arrPartiti
dati["arrGiudiziParty"] = arrGiudiziParty

#with open(FILEOUT, 'w') as json_file:
  #json.dump(dati, json_file, indent=2, ensure_ascii=False)
import json

# code used to eliminate copies of the same article

FILEGABRI = "../scripts/gabri1.json"

def ricerca():
  for articolo in datasetGabri:
    titolo = articolo["title"]
    if titolo in elencoTitoli:
      if titolo not in titoliDoppi:
        titoliDoppi.append(titolo)
    else:
      elencoTitoli.append(titolo)

  with open("doppi.txt", 'w') as file:
    for titolo in titoliDoppi:
      file.write(titolo)
      file.write("\n")


archivio_file = open(FILEGABRI, 'r')
datasetGabri = json.load(archivio_file)
archivio_file.close()

elencoTitoli = []
titoliDoppi = []
ricerca()
doppi = len(titoliDoppi)

# 194 duplicati individuati il 16 marzo 2023
# procedo a creazione dataset di copia privo di duplicati
new_dataset = []
for articolo in datasetGabri:
  titolo = articolo["title"]
  if titolo not in titoliDoppi:
    new_dataset.append(articolo)
  else:
    titoliDoppi.remove(titolo)
    # così al secondo incontro lo aggiungerà al nuovo dataset

with open("../archive/dataset_gabri.json", 'w') as json_file:
  json.dump(new_dataset, json_file, indent=2, ensure_ascii=False)

print(len(new_dataset) == len(datasetGabri) - doppi)
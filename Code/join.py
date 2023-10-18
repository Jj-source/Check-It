import json
import articleObj

# code used to join the older dataset 'Gabri'
# and the recent one 'Pagella'

FILEGABRI = "../archive/dataset_gabri.json"
PATHPAGELLA = "../archive/dataset/etichette_normalizzate/"
PATHJOIN = "../archive/dataset/etichette_normalizzate/join_"

archivio_file = open(FILEGABRI, 'r')
datasetGabri = json.load(archivio_file)
archivio_file.close()

pagella_file = open(PATHPAGELLA + "d2.json", 'r')
datasetJacopo = json.load(pagella_file)
pagella_file.close()

elencoTitoli = []
for articolo in datasetJacopo:
  elencoTitoli.append(articolo["title"])

# now, let's just check how many articles we have in common.
counter = 0
for articolo in datasetGabri:
  if articolo["title"] in elencoTitoli:
    counter += 1

print("JOIN d2")
print("articles in modern dataset:" + str(len(datasetJacopo)))
print("articles in old dataset:" + str(len(datasetGabri)))
print("common ones: "  + str(counter))

len_originale = len(datasetJacopo)

# damn. 1326 articoli comuni.
# verranno esclusi dal join

# un article di gabriele ha questa composizione:
# url
# title
# content
# politician
# verdict
# statement
# publish_date
# source_date
# source
# macro_area
# tags
# links

new_id = len(datasetJacopo)+1

for articolo in datasetGabri:
  if articolo["title"] not in elencoTitoli:
    if articolo["verdict"] == "Ni":
      articolo["verdict"] = "Nì"
    nuovo_articolo = {
      "id" : new_id,
      "date": articolo["publish_date"],
      "link": articolo["url"],
      "title": articolo["title"],
      "content": articolo["content"],
      "statement_date": articolo["source_date"],
      "source": articolo["source"],
      "statement" : articolo["statement"],
      "verdict": articleObj.remove_html_tags(articolo["verdict"]),
      "verdict_ext": "",
      "politician": articolo["politician"],
      "political_party": "",                                      # utile pensare al politiciansDatabbase per riempire questo campo
      "piattaforma": "",                                           # parzialmente riempibile estraendo contenuto link da "source"
      "politicians_in": "",
      "macro_area": articolo["macro_area"],
      "tags": articleObj.formatting_tags(articolo["tags"]),
      "links": articolo["links"],
      "versione": 4
    }
    datasetJacopo.append(nuovo_articolo)
    new_id += 1

for articolo in datasetGabri:
  if articolo["title"] in elencoTitoli:
    for articolo_mio in datasetJacopo:
      if articolo_mio["title"] == articolo["title"]:
        articolo_mio["date"] = articolo["publish_date"]
        articolo_mio["links"] = articolo["links"]
        articolo_mio["tags"] = articolo["tags"]
        articolo_mio["macro_area"] = articolo["macro_area"]
        if(articolo_mio["statement_date"] == ""):
          articolo_mio["statement_date"] = articolo["source_date"]
        if(articolo_mio["source"] == ""):
          articolo_mio["source"] = articolo["source"]
        if(articolo_mio["statement"] == ""):
          articolo_mio["statement"] = articolo["statement"]
        if(articolo_mio["politician"] == ""):
          articolo_mio["politician"] = articolo["politician"]

for articolo in datasetGabri:
  if(articolo["political_party"] == ""):
    p = articolo["politician"]
    if(p == "giorgia meloni"):
      articolo["political_party"] = "fratelli d'italia"
    elif(p == "matteo salvini"):
      articolo["political_party"] = "lega nord"
    elif(p == "giuseppe conte"):
      articolo["political_party"] = "movimento 5 stelle"

with open(PATHJOIN+ "d2.json", 'w') as json_file:
  json.dump(datasetJacopo, json_file, indent=2, ensure_ascii=False)

print(len(datasetJacopo) == len(datasetGabri) + len_originale - counter)

# successo!
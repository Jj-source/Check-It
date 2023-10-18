import json
import re

def normalizzazione_etichette(articolo):
  
  if articolo["verdict"] == "nì" or articolo["verdict"] == "C'eri quasi":
    articolo["verdict"] = "Nì"
  elif re.search("((P|p)anzana pazzesca)|((P|p)inocchio)|sbaglia( \.|\.)|fuorviante|esagera", articolo["verdict"]) is not None or re.search("torto|omette|scorretta|non è (supportat|confermat)|imprecis|non (è corrett|ha ragione)|confusione|confonde|sment|sbaglia|eccessiv(o|a)", articolo["verdict"]) is not None:
    articolo["verdict"] = "Falso"
  elif re.search("[^s]corrett(a|o)\.|ragione\.", articolo["verdict"]) is not None or re.search("danno ragione|sostanzialmente (ragione|corretto)|cita correttamente|verità| corrett(o|i|a)[^ ,]|ha ragione[^ ,]|giusta\.|fondat(e|i)", articolo["verdict"]) is not None or re.search("corrett(o|i|e|a)\.|sostanzialmente", articolo["verdict"]) is not None:
    if re.search("non è corrett(a|o)\.|non ha ragione\.|più o meno|quasi (ragione|corretto)|impreciso", articolo["verdict"]) is None:
      articolo["verdict"] = "Vero"
  elif re.search("a metà|in parte", articolo["verdict"]) is not None:
    articolo["verdict"] = "Nì"

#danno ragione|sostanzialmente (ragione|corretto)|cita correttamente

PATHIN = "../archive/dataset/after_pipeline_stanza/"
PATHOUT = "../archive/dataset/etichette_normalizzate/"
files = ["d1", "d2", "d3", "join_d1", "join_d2"]
files2 = ["d1", "d2", "d3", "join_d1"]
files3 = ["join_d2"]
verdetti = ["Vero", "Nì", "Falso"]

def riduzione():
  for file_name in files:
    file = open(PATHIN + file_name + ".json", 'r')
    data = json.load(file)
    file.close()
    for articolo in data:
      normalizzazione_etichette(articolo)

    with open(PATHOUT + file_name + ".json", 'w') as json_file:
      json.dump(data, json_file, indent=2, ensure_ascii=False)

def copia_accorciamento():
  with open(PATHOUT + "join_d2.json", 'r') as file_corretto:
    data_corretti = json.load(file_corretto)

  for file_name in files2:
    file = open(PATHOUT + file_name + ".json", 'r')
    data = json.load(file)
    file.close()
    for art in data:
      if(art["verdict"] not in verdetti):
        for art2 in data_corretti:
          if(art["title"] == art2["title"]):
            art["verdict"] = art2["verdict"]

    with open(PATHOUT + file_name + ".json", 'w') as json_file:
      json.dump(data, json_file, indent=2, ensure_ascii=False)

def fill_partito(data):
  for articolo in data:
    if(articolo["political_party" == ""]):
      pol = articolo["politician"]
      if(pol == "Matteo Salvini"):
        articolo["political_party"] = "Lega Nord"
        articolo["versione"] += .1
      elif(pol == "Giorgia Meloni"):
        articolo["political_party"] = "Fratelli d'Italia"
        articolo["versione"] += .1
      elif(pol == "Silvio Berlusconi"):
        articolo["political_party"] = "Forza Italia"
        articolo["versione"] += .1

copia_accorciamento()
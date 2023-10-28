import json
import re

PATH = "../../archive/dataset/after_pipeline_stanza/"
PATHIN = "../../archive/dataset/etichette_normalizzate/"
files = ["d1", "d2", "d3", "join_d1", "join_d2"]
files2 = ["join_d2"]
FREQ = "./freq.txt"

with open(FREQ, 'w') as file:
  for file_name in files:
    f = open(PATHIN + file_name + ".json", 'r')
    data = json.load(f)
    f.close()
    
    file.write(file_name + " : " + str(len(data)) + "\n")

    etichette = {}
    for articolo in data:
      key = articolo["verdict"]
      if(key not in etichette):
        etichette[key] = 1
      else:
        etichette[key] += 1

    file.write("\n")
    lunghe = 0
    for key in etichette:
      if(etichette[key]>0):
        file.write(key + ": " + str(etichette[key]) + "\n")
      else:
        lunghe+=1
    file.write("etichette lunghe: " + str(lunghe) + "\n")
    file.write("--------\n\n")

## marzo 2023

# 5414 articoli

# Vero :  1990
# C'eri quasi :  1902
# Panzana pazzesca :  889
# Ni :  387
# etichette lunghe:  219


# automatically change "ha ragione" (e non "ha ragione a metà") to vero
# e se alla fine del content dice "merita una panzana pazzesca" fagli aggiungere panzana pazzesca
# idem con altre etichette

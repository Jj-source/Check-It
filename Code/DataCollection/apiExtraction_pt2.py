import json
import articleObj
from bs4 import BeautifulSoup

# Link making: extraction of links from the body of the articles
# and creation of the link list
# Ordering of ids: rewriting ids in each dataset version to be in order
# (Same article can have different ids based on the dataset version)

D2 = '../archive/n/d2.json'
D1 = '../archive/n/d1.json'
D3 = '../archive/n/d3.json'
CONTENTFILE = "../archive/contents.json"
OUT = "../archive/n/o/"

with open(CONTENTFILE, "r", encoding='utf-8') as file:
  contents = json.load(file)
with open(D3, "r", encoding='utf-8') as file:
  d3 = json.load(file)
#with open(D1, "r", encoding='utf-8') as file:
  #d1 = json.load(file)
#with open(D2, "r", encoding='utf-8') as file:
  #d2 = json.load(file)
#per ognuno dei tre dataset devo fare estrazione link

def link_making(dataset):
  new_dataset = []
  for idx in range(len(dataset)):
    id_articolo = dataset[idx]["id"]
    content = contents[id_articolo]
    soup = BeautifulSoup(content["content"], 'html.parser')
    urls = []
    for data in soup('a'):
      try:
        urls.append(data['href'])
      except:
        urls.append("url not available")

    article = articleObj.openDictionary(dataset[idx])
    article.linksExtraction(urls)
    new_dataset.append(article.dictionary())
  return new_dataset

### rewriting ids to be in order and final print
finalDataset_v3 = link_making(d3)
#finalDataset_v1 = link_making(d1)
#finalDataset_v2 = link_making(d2)

def finalstep(dataset, name):
  indice = 0
  for el in dataset:
    el["id"] = indice
    indice += 1
  with open(OUT + name +".json", 'w') as json_file:
    json.dump(dataset, json_file, indent=2, ensure_ascii=False)

finalstep(finalDataset_v3, "d3")
#finalstep(finalDataset_v1, "d1")
#with open(OUT + "d2.json", 'w') as json_file:
  #json.dump(finalDataset_v2, json_file, indent=2, ensure_ascii=False)
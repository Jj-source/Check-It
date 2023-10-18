import json
import articleObj

# extraction of the content of the articles
# needed for future link making
    
APIFILE = '../archive/request_cruda_v2.json'
CONTENTFILE = "../archive/contents.json"

apiContent = open(APIFILE, "r")
dataArc = json.load(apiContent)
apiContent.close()

dataset = []

class contentObj:
  def __init__(self, id, content):
    self.id = id
    self.content = content

  def dictionary(self):
    dictionary = {
      "id" : self.id,
      "content": self.content,
    }
    return dictionary
  
id_postumo = 0
for article in dataArc:
  content = []
  try:
    if type(article["acf"]["editor"]) != bool:
      for elemento in article["acf"]["editor"]:
        if elemento["acf_fc_layout"] == "paragrafo" :
          content.append(elemento["testo"])
  except:
    pass
  try:
    len(content[0])
  except: #se fallisce è perchè content è vuoto
    try:
      content = []
      content.append(article["content"]["rendered"])
    except:
      content = []

  obj = contentObj(id_postumo, articleObj.bonifica(' '.join(content)))
  dataset.append(obj.dictionary())
  id_postumo += 1

with open(CONTENTFILE, 'w') as json_file:
  json.dump(dataset, json_file, indent=2, ensure_ascii=False)
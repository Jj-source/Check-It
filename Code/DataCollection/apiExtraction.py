import json
import articleObj

# Creation of articles

OUT2 = '../archive/dataset_v2.json'
OUT1 = '../archive/dataset_v1.json'
OUT3 = '../archive/dataset_v3.json'
APIFILE = '../archive/request_cruda_v2.json'
CONTENTFILE = "../archive/contents.json"

#number of articles
conteggio = 0

# define empy list: our dataset!
dataset = []
# id var to replace missing ids
idPostMortem = 0
# list of article obj to set chronological order id

apiContent = open(APIFILE, "r")
dataArc = json.load(apiContent)
apiContent.close()
for article in dataArc:
  #to have an article object we are going to need all of its parameters:
  #"id" 
  #"date"
  #"link"
  #"title"
  #"content"
  #"statement_date"
  #"source" 
  #"statement"
  #"verdict"
  #"verdict_ext"
  #"politician"
  #"political_party"
  #"piattaforma"
  #"politicians_in"
  #"macro_area"
  #"tags"
  #"links" : not needed in some cases as it is created from text, but older articles may have it
  #we can manipulate singular articles
  #"versione": added attribute to split the data in different groups based on the amount of information they contain
  #            dataset versions are explained in the readme file !
        
  date = article["date"]
  link = article["link"]
  title = article["title"]["rendered"]

  content = []
  primo_paragrafo = True
  try:
    if type(article["acf"]["editor"]) != bool:
      for elemento in article["acf"]["editor"]:
        if elemento["acf_fc_layout"] == "paragrafo":
          if primo_paragrafo:
            primo_paragrafo = False
          elif elemento["titolo"]  != "Il verdetto":
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

  try:
    statement_date = article["acf"]["data_della_dichiarazione"]
  except:
    statement_date = ""
  try:
    source = article["acf"]["link"]
  except:
    source = ""
        
  try:
    statement = article["acf"]["sentenza"]
  except:
    statement = article["title"]["rendered"]

  try:
    verdict = article["acf"]["verdetto"]["testo"]
  except:
    verdict = ""

  try:
    verdict_ext = []
    if(type(article["acf"]["verdetto"]["in_breve"]) != bool):
      for testo in article["acf"]["verdetto"]["in_breve"]:
        verdict_ext.append(testo["testo"])
    else:
      verdict_ext = ""
  except:
    verdict_ext = ""

  try:
    politician = article["acf"]["politico"]["post_title"]
  except:
    politician = ""
  try:
    political_party = article["acf"]["politico"]["partito"]
  except:
    political_party = ""
  try:
    piattaforma = article["acf"]["immagine_credits"]
  except:
    piattaforma = ""                
                
  try:
    if type(article["acf"]["politici_in"]) != bool:
      politicians_in = []
      for politico in article["acf"]["politici_in"]:
        politician = politico["post_title"]
        try:
          political_party = politico["partito"]
        except:
          political_party = ""
        politiconew = {"name" : politician,"party" : political_party}
        politicians_in.append(politiconew)
    else:
      politicians_in = ""                          
  except:
    politicians_in = "" 

  macro_area = "" #only in old articles

  try:
    tags = article["slug"]
  except:
    print("no tags")

  try:
    article["acf"]["sentenza"]
    article["acf"]["politico"]["post_title"]
    article["acf"]["politico"]["partito"]
    if(article["acf"]["immagine_credits"]!="" and article["acf"]["link"]!=""):
      versione = 3
    else:
      versione = 1
  except:
    try:
      article["acf"]["sentenza"]
      article["acf"]["politico"]["post_title"]
      versione = 1
    except:
      #if it failed, questo articolo manca di statement e farà parte solo della seconda versione del dataset
      versione = 2



  #now we can create our article object:
  empty_list = []
  articolo = articleObj.articleObj(idPostMortem, date, link, title, ' '.join(content), statement_date, source, statement, verdict, verdict_ext, politician, political_party, piattaforma, politicians_in, macro_area, tags, empty_list, versione)
  
  articolo.contentElaboration()
  # append it's dictionary version to our dataset
  dataset.append(articolo.dictionary())
  idPostMortem += 1

finalDataset_v2 = dataset
finalDataset_v1 = []
finalDataset_v3 = []

#finalDataset_v2[:] = [x for x in finalDataset_v2 if x["versione"]==1]
finalDataset_v1 = [x for x in finalDataset_v2 if (x["versione"]==1 or x["versione"]==3)]
finalDataset_v3 = [x for x in finalDataset_v2 if x["versione"]==3]

with open(OUT1, 'w') as json_file:
  json.dump(finalDataset_v1, json_file, indent=2, ensure_ascii=False)
with open(OUT3, 'w') as json_file:
  json.dump(finalDataset_v3, json_file, indent=2, ensure_ascii=False)
with open(OUT2, 'w') as json_file:
  json.dump(finalDataset_v2, json_file, indent=2, ensure_ascii=False)
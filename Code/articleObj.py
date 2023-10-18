import re
import linkObj
from bs4 import BeautifulSoup, Comment

class articleObj:
  def __init__(self, id, data, link, title, content, statement_date, source, statement, verdict, verdict_ext, politician, political_party, piattaforma, politicians_in, macro_area, tags, links, v):
    self.id = id
    self.date = data
    self.link = link
    self.title = bonifica(title)
    self.content = content
    self.statement_date = statement_date
    self.source = source
    self.statement = bonifica(statement)
    self.verdict = verdict
    self.verdict_ext = verdict_ext
    self.politician = politician
    self.political_party = political_party
    self.piattaforma = piattaforma
    self.politicians_in = politicians_in
    self.macro_area = macro_area
    self.tags = formatting_tags(tags)
    self.links = links
    self.versione = v

  def dictionary(self):
    dictionary = {
      "id" : self.id,
      "date": self.date,
      "link": self.link,
      "title": self.title,
      "content": self.content,
      "statement_date": self.statement_date,
      "source": self.source,
      "statement" : self.statement,
      "verdict": self.verdict,
      "verdict_ext": self.verdict_ext,
      "politician": self.politician,
      "political_party": self.political_party,
      "piattaforma": self.piattaforma,
      "politicians_in": self.politicians_in,
      "macro_area": self.macro_area,
      "tags": self.tags,
      "links": dictionary_list(self.links),
      "versione": self.versione
    }
    return dictionary
  
  def contentElaboration(self):
    self.content = bonificaContent(self.content)

  def getV(self):
    return self.versione

  def linksExtraction(self, links_from_content):
    # substitute a link in the article content with an easy identifiable and uncommon character,
    # for example [LINK!] could be a good choice
    ## what if I add also the number of words in the tag to avoid half of this
    # we can then split the content based on . to form phrases.
    # from contents.json we can still see the link tags and extract from there the link content.
    # we do this to form a list of the contents.
    # we iterate, so that the list order is the same order in which we will find those words in the phrases
    # we count words and phrases to build the right linkObj.
    elencoLinks = []
    frase = 0
    for riga in self.content:
      words = riga.split(" ")
      link_counter = 0
      for indice in range(len(words)):
        if words[indice] == "[LINK":
          inizio = indice - 3 * link_counter     #ogni link trovato è preceduto da tre stringhe: "[LINK!" "numero" "]"
                                                  #queste verranno tolte e quindi vanno sottratte dal conteggio parole
          fine = int(words[indice+1]) + 1
          elencoLinks.append(linkObj.linkObj(links_from_content[len(elencoLinks)], frase, inizio, fine))
          link_counter += 1
      frase += 1
    self.links = elencoLinks

    if(len(self.content)==1):
      self.content = re.sub("\[LINK \d+ \]", "", self.content)
    else:
      nuovo_content = []
      for riga in self.content:
        nuovo_content.append(re.sub(' +', ' ', re.sub("\[LINK \d+ \]", "", riga)))
      self.content = nuovo_content

def bonifica(txt):
  soup = BeautifulSoup(txt, 'html.parser')
  for element in soup(text=lambda text: isinstance(text, Comment)):
    element.extract()
  for data in soup(['div', 'br', 'span', 'i', 'b', 'p', 'em', 'u', 'img', 'hr', "ul", "li", "blockquote", "table", "tbody", "td", "tr", "iframe", "script"]):
    data = data.unwrap()
  txt = remove_recurrent_phrases(txt)
  txt = punteggiatura(txt)
  txt = remove_tabs(txt)
  return txt

def bonificaContent(txt):
  txt = remove_recurrent_phrases(txt)
  txt = remove_html_tags(txt)
  txt = remove_tabs(txt)
  return re.sub(' +', ' ', dots(txt))

def remove_recurrent_phrases(txt):
  txt = re.sub("Ti è piaciuta l'analisi?", "", txt)
  return re.sub(r"http\S+", "", txt)

def dots(txt):
  if re.search("www\.[^ ] ", txt) is not None:
    link_abusivo = re.search("www\.[^ ] ", txt).group(0)
    #re.sub(link_abusivo, "[LINK ABUSIVO]" + redatto + "[FINE]", txt)
    re.sub(link_abusivo, "", txt)
  return txt

def remove_html_tags(txt):
  soup = BeautifulSoup(txt, 'html.parser')
  for data in soup('strong'): #used as titles so not usefull to keep
    data.decompose()
  for element in soup(text=lambda text: isinstance(text, Comment)):
    element.extract()
  for data in soup('div', {'class':'sharethefacts_microdata_embed'}):
    data.decompose()
  for data in soup(['div', 'br', 'span', 'i', 'b', 'p', 'em', 'u', 'img', 'hr', "ul", "li", "blockquote", "table", "tbody", "td", "tr", "iframe", "script"]):
    data = data.unwrap()
  for data in soup('a'):
    leng = data.text.count(" ")
    data.insert_before(" [LINK " + str(leng) + " ] ")
    data = data.unwrap()
  return str(soup)
    
def remove_tabs(txt):
  txt = re.sub('\n|\t|\a|\r', '', txt)   #\n lo tengo per vedere se ha effetti sul sentence splitter del docente
  txt = re.sub("&nbsp;", " ", txt)
  txt = re.sub(r"\\n", '', txt)
  return re.sub(' +', ' ', txt)

def punteggiatura(txt):
  txt = re.sub(r" , ", ", ", txt)
  txt = re.sub(r" ; ", "; ", txt)
  txt = re.sub(r" : ", ": ", txt)
  txt = re.sub(r" ! ", "! ", txt)
  txt = re.sub(r" \. ", ". ", txt)
  txt = re.sub("(?<=[^ ])<", " <", txt)
  txt = re.sub("> ", ">", txt)          #tutti attaccati, poi stacca quelli del begin tag e non dell'end tag
  return re.sub(r" \? ", "? ", txt)

def dictionary_list(list):
  new_list = []
  for link in list:
    new_list.append(link.json_ser())
  return new_list

def formatting_tags(tags):
  if type(tags) != list: 
    words = re.findall("-[^-]*", tags) # is it a combination of words separeted by '-' ?
    if len(words) > 0 :
      return tags.split("-")  # returns an array of words, splitting every '-'
  return tags

def openDictionary(dict):
  articolo = articleObj(
    dict["id"],
    dict["date"],
    dict["link"],
    dict["title"],
    dict["content"],
    dict["statement_date"],
    dict["source"],
    dict["statement"],
    dict["verdict"],
    dict["verdict_ext"],
    dict["politician"],
    dict["political_party"],
    dict["piattaforma"],
    dict["politicians_in"],
    dict["macro_area"],
    dict["tags"],
    dict["links"],
    dict["versione"]
  )
  return articolo

#def checkPolitician(text):
  ### how to efficiently find people's name in text??
  ### neural network to recognise names in text?
  # will have to look this up

### 16 gen
## create a catalog of politicians found in the tags "politician" and "political_party"
# for every article inspect the content and the statement looking for matches: this could fill
# the field politicians_in in articles that don't have it naturally filled.
## be sure that the "tags" field is formatted well: not one singular string with words separeted
# by '-' but an array of string?
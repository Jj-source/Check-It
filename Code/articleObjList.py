import articleObj

# request is in reverse cronological order
# if we put Id in that order, as soon as a new article is added
# the ids will be shifted, and there's no way of knowing when
# this could happen
# so we make a list of articleObj, nodes with a this = articleObj
# and a next pointer to the previous articleObj.
# when we finish the extraction in api2.py, we go throught it and start
# putting id from the oldest

class ArticleObjNode:
  def __init__(self, articleObj):
    self.this = articleObj
    self.next = None
    self.previous = None

  def setNext(self, Node):
    self.next = Node
  
  def setPrev(self, Node):
    self.previous = Node

  def getArticle(self):
    return self.this
  def getNext(self):
    return self.next
  def getPrev(self):
    return self.previous
  

class ArticleObjList:
  def __init__(self):
    self.first = None
    self.last = None

  def setLast(self, node):
    self.last = node
  def setFirst(self, node):
    self.first = node
  def getFirst(self):
    return self.first
  def getLast(self):
    return self.last

  def add(self, articleObj):
    node = ArticleObjNode(articleObj)
    node.setNext(self.getFirst())
    self.setFirst(node)

  def addLinked(self, articleObj):
    node = ArticleObjNode(articleObj)
    if self.getFirst() is None:
      self.setFirst(node)
      self.setLast(node)
    else:
      self.getLast().setNext(node)
      node.setPrev(self.getLast())
      self.setLast(node)



#let's try?

#testo = ["<p>\n\t L&#8217;emergenza umanitaria in Siria ha coinvolto circa 2 milioni di persone, di cui <a href=\"http://www.corriere.it/esteri/12_agosto_14/siria-emergenza-umanitaria-sottosegretario-onu_727bf8d2-e5f0-11e1-aa1f-b3596ab6a873.shtml%20\" target=\"_blank\" rel=\"noopener\">1 milione e mezzo hanno abbandonato le proprie case </a>. Il <a href=\"http://vdc-sy.org/index.php/en/\" target=\"_blank\" rel=\"noopener\">Center of Documentation of Violations in Syria</a>, in contatto con gli attivisti, denuncia oltre 26mila vittime e più di 3mila prigionieri dall&#8217;inizio della rivoluzione. Il Syrian Documents Center, vicino al regime, si limita a segnalare invece circa 5mila vittime.\n</p>"]


#id = "id"
#date = "data"
#link = "link"
#title = "bonifica(title)"
#content = testo
#statement_date = "statement_date"
#source = "source"
#statement = "bonifica(statement)"
#verdict = "verdict"
#verdict_ext = "verdict_ext"
#politician = "politician"
#political_party = "political_party"
#piattaforma = "piattaforma"
#politicians_in = "politicians_in"
#macro_area = "macro_area"
#tags = "formatting_tags(tags)"

#articolo = articleObj.articleObj(id, date, link, title, ' '.join(content), statement_date, source, statement, verdict, verdict_ext, politician, political_party, piattaforma, politicians_in, macro_area, tags)


#list = ArticleObjList()
#print(type(list.first))
#list.add(articolo)
#print(type(list.first))
#print(list.first.this.date)

# it works!
import json
#link {
#   "url": "",
#   "phraseIdx" : number of the phrase of content in which the link appears
#   "beginIdx" : word index of first word linked to the link
#   "lenght" :  number of words linked to the link
# }

class linkObj:
    def __init__(self, url, phraseIdx, beginIdx, lenght):
        self.url = url
        self.phraseIdx = phraseIdx
        self.beginIdx = beginIdx
        self.lenght = lenght

    def json_ser(self):
      dictionary = {
        "url": self.url,
        "phraseIdx" : self.phraseIdx,
        "beginIdx" : self.beginIdx,
        "lenght": self.lenght
      }
      return dictionary

    def __str__(self):
        return "url: " + self.url + " " + "(" + str(self.phraseIdx) + ", " + str(self.beginIdx) + ", " + str(self.lenght) + ")\n"
import re
import numpy as np
from datetime import datetime
from codice.statistics.frequency.plot import *

FILEPAGELLA = '../raw_data/pagellaPolitica_data_24092022.json'
FILEPAG = "../raw_data/dictionariesPag/pag2.json"

with open(FILEPAGELLA, "r") as json_file:
    #unable to open it as json: more than 1 dictionary
    #data = json.load(json_file)
    #raccolta date
    lines = json_file.readlines()
    text = "\"data_della_dichiarazione\": \"[0-9]* \w* [0-9][0-9][0-9][0-9]\""
    listDateObj = []
    for str in lines:
        x = re.findall(text, str)
        if(x):
            x[0] = x[0].lower()
            x[0]=x[0].replace("\"data_della_dichiarazione\": \"","")
            x[0]=x[0].replace("\"","")
            x[0]=x[0].replace("\"","")
            x[0]=x[0].replace(" gennaio ","-01-")
            x[0]=x[0].replace(" febbraio ","-02-")
            x[0]=x[0].replace(" marzo ","-03-")
            x[0]=x[0].replace(" aprile ","-04-")
            x[0]=x[0].replace(" maggio ","-05-")
            x[0]=x[0].replace(" giugno ","-06-")
            x[0]=x[0].replace(" luglio ","-07-")
            x[0]=x[0].replace(" agosto ","-08-")
            x[0]=x[0].replace(" settembre ","-09-")
            x[0]=x[0].replace(" ottobre ","-10-")
            x[0]=x[0].replace(" novembre ","-11-")
            x[0]=x[0].replace(" dicembre ","-12-")

            #converting string to date obj
            datetime_object = datetime.strptime(x[0], "%d-%m-%Y")
            #creating array of date objs
            listDateObj.append(datetime_object)

print("number of dates found" , len(listDateObj))

#listDateObj is made of elements like this: %d-%m-%y (00-00-0000)
#from the date objs array we get the string out to
#trasform from d-m-y to y-m-d -> YYYY-MM-DD
#having a dateobjs array could be useful for future applications

listaAnnoMeseGiorno = []
for str in listDateObj:
    newFormat = str.strftime('%Y/%m/%d')
    listaAnnoMeseGiorno.append(newFormat)

#we convert it to array Year Month Day in numpy
arrYMD = np.array(listaAnnoMeseGiorno)

#creating couples with unique value (a date) and count of frequency
uniqueDAY, countsDAY = np.unique(arrYMD, return_counts=True)

#plotting per day
#plotting("Frequency per day", "day", "number of statements", uniqueDAY, countsDAY)

#per month and year
listaAnnoMese = []
for mese in arrYMD:
    #rsplit is same as split but starting from the end of the string
    #we split every string in the list at the last '/', keeping the first part therefore cutting out the day
    data = mese.rsplit("/", 1)
    listaAnnoMese.append(data[0])

#again numpy array
arrAnnoMese = np.array(listaAnnoMese)

uniqueYM, countsYM = np.unique(arrAnnoMese, return_counts=True)
#plotting("Frequency per month", "month", "number of statements", uniqueYM, countsYM)

#now only for year
listaAnno = []
for anno in arrYMD:
    #we split every string in the list at the first '/', cutting out the day
    data = anno.split("/", 1)
    listaAnno.append(data[0])

#again numpy array
arrAnno = np.array(listaAnno)

uniqueY, countsY = np.unique(arrAnno, return_counts=True)
# plotting("Frequency per year", "year", "number of statements", uniqueY, countsY)
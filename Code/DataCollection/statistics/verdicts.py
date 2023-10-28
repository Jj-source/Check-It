import re

FILEPAGELLA = '../raw_data/pagellaPolitica_data_24092022.json'

with open(FILEPAGELLA, "r") as json_file:
    lines = json_file.readlines()
    textDate = "\"data_della_dichiarazione\": \"[0-9]* \w* [0-9][0-9][0-9][0-9]\""
    textTitle = "\"title\": {"
    withDate = 0
    articoli = 0
    for str in lines:
        x = re.findall(textDate, str)
        if(x):
            withDate+=1
        y = re.findall(textTitle, str)
        if(y):
            articoli+=1

print("articoli:", articoli)
print("con data:", withDate)
withoutDate = articoli - withDate
print("senza data:", withoutDate)
rate = withDate / withoutDate
print("con data / senza data", rate)

#now we count verdetto verboso vs verdetto sintetico
with open(FILEPAGELLA, "r") as file:
    f = file.read()

t = "\"verdetto\": {\n([ |\t])*\"testo\": \".*?\""

VERDETTI = "../outputs/verdetti2.txt"
fout = open(VERDETTI,"w")

matches = re.finditer(t, f)
counterVerdetti = 0
verdetti = []
for match in matches:
    #match.group(0) contains the matched
    verdetto_testo = match.group(0).split("\"testo\": ", 1)
    fout.write(verdetto_testo[1] + "\n")
    verdetti.append(verdetto_testo[1])
    counterVerdetti+= 1

fout.close()

if(articoli == counterVerdetti):
    print("all verdicts retrieved!")

#now with the list containing strings for every verdetto
#split for ' ', if we get more than 2 substring : verbose. else : short
verbose = 0
short = 0
for string in verdetti:
    subVerdetto = string.split(' ')
    if(len(subVerdetto)>2):
        verbose+=1
    else:
        short+=1

print("verdetto breve:", short)
print("verdetto verbose:", verbose)
print( articoli == verbose + short)
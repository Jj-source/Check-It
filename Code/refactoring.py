import codice.articleObj as articleObj
import json

# code to clean and refactor the dataset

FILEPAGELLA = '../raw_data/pagellaPolitica_data_24092022.json'

with open(FILEPAGELLA, "r") as json_file:
    f = json.load(json_file)
    DATASET = "../outputs/dataset.txt"
    #clean the file from previous writes
    open(DATASET, 'w').close()

    dataset = []
    for dict in f:
        for art in dict:
            title = art["title"]["rendered"]
            title = articleObj.bonifica(title)
            verdettoVerboso = ""
            counter = 0
            try:
                data = art["acf"]["data_della_dichiarazione"]
                data = articleObj.bonifica(data)
            except:
                data = ""
            try:
                statement = art["acf"]["sentenza"]
                statement = articleObj.bonifica(statement)
            except:
                statement = ""
            try:
                source = art["acf"]["link"]
                source = articleObj.bonifica(source)
            except:
                source = ""
            try:
                verdetto = art["acf"]["verdetto"]["testo"]
                verdetto = articleObj.bonifica(verdetto)
            except:
                verdetto = ""
            try:
                counter = len(art["acf"]["verdetto"]["in_breve"])
                for str in art["acf"]["verdetto"]["in_breve"]:
                    if(counter == 1):
                        verdettoVerboso += "\t\t\"" + articleObj.bonifica(str["testo"]) + "\""
                    else:
                        verdettoVerboso += "\t\t\"" + articleObj.bonifica(str["testo"]) + "\"," + "\n"
                    counter -= 1
            except:
                verdettoVerboso = ""
            try:
                content = art["content"]["rendered"]
                content = art.bonifica(content)
                #dividiamolo in singole frasi
                newContent = content.split('.')
            except:
                newContent = ""
            try:
                del art["editor"]
            except:
                pass
            try:
                del art["_links"]
            except:
                pass

            #links elaboration



            p1 = articleObj.articleObj(title,data,statement,verdetto,verdettoVerboso,source,newContent)
            dataset.append(p1)
            p1.writeToFile(DATASET)

###########
import requests

# Collecting of data from the API, saved in a file for further manipolatino
    
# api-endpoint
URLPAGELLA = ""
OUTFILE = ''
#number of articles
conteggio = 0

with open(OUTFILE, 'w') as json_file:
  # defining a params dict for the parameters to be sent to the API
  PARAMS = {
      'per_page':'100',
      'page': 1
    }
  # define empy list: our dataset!
  dataset = []

  # sending get request and saving the response as response object
  r = requests.get(url = URLPAGELLA, params = PARAMS)
  while r.status_code == 200:
    #update page number for next request
    PARAMS["page"] += 1
    # extracting data in json format
    response = r.json()
    for singleArticle in response :
      dataset.append(singleArticle)
    print(str(PARAMS["page"]-1) +" page done!")
    r = requests.get(url = URLPAGELLA, params = PARAMS)

  # request not succesfull, we read everything we could

  # uncomment the following line to overwrite json_file
  #json.dump(dataset, json_file, indent=2, ensure_ascii=False)

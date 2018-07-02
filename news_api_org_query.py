# This script queries the Newsapi.org API for all mentions of a given set of keywords or phrases,
# and puts the results into a PANDAS dataframe

#Importing relevant packages
from __future__ import division
import requests
import json
import math
import time # for pauses between calls
import pandas # for dataframes
import csv # to write to file

# Forming the API Query from NewsAPI
# documentation: https://newsapi.org/docs
# and especially: https://newsapi.org/docs/endpoints/everything
# doc recommends using HTTP headers instead of querystring parameters, but IDK how

key = "f9c1545dd5f84fc0ac45308b845bab68" # get at https://newsapi.org/register
base_url = "https://newsapi.org/v2/everything"

# Search paramters
# q obviously needs refining; see API documentation
search_params = {"q": '"detention+center"',
                 "apiKey": key,
                 "from": "2018-05-01", # "this API only includes articles up to a month old!!!"
                 # "to" by default is as recent as API plan allows (15 min ago for free)
                 "pageSize": "100" # maximum possible, to cut down on num of requests
                }

# Initial request to see hwo many hits there will be before querying page by page
request = requests.get(base_url,params=search_params)

# converting the response to JSON
initial_data = json.loads(request.text)

# How many hits are there for this query?
hits = initial_data['totalResults']
print("number of hits:", str(hits))

# How many pages of results?
# necessary in order to loop through pages of results later
pages = int(math.ceil(hits/100))
print("number of pages: ", str(pages))

# using the test query to see what metadata we get
print('\n')
print('available data: ')
print(list(initial_data['articles'][1]))
print('\n')

# Creating an empty dataframe to store the data
articles = pandas.DataFrame()

# looping through the pages of results and adding them to df
for i in range(pages):
    print("collecting page", str(i)) # shows in console

    # setting the page parameter
    search_params['page'] = i + 1

    # making the request
    r = requests.get(base_url, params = search_params)

    # getting the text and converting it to a dictionary
    data = json.loads(r.text)
    docs = data['articles']
    df_temp = pandas.DataFrame(docs)

    #adding those docs to the master dataframe
    articles = pandas.concat([articles,df_temp],ignore_index=True)

    time.sleep(.2) # pause between calls to prevent refusal

print ('done')

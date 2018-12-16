import numpy as np
import pandas as pd
import os
from pathlib import Path
import urllib2
# import urllib.request  as urllib2 
import shutil
# Imports the Google Cloud client library
from google.cloud import bigquery
import pkg_resources
import glob
import argparse
from forex_python.converter import CurrencyRates
c = CurrencyRates()
listofcurrency = c.get_rates('USD')

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--queries", required=True,
    help="path to input queries (i.e., directory of sql queries)")
args = vars(ap.parse_args())

trainpercent = 0.9
#Append all sql queries
sqlfiles = []
for file in glob.glob(str(args["queries"]) + "*.sql"):
    sqlfiles.append(file[len(str(args["queries"])):])



def get_sql(path):
    return(pkg_resources.resource_string(__name__,  str(args["queries"]) + path))
#Download
for sqlfile in sqlfiles:
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = True
    bigquery_client = bigquery.Client()
    query = get_sql(sqlfile)
    job = bigquery_client.query(query, job_config=job_config)
    print(str(sqlfile))
    print(job.state)
    totaldata = job.result().to_dataframe()
    totaldata.dropna(inplace = True)
    
    #convert currency
    for currency in list(listofcurrency):
        totaldata.loc[totaldata["currency"] == currency,"price"] = totaldata[totaldata["currency"] == currency]["price"].divide(listofcurrency[currency])
        
    #Price ranges
    price_range = [0,int(np.percentile(totaldata["price"],25)),int(np.percentile(totaldata["price"],50)),int(np.percentile(totaldata["price"],75)), int(max(totaldata["price"]))]

    # for price in price_range[:-1]:
    #     try:
    #         if not os.path.exists(str("trainset/") + str(Path(sqlfile).stem)+str("_")+str(price)+str("/")):
    #             os.makedirs(str("trainset/") + str(Path(sqlfile).stem)+str("_")+str(price)+str("/"))
    #         if not os.path.exists(str("testset/") + str(Path(sqlfile).stem)+str("_")+str(price)+str("/")):
    #             os.makedirs(str("testset/") + str(Path(sqlfile).stem)+str("_")+str(price)+str("/"))
    #     except OSError:
    #         print ('Error: Creating directory. ')
    
    for j in range(1,len(price_range)):
        data=totaldata[(totaldata["price"]>=int(price_range[j-1]))&(totaldata["price"]<=int(price_range[j]))]
        trainl = round(trainpercent*len(data))
        train = data.iloc[:int(trainl)]
        test=data.iloc[int(trainl):]
        for i in range(len(train)):
            try:
                filedata = urllib2.urlopen(str(train.iloc[i,3]))  
                datatowrite = filedata.read()
                name = str("trainset/") + str(Path(sqlfile).stem)+str("_")+str(price_range[j-1])+str("/") + str(Path(sqlfile).stem) + str(i) + str(".jpg")
                with open(str(name), 'wb') as f:  
                    f.write(datatowrite)
            except:
                print ('Error: URL not found. ')
        for i in range(len(test)):
            try:
                filedata = urllib2.urlopen(str(test.iloc[i,3]))  
                datatowrite = filedata.read()
                name = str("testset/") + str(Path(sqlfile).stem)+str("_")+str(price_range[j-1])+str("/")  + str(Path(sqlfile).stem) + str(i) + str(".jpg")
            except:
                print ('Error: URL not found. ')
            with open(str(name), 'wb') as f:  
                f.write(datatowrite)
print("Downloading Datasets is finished")


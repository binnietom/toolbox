"""
datasette example. based on sqlite
https://datasette.io

(the website itself is actually built in datasette.)

brew install datasette sqlite-utils
datasette install datasette-cluster-map

e.g.
sqlite-utils insert dataexamples/trees.db trees dataexamples/Borough_tree_list_2025Nov.csv --csv


or.

!datasette publish cloudrun data.db --service=mydata


dealing with duplicates
>sqlite-utils extract trees.db trees !!!!!column
results in specific entries being hyperlinked to a dedicated table. 
repeat on lots of columns

add searching (search bar at the top). 
>sqlite-utils enable-fts trees.dv trees !!!column. 


make it accessable online - uses google cloud via a docker container and built as a docker image. 
>

brew install --cask google-cloud-sdk
gcloud init
gcloud --version

##billing activated only...
""" 

import pandas as pd

path = "../../../../_Qresearch/Arthur_Turrell/coding_for_economists/datasets/Ward_to_Local_Authority_District_to_County_to_Region_to_Country_December_2019_UK.csv"

df = pd.read_csv(path)

import subprocess
import sys
##subprocess is needed to replace the notebook inline ! (see below)

#!csvs-to-sqlite "datasets/Ward_to_Local_Authority_District_to_County_to_Region_to_Country_December_2019_UK.csv" "datasets/data.db"
#!datasette "datasets/data.db"
#!datasette publish cloudrun "datasets/data.db" --service=mydata



#EG1 - trees, creating useful bits in the database table

#subprocess.run(["sqlite-utils", "extract", "dataexamples/trees.db", "trees", "taxon_species",], #check = True) 

#subprocess.run(["sqlite-utils", "enable-fts", "dataexamples/trees.db", "trees", "location",], #check = True) 
###Note these onle need to be run once!

#simple local excecution
subprocess.run([
    "datasette",
    "dataexamples/trees.db",
], check=True)

"""
#cloud excecution
subprocess.run([
    "datasette",
    "publish",
    "cloudrun",
    "dataexamples/trees.db",
    "--service=mytrees",
], check=True)
"""

"""
#EG2 (from python4economists) 
subprocess.run([
    "csvs-to-sqlite",
    path,
    "dataexamples/data.db",
], check=True)

subprocess.run(["datasette", "dataexamples/data.db"], check=True)

subprocess.run([
    "datasette",
    "publish",
    "cloudrun",
    "dataexamples/data.db",
    "--service=mydata",
], check=True)
"""
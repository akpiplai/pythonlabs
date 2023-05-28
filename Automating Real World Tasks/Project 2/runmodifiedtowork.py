#! /usr/bin/env python3

# objective of this script is to read text files that contains feedback of customers in a 
# specific format and then parse them into a dictionary
# so that it can be passed to a web service endpoint in post request to update a database

from genericpath import isfile
from os import listdir
from os.path import join
import requests
import json

def list_text_files(dirpath):
    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f)) and f.endswith(".txt")]
    return files

def read_feedback(filename):
    field_titles = ["title", "name", "date", "feedback"]
    field_values = []
    
    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip(): #non-empty lines
                    field_values.append(line.strip())
    except Exception as e:
            print(e)
    
    #combining keys and values to form dictionary and return to the caller
    return dict(zip(field_titles, field_values))

def main():
    #read the file names which are text files from the specified directory
    files = list_text_files(".")

    #list to store feedbacks
    feedbacks = []
    
    #iterating through files to read and store feedbacks in dict and then into list
    for f in files:
        dict = read_feedback(f.strip())
        feedbacks.append(dict)
    
    #turn the parameters into json
    #post_json = json.dumps(feedbacks)
    
    #print(post_json)

    for item in feedbacks:
        try:
            #send it to django web api for updating database
            #p=json.dumps(item)
            print("inserting: \n {}".format(item))

            # no need to mention header as header is automatically set to application/json with json param
            response = requests.post("http://104.155.149.37/feedback/", json=item)
            
            print("Request details:\n")
            print(response.request.url)
            print(response.request.body)
            
            response.raise_for_status()
            print("UPDATE SUCCESS....")
            print()
            
        except Exception as e:
            print ("error while inserting feedback through web api. \n {}".format(e))
    
if __name__ == "__main__":
    main()
    
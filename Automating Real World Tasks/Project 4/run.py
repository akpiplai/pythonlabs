#! /usr/bin/env python3

import requests
import common
from os.path import split

def read_description(filename):
    field_titles = ["name", "weight", "description", "image_name"]
    field_values = []
    
    try:
        #open each file to read contents
        with open(filename, "r") as f:

            lines_in_file = ""
            
            #traverse each line in the file and add to string with comma(,) separator
            for line in f:
                if line.strip(): #non-empty lines
                    field_values.append(line.strip())
                    
        # add image name or the file name
        d, f = split(filename)
        field_values.append(f.replace("txt", "jpeg"))
        
    except Exception as e:
            print(e)
    
    #combining keys and values to form dictionary and return to the caller
    return dict(zip(field_titles, field_values))

def main():
    #read the file names which are text files from the specified directory
    files = common.list_files("images", ".txt")

    #list to store image descriptions
    image_descriptions = []
    
    #iterating through files to read and store feedbacks in dict and then into list
    for f in files:
        dict = read_description(f.strip())
        image_descriptions.append(dict)
    
    print(image_descriptions)
    
    for item in image_descriptions:
        try:
            #send it to django web api for updating database
            #p=json.dumps(item)
            print("inserting: \n {}".format(item))

            # no need to mention header as header is automatically set to application/json with json param
            response = requests.post("http://104.155.149.37/fruits/", json=item)
            
            response.raise_for_status()
           
        except Exception as e:
            print ("error while inserting feedback through web api. \n {}".format(e))

    print("UPDATE SUCCESS....")
    print()    
    
if __name__ == "__main__":
    main()
    
#!/usr/bin/env python3

import common
import datetime
import reports
import emails
import os

def main():
    #read the file names which are text files from the specified directory
    files = common.list_files("images", "txt")

    #list to store image descriptions
    image_descriptions = []
    
    #iterating through files to read and store feedbacks in dict and then into list
    for f in files:
        try:
            dict = common.read_description(f.strip())
            image_descriptions.append(dict)
        except Exception as e:
            print(e)
            
    report_title = "Processed Update on {}".format(datetime.datetime.now().strftime("%x"))
    paragraph = ""
    
    for item in image_descriptions:
        paragraph += "<br/> name : {} <br/> weight : {} <br/>".format(item["name"], item["weight"])
        
    reports.generate_report("processed.pdf", report_title, paragraph)
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate(sender, receiver, subject, body, "processed.pdf")
    
    try:
        emails.send(message)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import shutil
import psutil
import emails
import os
import socket

def send_email(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    
    message = emails.generate(sender, receiver, subject, body)
    
    try:
        emails.send(message)
    except Exception as e:
        print(e)
    
def main():
    if psutil.cpu_percent(interval=1) > 80:
        send_email("Error - CPU usage is over 80%")
        
    total, used, free = shutil.disk_usage("/")
    freedisk_percent = (free * 100)//total
    
    if freedisk_percent < 20:
        send_email("Error - Available disk space is less than 20%")
    
    obj_memory = psutil.virtual_memory()
    
    if (obj_memory.free//(1024**2)) < 500:
        send_email("Error - Available memory is less than 500MB")
        
    try:
        socket.gethostbyname("http://localhost")
    except socket.error:
        send_email("Error - localhost cannot be resolved to 127.0.0.1")
        
if __name__ == "__main__":
    main()
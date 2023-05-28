#!/usr/bin/env python3
import re
from operator import itemgetter

# reads ERROR and INFO log details from logfiles and generates dictionary items. 
def readFromLog(logFileName):
    error_message = {}
    user_stat = {}
            
    with open(logFileName, "r") as f:
        
        for line in f.readlines():
            
            # regex for taking out ERROR/INFO (Group 1), Error Text (Group 2) and Username (Group 3)
            result = re.search(r"(ERROR|INFO) ([\w. \D\[?\D?\]?]+)\(([\w.?]+)\)", line) 
            
            if(result != None):
                errorOrInfo = result.group(1).strip()
                errorOrInfoText = result.group(2).strip()
                userName = result.group(3).strip()

                if errorOrInfo == "ERROR":
                    if errorOrInfoText not in error_message: 
                        error_message[errorOrInfoText] = 0
                    error_message[errorOrInfoText] += 1

                    if userName not in user_stat:
                        user_stat[userName] = {"INFO" : 0, "ERROR" : 0}
                    user_stat[userName]["ERROR"] += 1
                    
                if errorOrInfo == "INFO":
                    if userName not in user_stat:
                        user_stat[userName] = {"INFO" : 0, "ERROR" : 0}
                    user_stat[userName]["INFO"] += 1
            
    f.close()
    
    return error_message, user_stat

# prints dictionary output to csv file. **prints dictionary ONLY upto nesting level 1
def generateCSV(d, fileName, headerText, sortIndex, reverseOrder):
    
    if isinstance(d, dict) and len(d) > 0 \
        and type(sortIndex) == int and sortIndex >= 0 \
            and type(reverseOrder) == bool:
    
        d = dict(sorted(d.items(), key=itemgetter(sortIndex), reverse=reverseOrder))
               
        try:
            with open(fileName, "w") as f:
                if headerText != "": f.write(headerText)

                for key, value in d.items():
                    if isinstance(value, dict):
                        f.write("\n{0}".format(key))
                        
                        for v in value.values():
                            f.write(",{0}".format(v))
                                                
                    else:
                        f.write ("\n{0},{1}".format(key, value))
        except:
            print ("exception happened while writing file.")
            
        finally:
            f.close()
    else:
        raise ValueError("Input validation failed for function : generateCSV")

# read error and info messages from log as per given requirement
error_msg, per_user = readFromLog("syslog.log")

# generate csv files from dictionaries
generateCSV(error_msg, "error_message.csv", "Error,Count", 1, True)
generateCSV(per_user, "user_statistics.csv", "Username,INFO,ERROR", 0, False)

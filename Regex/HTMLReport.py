#!/usr/bin/env python3
import re
import operator

#reads ERROR and INFO log details from logfiles and generates dictionary items. 
def readFromLog(logFileName, format):
    error_message = {}
    user_stat = {}

    with open(logFileName, "r") as f:
        
        for line in f.readlines():
            result = re.search(r"" + format + "", line) 
            
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
            
    error_message = dict(sorted(error_message.items(), key=operator.itemgetter(1), reverse=True))
    user_stat = dict(sorted(user_stat.items(), key=operator.itemgetter(0)))
    
    return error_message, user_stat

#prints dictionary output to csv file. **prints only dictionary with nesting level 1
def generateCSV(d, filename, headerText):
    try:
        with open(filename, "w") as f:
            if headerText != "": f.write(headerText)

            for key, value in d.items():
                if isinstance(value, dict):
                    f.write("\n{}".format(key))
                    
                    for v in value.values():
                        f.write(",{}".format(v))
                                            
                else:
                    f.write ("\n{},{}".format(key, value))
            
            f.close()
    except:
        print ("exception happened while writing file")
        
format = "(ERROR|INFO) ([\w. \D\[?\D?\]?]+)\(([\w.?]+)\)"
error_msg, per_user = readFromLog("syslog.log", format)

generateCSV(error_msg, "error_message.csv", "Error,Count")
generateCSV(per_user, "user_statistics.csv", "Username,INFO,ERROR")
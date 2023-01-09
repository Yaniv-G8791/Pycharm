import os
import json
def configjson():
    configfile = str(os.getcwd())+"\\Config\\AppConfig.Json"
    file = open(configfile, "r",encoding="utf8")
    jsoncontent = json.load(file)
    file.close()
    return jsoncontent
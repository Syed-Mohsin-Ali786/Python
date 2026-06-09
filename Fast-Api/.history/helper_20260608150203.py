from config import filename
import json
def write(data:dict):
    with open(filename,'w') :
        json.load(data)
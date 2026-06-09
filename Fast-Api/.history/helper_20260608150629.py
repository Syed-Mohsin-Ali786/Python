from config import filename
import json
def write(data:dict):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)
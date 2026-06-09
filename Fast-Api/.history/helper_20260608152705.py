from config import filename
import json

def read():
    with open (filename,'r') as file:
        data=json.load(file)
        if data=="":
            return []
        return data
def write(data:dict):
    with open(filename,'a') as file:
        json.dump(data,file,indent=4)
        
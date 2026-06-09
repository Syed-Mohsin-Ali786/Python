from config import filename
import json

def read():
    try:
     with open (filename,'r') as file:
        data=json.load(file)
        if data=="":
            return []
        return data
    except 
def write(data:dict):
    current_data=read()
    new_data=current_data.append(data)
    with open(filename,'a') as file:
        json.dump(new_data,file,indent=4)
        
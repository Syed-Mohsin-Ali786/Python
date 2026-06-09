from config import filename
def write(data:dict):
    with open(filename,'w') as file:
        file.write(data)
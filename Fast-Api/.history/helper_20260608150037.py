from config import filename
def write(data:dict):
    print(data)
    with open(filename,'w') as file:
        file.writelines(data)
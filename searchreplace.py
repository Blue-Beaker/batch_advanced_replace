import os,sys

recursive:bool=True
scanPath="~"

def whetherToProcessFile(file:str):
    return file.endswith(".json") and 'dye_' in file

def operationToFiles(file:str):
    filename=os.path.basename(file)
    with open(file,"r") as f:
        print(f.read())
    return



def listTree(folder:str):
    files=[]
    files2=[]
    for file in sorted(os.listdir(folder)):
        path=os.path.join(folder,file)
        if recursive and os.path.isdir(path):
            files2.extend(listTree(path))
        elif whetherToProcessFile(path):
            files.append(file)
    files2.extend(files)
    return files2

os.chdir(scanPath)
lst=listTree(scanPath)
print(lst)
for file in lst:
    operationToFiles(file)
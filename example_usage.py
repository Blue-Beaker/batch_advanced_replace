import os
from searchreplace import Replacer
"""
    Overwrite this to change what file to be processed.
"""
def whetherToProcessFile(file:str):
    return file.endswith(".txt") and 'test' in file

"""
    Overwrite this to change what operations to be done with the files.
"""
def operationToFiles(file:str):
    filename=os.path.basename(file)
    with open(file,"r") as f:
        print(f.read().replace("filename",filename.removesuffix('.txt')))
    return

replacer=Replacer(whetherToProcessFile,operationToFiles)
replacer.run(".")
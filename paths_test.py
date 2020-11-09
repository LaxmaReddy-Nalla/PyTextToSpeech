from pathlib import Path,PurePosixPath

def getPATH():
    inpFilePAth = input('Enter file path:- ')
    source = Path(inpFilePAth)
    p = PurePosixPath(inpFilePAth)
    q = str(p.parent)
    r == inpFilePAth = input('Enter file path:- ')
    source = Path(inpFilePAth)
    print(q)
    fileName = str(source.name)
    print(fileName)
    r = q+'/'+fileName
    print(r)
    
getPATH()

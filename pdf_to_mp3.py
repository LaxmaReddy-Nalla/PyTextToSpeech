import PyPDF2 as pdf
from gtts import gTTS
from pathlib import Path,PurePosixPath
import os


#input file path from user
def getPATH():  
    global q,fileName,file1
    inpFilePAth = input('Enter file path:- ')
    source = Path(inpFilePAth)
    p = PurePosixPath(inpFilePAth)  
    q = str(p.parent)
    fileName = str(source.stem)
    print(fileName)
    file = str(source.name)
    file1 = q+'/'+file
    print(file1)
    print(file)


#open pdf file and extract pdf content to txt file
def open_Doc():
    global open_doc,pages,txtFile
    open_doc= pdf.PdfFileReader(file1,'rb')
    pages = open_doc.numPages
    print(pages)
    #create a text to wirte the pdf content
    txtFile = open(fileName+'.txt','w')
    #forLoop(pages,open_doc,txtFile)

#for loop to retrive pages from pdf file and print to text file
def forLoop():
    for i in range(pages):
        page = open_doc.getPage(i)
        content = page.extractText()
        txtFile.write(content)    
    print('finished')


#read file content from text
def read_content():
    global text
    f = open(fileName+'.txt','r')   
    text = f.read()
    f.close()
    

#initialize the google text to speech engine and save to mp3 file
def convertAudio():
    print('Audio Conversion Started')
    tts = gTTS(text,lang='en')
    destination = q+"/"+fileName
    tts.save(destination+'.mp3')
    print('saved audio file')
    os.remove(fileName+'.txt')

def main():
    getPATH()
    open_Doc()
    forLoop()
    read_content()
    convertAudio()
main()

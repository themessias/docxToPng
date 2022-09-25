import os
from msoffice2pdf import convert
from pdf2image import convert_from_path

def getFolder():
  return os.getcwd()

def getFiles():
  folder = getFolder() + '\input'
  files = os.listdir(folder)
  files = removeFoldersFromList(files)
  return files

def removeFoldersFromList(list):
  return [element for element in list if "." in element]

def removeExtension(file):
  return file.rsplit(".")[0]

def folderExists(path):
  return os.path.exists(path)

def createFolder(path):
  if not folderExists(path):
    os.mkdir(path)
    print(f'Pasta output criada com sucesso!')

if __name__ == "__main__":
  files = getFiles()
  for file in files:
    inputFile = getFolder() + f"\input\{file}"
    path = f'{getFolder()}'
    createFolder(path+'\input')
    createFolder(path+'\output')
    outputFile = getFolder() + f"\output\{removeExtension(file)}.pdf"
    convert(source=inputFile, output_dir=path+'\output', soft=0)
    pages = convert_from_path(outputFile, 500, poppler_path=r'.\poppler\bin')
    pngName = input(f'Digite o novo nome do arquivo {file}(Deixe vazio para manter o'\
                    ' mesmo nome)\n->')
    if not pngName:
      pngName = removeExtension(file)
    for page in pages:
      page.save(f'{getFolder()}\output\{pngName}.png')
    os.remove(outputFile)
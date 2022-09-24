import os
from docx2pdf import convert
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
    print(file)
    input = getFolder() + f"\input\{file}"
    path = f'{getFolder()}\output'
    createFolder(path)
    output = getFolder() + f"\output\{removeExtension(file)}.pdf"
    convert(input, output)
    pages = convert_from_path(output, 500, poppler_path=r'.\poppler\bin')
    for page in pages:
      page.save(f'{getFolder()}\output\{removeExtension(file)}.png')
    os.remove(output)
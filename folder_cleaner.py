import os

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def moveFiles(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


files = os.listdir()
files.remove('folder_cleaner.py')

createFolder('Images')
createFolder('Medias')
createFolder('Docs')
createFolder('PythonFiles')
createFolder('Others')

imgExts = ['.png', '.jpg', '.jpeg', '.img']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.csv']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = ['.mp3', '.mp4', '.flv']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

pyExts = ['.py']
python = [file for file in files if os.path.splitext(file)[1].lower() in pyExts]

Exts = ['']
Exts.extend(imgExts)
Exts.extend(docExts)
Exts.extend(mediaExts)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if ext not in Exts and os.path.isfile(file):
        others.append(file)

moveFiles("Images",images)
moveFiles("Docs",docs)
moveFiles("PythonFiles",python)
moveFiles("Medias",medias)
moveFiles("Others",others)

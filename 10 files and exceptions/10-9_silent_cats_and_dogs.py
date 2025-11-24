##CATS AND DOGS BUT SILENT EXERCISE#
#modify your except block in exercise 10-8 to fail silently if either file is misisng

from pathlib import Path

def readfile(path):
    """reads the file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(contents)
        
filenames = ['cats.txt','dogs.txt','chicken.txt']
for filename in filenames:
    path = Path(f'./10 files and exceptions/{filename}')
    readfile(path)
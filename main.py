import os
from PIL import Image

folder = 'C:/dir'

def conv(folder):
    for fileN in os.listdir(folder):
        if fileN.endswith('.png') or fileN.endswith('.jfif'):
            fileP = os.path.join(folder, fileN)
            img = Image.open(fileP)
            
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            new_fileN = os.path.splitext(fileN)[0] + '.jpg'
            new_fileP = os.path.join(folder, new_fileN)
            
            img.save(new_fileN, 'JPEG')
            print(f'Converted {fileN} to {new_fileN}')
            os.remove(fileP)
            print(f'Deleted original file: {fileN}')

conv(folder)


import os
from PIL import Image

target_dir = 'C:/dir'

def conv(folder):
    for fileN in os.listdir(folder):
        if fileN.endswith('.png') or fileN.endswith('.jfif'):
            fileP = os.path.join(folder, fileN)
            img = Image.open(fileP)
            
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            new_fileN = os.path.splitext(filename)[0] + '.jpg'
            new_fileP = os.path.join(folder, new_fileN)
            
            img.save(new_file_path, 'JPEG')
            print(f'Converted {filename} to {new_filename}')
            os.remove(file_path)
            print(f'Deleted original file: {filename}')

conv(target_dir)

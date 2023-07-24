#!/usr/bin/env python3

# from PIL import Image
# import glob, os

# for infile in glob.glob(os.path.join("G:\我的雲端硬碟\Git\Google_Crash_Course_On_Python\Automating-Real-World-Tasks-with-Python\W4\supplier-data\images","*.tiff"))
#     file,ext = os.path.splitext(infile)
    

#!/usr/bin/env python3

from PIL import Image
import os
directory = "supplier-data/images/"

for filename in os.listdir(directory):
#  print(filename)
    if filename.endswith(".tiff"):
        # print(filename)
        im = Image.open(os.path.join(directory,filename))
        im = im.resize((600,400))
        im = im.convert("RGB")
        im.save(os.path.join(directory,filename+".jpeg"))

# path = "supplier-data/images/"
# for f in os.listdir("supplier-data/images"):
#     if f.endswith(".tiff"):
#         split_f = f.split(".")
#         name = split_f[0] + ".jpeg"
#         im = Image.open(path + f).convert("RGB")
#         im.resize((600, 400)).save("./supplier-data/images/" + name, "JPEG")
        
# file ~/supplier-data/images/003.jpeg
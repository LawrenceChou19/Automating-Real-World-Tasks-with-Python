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
        #split 001.tiff -> 001 and tiff 
        splitfilename = filename.split(".")
        im = im.resize((600,400))
        im = im.convert("RGB")
        #save 001 with .jpeg extension format
        im.save(os.path.join(directory,splitfilename[0]+".jpeg"))

# file ~/supplier-data/images/003.jpeg
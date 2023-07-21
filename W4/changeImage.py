#!/usr/bin/env python3

from PIL import Image
import glob, os

for infile in glob.glob(os.path.join("G:\我的雲端硬碟\Git\Google_Crash_Course_On_Python\Automating-Real-World-Tasks-with-Python\W4\supplier-data\images","*.tiff"))
    file,ext = os.path.splitext(infile)
    
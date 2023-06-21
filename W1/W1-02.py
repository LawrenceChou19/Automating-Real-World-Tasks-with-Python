# from PIL import Image
# with Image.open("G:\我的雲端硬碟\Git\Google_Crash_Course_On_Python\Automating-Real-World-Tasks-with-Python\W1\hopper.jpg") as im:
#     im.rotate(45).show()
    
    
from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob(os.path.join("G:\我的雲端硬碟\Git\Google_Crash_Course_On_Python\Automating-Real-World-Tasks-with-Python\W1","*.jpg")):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
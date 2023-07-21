

# curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

#unzip images.zip

from PIL import Image
import os
import sys

# ' / '：根目錄
# ' ./ '：當前同級目錄
# ' ../ '：上級目錄
directory = "images/"
output_directory = "./output/"

# Check if the directory exists
if not os.path.exists(output_directory):
    # If it doesn't exist, create it
    os.makedirs(output_directory)

for filename in os.listdir(directory):
    if filename !=".DS_Store":
        imag = Image.open(os.path.join(directory,filename))
        imag = imag.rotate(-90)
        imag = imag.resize((128,128))
        imag = imag.convert("RGB")
        imag.save(os.path.join(output_directory,filename+".jpeg"))
        
        
#validation
# python3
from PIL import Image
img = Image.open("G:/我的雲端硬碟/Git/Google_Crash_Course_On_Python/Automating-Real-World-Tasks-with-Python/W1/output/ic_add_location_white_48dp.jpeg")  
img.format, img.size
# This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:

# Iterate through each file in the folder
# For each file:
# Rotate the image 90° clockwise
# Resize the image from 192x192 to 128x128
# Save the image to a new folder in .jpeg format
# Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: /opt/icons/
#curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
#!/usr/bin/env python3
from PIL import Image
import os

directory = "images/"
output_directory = "/opt/icons/"

#The for loop to correct the badly formatted images.
for filename in os.listdir(directory):
    if filename !=".DS_Store":
        im = Image.open(os.path.join(directory,filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(output_directory,filename+".jpeg"))

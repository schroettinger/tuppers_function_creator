from PIL import Image
from PIL import ImageDraw
# from PIL import ImageFont
# import numpy as np
#Python2:
#import cStringIO
from io import BytesIO

BMPHEADERSIZE = 54
BMPLIMITLINE = 106
BMPLIMITLINE_WITHPADDING = 110
#Get a string
print("Input some string!")
inputstring = "Daniel" #input()

#Create a image and plot the input
img = Image.new('RGB', (BMPLIMITLINE, 17), (255, 255, 255))
d = ImageDraw.Draw(img)
d.text((0, 0), inputstring, fill=(0, 0, 0))

#Save the picture of the input in the memory
#Python2:
#s = cStringIO.StringIO()
s = BytesIO()
img.save(s, 'bmp')

#Get the - converted - image back and store it in an array
in_memory_file = s.getvalue()
array = in_memory_file


outputstring = ""
temp =""
skipheadercounter = 0
gothroughline = 0
for a in array:
    if (skipheadercounter > BMPHEADERSIZE):
        gothroughline = gothroughline +1

        if(gothroughline < BMPLIMITLINE):
            temp += str(hex(a))
            if a == 255:
                outputstring += "0"
            else:
                outputstring += "1"
        if(gothroughline == BMPLIMITLINE_WITHPADDING):
            gothroughline = 0
    else:
        skipheadercounter = skipheadercounter + 1 #skip theBMP Header but stop when limit reached

# print(temp)
print(outputstring)

#img.save('input.bmp')








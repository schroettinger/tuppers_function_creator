from PIL import Image
from PIL import ImageDraw
# from PIL import ImageFont
# import numpy as np
#Python2:
#import cStringIO
from io import BytesIO

BMPHEADERSIZE = 54
BMPLIMITLINE = 318*3
BMPLIMITLINE_WITHPADDING = 320*3
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
in_memory_file = s.getvalue() #210b size, 24bit, 106x17
array = in_memory_file


outputstring = ""
temp =""
skipheadercounter = 0
gothroughline = 0
i =0;
for a in array: #our bmp has 5494 bytes
    i=i+1
    if (skipheadercounter > BMPHEADERSIZE): #use only the payload of 5440B
        print(str(a))

        gothroughline = gothroughline + 1
        # 5440 / 17 = 320;  106 Pixel with 24bit (=3Byte) will have 318 Byte; difference of two has to be skipped
        if(gothroughline < BMPLIMITLINE) & (gothroughline % 3 == 0): #check each 3rd becasue of 24bit color depth. As we are only using one byte as identification this should work

            if a == 255:
                outputstring += "0"
                temp += "0"
            else:
                outputstring += "1"
                temp += "1"

        if(gothroughline >= BMPLIMITLINE_WITHPADDING):
            gothroughline = 0
            print(temp)
            temp = ""
    else:
        skipheadercounter = skipheadercounter + 1 #skip theBMP Header but stop when limit reached


print(outputstring)

#img.save('input.bmp')








from PIL import Image
from PIL import ImageDraw
import webbrowser

#Defines
TUPPERS_X = 106  # The maximal x axis or the tupper's funtion is 106
TUPPERS_Y = 17  # teh amximal Y axis for tupper's function is 17
ROTATEANGLE = 90
URL = "https://tuppers-formula.ovh/#"

# Get a string
print("Input some string!")
inputstring = input() # A maximum stringlength is not implemented until now

# Create a image and plot the input
img = Image.new('RGB', (TUPPERS_X, TUPPERS_Y), (255, 255, 255))
d = ImageDraw.Draw(img) #create a draw element to adding something to the image
d.text((0, 0), inputstring, fill=(0, 0, 0)) # Insert our string
size = TUPPERS_Y, TUPPERS_X #define size for rotate function
img = img.rotate(ROTATEANGLE, expand=1).resize(size) #resize the picture to be vertical instead of horizontal

# Define a black and a white pixel - more we don't need and other colors are also not defined by us
pixel_black = (0, 0, 0)
pixel_white = (255, 255, 255)
outputstring = ""

#loading only the needed pixels from the picture into pixels - without header or padding or something
pixels = img.load()

#this will step through the imape's pixels starting in the top upper left, going to the right and then into the next line
#until it ends up in the lower right corner
for y in range(TUPPERS_X): #y for TUPPERS_X because of rotation
    for x in range(TUPPERS_Y): #x for TUPPERS_Y because of rotation

        #print(pixels[x, y]) #for debug only
        if(pixels[x, y] == pixel_black):
            outputstring = outputstring + "1"

        if (pixels[x, y] == pixel_white):
            outputstring = outputstring + "0"

# Calculations for k:
#print(outputstring)
#print(int(outputstring))
outputstringAsNumber = int(outputstring, 2)
k = outputstringAsNumber *17

print("k to text \"" + inputstring + "\" is:")
print(k)

#Show it at the Webbrowser
webbrowser.open_new_tab(URL+str(k))
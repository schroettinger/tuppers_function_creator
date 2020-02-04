from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import cStringIO

#Get a string
inputstring = raw_input()

#Create a image and plot the input
img = Image.new('RGB', (106, 17), (255, 255, 255))
d = ImageDraw.Draw(img)
d.text((0, 0), inputstring, fill=(255, 0, 0))

#Save the picture of the input in the memory
s = cStringIO.StringIO()
img.save(s, 'png')

#Get the - converted - image back and store it in an array
in_memory_file = s.getvalue()
array = np.array(in_memory_file)

#print the array
print(array)

#img.save('hello.png')

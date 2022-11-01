from PIL import Image,ImageDraw,ImageFont
import textwrap as tr
import numpy as np
import cv2
import math

def breaktext(txt):
    output = " "
    lines = tr.wrap(txt, width=40)
    for line in lines:             #
        output = output + line + "\n "
    return output[:-2]           #(40-len(line))*" "+ 


        
def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)



fontname = "C:/Windows/Fonts/Arial.ttf"
fontsize = 20  
inputtext = post.title    
colorText = "black"
colorOutline = "white"
colorBackground = "white"

text = breaktext(inputtext)

font = ImageFont.truetype(fontname, fontsize)
width, height = getSize(text, font)
img = Image.new('RGB', (width+4, height+4), colorBackground)
d = ImageDraw.Draw(img)
d.text((2, height/2), text, fill=colorText, anchor="lm", font=font)
d.rectangle((0, 0, width+3, height+3), outline=None)
    
img.save("top.png")

image_1 = cv2.imread("top.png")
image_2 = cv2.imread("output.png")

height_1, width_1 = image_1.shape[:2]
height_2, width_2 = image_2.shape[:2]

# Resizing image_2 to match the width of image_1
new_width_2 = width_1
new_height_2 = new_width_2 * height_2 // width_2
image_2 = cv2.resize(image_2, (new_width_2, new_height_2))

combined_image = np.vstack((image_1, image_2))

cv2.imwrite("combined_image.jpg", combined_image)
i = Image.open("combined_image.jpg")
#i.show("combined_image.jpg")
#i.save()




old_size = i.size
if max(old_size) == old_size[1]:
    change="side"
    if (old_size[1]/5)*4 < old_size[0]:
        new_size = (old_size[1],old_size[1])#1:1
        ratio="1:1"
    else:
        new_size = ((old_size[1]/5)*4,old_size[1])#4:5
        ratio="4:5"
else:
    change="top"
    if old_size[1] > (old_size[0]/16)*9:
        new_size = (old_size[0],old_size[0])#1:1
        ratio="1:1"
    else:
        new_size = (old_size[0],(old_size[0]/16)*9)#16:9
        ratio="16:9"

new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
"""        
while type(new_size[1]) != "int" or type(new_size[0]) != "int":
    if ratio == "1:1":
        new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
    if ratio == "4:5":
        new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
        if math.ceil(new_size[0])/math.ceil(new_size[1]) != 4/5:
            new_size = ((math.ceil(new_size[1])/5)*4,math.ceil(new_size[1]))
    if ratio == "16:9":
        new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
        if math.ceil(new_size[0])/math.ceil(new_size[1]) != 16/9:
            new_size = (math.ceil(new_size[0]),(math.ceil(new_size[0])/16)*9)

"""
new_im = Image.new("RGB", new_size, "White")   ## luckily, this is already black!
box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
new_im.paste(i, box)

#new_im.show()
#new_im.save("post.png")

from PIL import Image

old_im = Image.open('cool-nawpic-11.jpg')
old_size = old_im.size
'''
new_size = (old_size[0], old_size[1]+200)
new_im = Image.new("RGB", new_size, "white")   ## luckily, this is already black!
box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
new_im.paste(old_im, box)

new_im.show()
# new_im.save('someimage.jpg')
'''
'''
import cv2
 
# reading the image
virat_img = cv2.imread('cool-nawpic-11.jpg')
 
# making border around image using copyMakeBorder
borderoutput = cv2.copyMakeBorder(
    virat_img, 100, 10, 10, 10, cv2.BORDER_CONSTANT, value=[100, 100, 100])
 
# showing the image with border
cv2.imwrite('output.png', borderoutput)

image = Image.open('output.png')
image.show()
'''
########################
from PIL import Image, ImageDraw, ImageFont

# create empty image
img = Image.open("cool-nawpic-11.jpg")
draw = ImageDraw.Draw(img)

# draw white rectangle old_size[0] x100 with center in 200,150
draw.rectangle([0, 0, old_size[0], 100], fill='gray')

# find font size for text `"Hello World"` to fit in rectangle 200x100
selected_size = 1
for size in range(1, 150):
    arial = ImageFont.FreeTypeFont('C:/Windows/Fonts/arial.ttf', size=size)
    w, h = arial.getsize("An anchor is specified with a two-character string. The first character is the horizontal alignment")  # older versions
    #left, top, right, bottom = arial.getbbox("Hello World")  # needs PIL 8.0.0
    #w = right - left
    #h = bottom - top
    print(w, h)
    
    if w > 200 or h > 100:
        break
        
    selected_size = size

    print(arial.size)
    
# draw text in center of rectangle 200x100        
arial = ImageFont.FreeTypeFont('C:/Windows/Fonts/arial.ttf', size=selected_size)

#draw.text((200-w//2, 150-h//2), "Hello World", fill='black', font=arial)  # older versions
#img.save('center-older.png')

draw.text((old_size[0]/2, 50), "An anchor is specified with a two-character string. The first character is the horizontal alignment", fill='black', anchor='ms', font=arial, align ="left")
#img.save('center-newer.png')

img.show()

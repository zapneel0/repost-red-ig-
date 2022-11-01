from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''        
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)    
    return lines
 
 
def draw_text(text):    
    # open the background file
    img = Image.open('cool-nawpic-11.jpg')
    
    # size() returns a tuple of (width, height)
    image_size = (old_size[0], 100)
 
    # create the ImageFont instance
    font_file_path = 'C:/Windows/Fonts/arial.ttf'
    font = ImageFont.truetype(font_file_path, size=50, encoding="unic")
 
    # get shorter lines
    lines = text_wrap(text, font, image_size[0])
    print(lines) # ['This could be a single line text ', 'but its too long to fit in one. ']

draw_text("This could be a single line text but its too long to fit in one.")#replace with meme text

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

#draw.text((old_size[0]/2, 50), "An anchor is specified with a two-character string. The first character is the horizontal alignment", fill='black', anchor='ms', font=arial, align ="left")
#img.save('center-newer.png')

img.show()
############################################################

text = "This could be a single line text but its too long to fit in one."#replace with meme text
lines = text_wrap(text, font, image_size[0])
line_height = font.getsize('hg')[1]
 
x = old_size[0]/2
y = 50
for line in lines:
    # draw the line on the image
    draw.text((x, y), line, fill=color, font=font)
    
    # update the y position so that we can use it for next line
    y = y + line_height
# save the image
img.save('word2.png', optimize=True)

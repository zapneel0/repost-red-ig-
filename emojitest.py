from pilmoji import Pilmoji
from PIL import Image, ImageFont


my_string = '''
Hello, world! 👋 Here are some emojis: 🎨 🌊 😎
I also support Discord emoji: <:rooThink:596576798351949847>
'''

with Image.new('RGB', (550, 80), (255, 255, 255)) as image:
    font = ImageFont.truetype('arial.ttf', 24)

    with Pilmoji(image) as pilmoji:
        pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)

    image.show()

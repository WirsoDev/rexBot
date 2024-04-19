import os
from PIL import Image, ImageDraw, ImageFont
import random


def apply_water_mark(path, text="AQUINOS GROUP", opacity=40, font_size=40, resize=True):

    if os.path.exists(path):
    
        extentions = [
            'jpg',
            'tiff',
            'png'
        ]

        if not os.path.exists(f"{path}\WaterMark"):
            os.mkdir(fr"{path}\waterMark")
        
        new_dir = fr"{path}\waterMark"
        files = os.listdir(path)

        for x in files:
            if x.split('.')[-1] in extentions:

                img = Image.open(os.path.join(path, x)).convert("RGBA")

                if resize and img.size[0]>1700:
                    # resize img
                    print(img.size[0])
                    new_size_y = int(1700) / (int(img.size[0]) / int(img.size[1]))
                    img = img.resize((1700, int(new_size_y)), Image.LANCZOS)

                #add some color!

                txt = Image.new('RGBA', img.size, (255,255,255,0))

                #Creating Text
                font = ImageFont.truetype("./fonts/Gilroy-Regular.ttf", font_size)

                #Creating Draw Object
                draw = ImageDraw.Draw(txt)

                #Positioning of Text
                width, height = img.size 

                # Loop for Multiple Watermarks
                y=200
                for i in range(7):
                    j=random.randint(0, width-300)
                    y+=random.randrange(0,int(height/8), 19)+random.randint(0,100)
                    draw.text((j,y), text, fill=(255,255,255, opacity), font=font)

                #Combining both layers and saving new image
                watermarked = Image.alpha_composite(img, txt)
                watermarked.save(new_dir + '/' + x.split('.')[0] + '.png')
        return True
    else:
        return False
    

    


            

            
            




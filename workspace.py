from PIL import Image, ImageDraw, ImageFont
#%%
imgSize = (400,600)
img = Image.new('RGB', imgSize, color = 'white')
#%%
drawer = ImageDraw.Draw(img)
drawer.text( (0,0), 'Hello World', fill = (255,0,0), size = 500)
#%%
text_size = drawer.textsize('Hello World')

#%%
img.save('blank.png')
#%%
from PIL  import ImageFont, ImageDraw, Image

image = Image.new('RGB', imgSize, color = 'black')
draw = ImageDraw.Draw(image)
txt = "Hello World"
fontsize = 1  # starting font size
fontName = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

# portion of image width you want text width to be
img_fraction = 0.99
font = ImageFont.truetype(fontName, fontsize)
while font.getsize(txt)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype(fontName, fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype(fontName, fontsize)

print('final font size',fontsize)
draw.text((10, 25), txt, font=font) # put the text on the image
image.save('blank.png') # save it
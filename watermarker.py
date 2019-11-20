from PIL import Image
import os
from pathlib import Path
from PIL.ExifTags import TAGS

#### Custom user file path ####
folder_path = Path("/Users/alexchapple/Mine/Watermark/")

def watermark_photo(input_image_path, output_image_path, watermark_image_path):

    # Opens the images
    base_image = Image.open(folder_path / str('photos' '/' + str(photo)))
    watermark = Image.open(watermark_image_path)

    # Gets the initial width and height for portrait mode
    init_width, init_height = base_image.size

    # Looks into exif code to see whether the photo is portrait or landscape
    base_image = get_exif(base_image)
    width, height = base_image.size
    
    # Resize water mark to fit the photo
    watermark = watermark.resize((int(init_width*0.2), int(init_height*0.2)), Image.ANTIALIAS)
    watermark.save('watermark_white.png')

    # Position of the watermark
    width2, height2 = watermark.size
    position = (width-width2, height-height2)

    # Add watermark to an image
    transparent = Image.new('RGB', (width, height))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.save(folder_path / str('watermarked_photos/' + output_image_path))

# Function that looks into the exif code to correctly orientate the image 
def get_exif(image):
    ret = {}
    info = image._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    print(ret["Orientation"])
    orientation = ret["Orientation"]
    if orientation == 3:
        image = image.rotate(180, expand=True)
    elif orientation == 6:
        image = image.rotate(-90, expand=True)
    elif orientation == 8:
        image = image.rotate(90, expand=True)
    return image

# Script code that runs through the 'photos' folder and performs the water marking
photo_folder = os.listdir(folder_path / 'photos')
i = 1

for photo in photo_folder:
    if photo.endswith('.JPG') | photo.endswith('.jpg'):
        watermark_photo(photo, str(i) + '.JPG', 'watermark.png')
        i += 1

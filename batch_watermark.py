import watermarker
import os

directory = '/Users/alexchapple/Mine/Watermark/photos'
i = 1

for image in os.listdir(directory):
    watermark_photo(image, str(i)+'jpg', 'watermark.png')

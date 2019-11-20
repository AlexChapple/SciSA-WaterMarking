# SciSA-WaterMarking

This is a piece of custom software created for watermarking photos from our events.
The following instructions are for anybody who would like to use this software for 
their own watermarking. There are 2 main watermarking files. "watermarker.py" is for adding a logo to the bottom right of the photo. "watermarker_double.py" is for adding two logos to the bottom left and right of the photo. The position of the logo can be customised easily with some tweak to the code. 

Things you need: 
- Python 3
- Some way to run, and edit python code

How to configure:

1. Choose a location for your main folder, and name it Watermark. 
2. Within the folder, create 2 folders. One folder will be named photos, and the other will be named watermarked_photos. 
3. In the main Watermark folder, add the 2 watermarking python files alongside the 2 folders. 
4. Open the file "watermarker.py" in an editor. On line 7 there should be a variable named "folder_path". This is the path to the main Watermark folder on your device. You will need to replace the text in Path("") to the folder path for your main Watermark folder. 
5. The same can be done for the file "watermarker_double.py". 

Now you are set up to watermark your photos. 

In order to watermark your photos, add the photos you want watermarked to the "photos" folder in your main Watermark folder.
Note that the photos must be jpeg of jpg for this to work. Next, in your main Watermark folder, add the logo you want to watermark and name it "watermark.png". If you are using the "watermarker_double.py" file to water mark two logos, you will need another logo in your main folder named "watermark2.png". 

Now, run the watermarking python file (either watermarker.py or watermarker_double.py). The watermarked photos will appear in the "watermarked_photos" folder in your main folder.

For any further questions, message us on Facebook at www.facebook.com/sciencestudentsassociation 

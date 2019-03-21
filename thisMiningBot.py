from miningbot import gather, db_gui
from PIL import Image, ImageChops
import pyautogui
import os


# Take regional screenshots
thumbs, region_list = gather.images("NoxLogo.PNG")
#print("Images taken: %(img_count)02d" % {"img_count": len(thumbs)})

if len(thumbs) > 0:
    base_dir_path = "PVP Data/Heroes"    
    all_images = gather.seek_all(base_dir_path)
    dir_list = gather.list_items(base_dir_path)
    #print("Db Size: %(img_count)03d" % {"img_count": len(all_images)})    
    found_count = 1
    #not_found_count = 0
    for single_thumb in thumbs:
        #print("Image Index: %(img_index)03d" % {"img_index": thumb_index})
        #temp_name = "Temp%(img_index)03d.png" % {"img_index": thumb_index}
        temp_name = "Temp.png"
        single_thumb.save(temp_name)
        for single_image in all_images:            
            file_path = os.path.normpath(single_image)
            file_path = file_path.replace("\\", "/")
            db_img = Image.open(file_path)
            temp_img = Image.open(temp_name)
            pixel_difference = ImageChops.difference(db_img, temp_img).getbbox() is None
            if pixel_difference:
                #print(pixel_difference)
                print(single_image.name)
                os.remove(temp_name)
                found_count = found_count + 1
                break                
            
        if os.path.isfile(temp_name):
            db_gui.populate_db(dir_list, temp_name)
        #os.remove(temp_name)
    
    
    # Ban charaters
    # Play PVP


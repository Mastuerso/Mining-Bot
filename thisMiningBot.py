from miningbot import gather, db_gui
import pyautogui
import os


# Take regional screenshots
thumbs, region_list = gather.images("NoxLogo.PNG")
#print(len(thumbs))
#print(len(region_list))

if len(thumbs) > 0:

    new_entries = thumbs
    dir_list = gather.list_items("PVP Data/Heroes")
    #print("Available dirs: %(dir_count)01d" % {"dir_count": len(dir_list)})
    #encapsulate all inside another loop to check every thumb region    
    commom_path = os.path.commonpath(dir_list)
    count = 0
    last_count = 0
    img_index = 0
    last_finding = str
    #for thumb in thumbs:
        
        #print(img_region)
        # Compare to database
    for local_region in region_list:
        #print(local_region) 

        for single_dir in dir_list:
            single_dir_path = os.path.join(commom_path, single_dir.name)
            #find all files inside this dir
            files_inside = gather.list_items(single_dir, "f")
            #print(single_dir.name)
            for single_file in files_inside:
                #file_path = "PVP Data/Heroes/" + single_dir.name + "/" + single_file.name 
                file_path = os.path.join(single_dir_path, single_file.name)
                #print(file_path)
                
                try:
                    #print(pyautogui.locateOnScreen(currentHDir, confidence=0.6, grayscale=True))
                    heroLocation = pyautogui.locateOnScreen(file_path, grayscale=True)
                    #print(single_file.name)
                    #Banning Fase
                    #heroPoint = pyautogui.center(heroLocation)
                    #pyautogui.moveTo(heroPoint.x, heroPoint.y)
                    count = count + 1                        
                except:
                    #print("Item not Found")
                    errCount = 1
                    #new_entries.append(thumbs[not_found])
        
        if count != last_count:
            print(img_index)
            print(len(new_entries))
            last_count = count            
            del new_entries[img_index]
        else:
            img_index = img_index + 1
            print("Item not Found")
                
                
    count = count / 8    
    print("Detected: %(count)01d" % {"count": count})

    """       
        for mini_dir in dir_list:
            files_inside = gather.list_items(mini_dir, "f")
            for file_founded in files_inside:
                #print(file_founded.name)
                try:
                    # remove if found and use only results
                    #heroLocation = pyautogui.locateOnScreen(file_founded, grayscale=True, region = img_region)
                    heroLocation = pyautogui.locateOnScreen(file_founded, grayscale=False)
                    heroPoint = pyautogui.center(heroLocation)
                    pyautogui.moveTo(heroPoint.x, heroPoint.y)
                    print("heroLocation")
                    new_entries.pop(count)
                    count = count + 1
                except:
                    print("Something New")
    """
    
    if len(new_entries) > 0:
        #GUI to add new items
        print("new Stuff: %(new_entries)01d" % {"new_entries": len(new_entries)})
        
        for new_entry in new_entries:
            new_entry.save("temp.png")
            #Call GUI Here
            db_gui.populate_db(dir_list, "temp.png")
            os.remove('temp.png')
            print(new_entry)
    
    
    # Ban charaters
    # Play PVP


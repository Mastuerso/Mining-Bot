from miningbot import gather

# Take regional screenshots
thumbs, region_list = gather.images("NoxLogo.PNG")
#print(len(thumbs))
#print(len(region_list))

#prepare for count no new entries

if len(thumbs) > 0:
    new_entries = thumbs
    dir_list = gather.list_items("./PVP Data/Heroes")
    print("Available dirs: %(dir_count)01d" % {"dir_count": len(dir_list)})
    #encapsulate all inside another loop to check every thumb region    
    for img_region in region_list:
        #print(img_region)
        # Compare to database        
        for mini_dir in dir_list:
            files_inside = gather.list_items(mini_dir, "f")
            for file_founded in files_inside:
                #print(file_founded.name)
                try:
                    # remove if found and use only results
                    heroLocation = pyautogui.locateOnScreen(file_founded, grayscale=True, region = img_region)
                    print("heroLocation")
                    new_entries.remove(file_founded)                    
                except:
                    print("Something New")
    if len(new_entries) > 0:
        #GUI to add new items
        print("new Stuff: %(new_entries)01d" % {"new_entries": len(new_entries)})
    else:
        #Message that nothing new was founded
        print("Nothing new")
    
    # Ban charaters
    # Play PVP


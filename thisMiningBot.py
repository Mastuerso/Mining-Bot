from miningbot import gather
from appJar import gui
from PIL import Image, ImageTk
import os

def storage(parent, child):   
    if child == "Hidden":
        #print("Adding Hidden Hero")
        parenDir = os.path.commonpath(parent)
        #print(parenDir)
        hidden_hero = os.path.join(parenDir, "hidden_hero")
        #print(noHero)
        if not os.path.exists(hidden_hero):
            #print("Dir doesn't exists")
            os.makedirs(hidden_hero)
        thumbPath = hidden_hero
    else:
        for target in parent:
            if target.name == child:
                #print(target)
                thumbPath = target
    # storage image in the selected path
    print(thumbPath)   

def press(button):
    if button == "Ok":
        selection = app.getListBox("Hero")
        print("Adding " + selection[0] + " data")
        storage(dir_list, selection[0])
    elif button == "Hidden":        
        storage(dir_list, "Hidden")
        print("Hidden")
    elif button == "New":        
        #new gui to ask Name of Character        
        print("----------------New")
        app.showSubWindow("Add_Hero")       
    app.stop()

def add_new_char():
    selection = app.getEntry("new_Hero")
    print(selection)
    app.stop()

# Take regional screenshots
thumbs, region_list = gather.images("NoxLogo.PNG")
#print(len(thumbs))
#print(len(region_list))

if len(thumbs) > 0:
    new_entries = thumbs
    dir_list = gather.list_items("PVP Data/Heroes")
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
        
        characters_names = []
        for character in dir_list:
            characters_names.append(character.name)
        
        for new_entry in new_entries:
            with gui("Select Hero") as app:
                new_entry.save("temp.png")
                photo = ImageTk.PhotoImage(Image.open("temp.png"))
                app.addImageData("pic", photo, fmt="PhotoImage")
                app.addListBox("Hero", characters_names)
                app.selectListItemAtPos("Hero", 0)
                #Subwindow to add new Characters
                app.startSubWindow("Add_Hero", modal=True, blocking=True)
                app.addEntry("new_Hero")
                app.addButton("Add", add_new_char)                
                app.stopSubWindow()
                # link the buttons to the function called press
                app.addButtons(["Ok", "Hidden", "New"], press)
        os.remove('temp.png')
    """
    else:
        #Message that nothing new was founded
        #print("Nothing new")
        with gui("Nothing New") as app:
            app.addLabel("title", "Nothing new")
            app.addButton(["Ok"], close)
    """
    
    # Ban charaters
    # Play PVP


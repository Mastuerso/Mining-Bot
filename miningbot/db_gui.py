from appJar import gui
from PIL import Image, ImageTk
from miningbot import gather
from shutil import copyfile
import os

def populate_db(dir_list ,temp_image):
    
    def storage(parent, child):

        parenDir = os.path.commonpath(parent)
        #print(parenDir)
        adding_hero = os.path.join(parenDir, child)
        #print(noHero)
        if not os.path.exists(adding_hero):
            #print("Dir doesn't exists")
            os.makedirs(adding_hero)
        files_inside = gather.list_items(adding_hero, "f")
        files_count = len(files_inside) + 1
        file_name = child + "%(files_count)03d.png" % {"files_count" : files_count}
        print("file name: " + file_name)
        thumbPath = os.path.join(adding_hero, file_name)
        copyfile(temp_image, thumbPath)        
        print(thumbPath)   

    def press(button):
        if button == "Ok":
            selection = app.getListBox("Hero")
            print("Adding " + selection[0] + " data")
            storage(dir_list, selection[0])
            app.stop()
        elif button == "Hidden":        
            storage(dir_list, "Hidden_Sign")
            print("Hidden")
            app.stop()
        elif button == "New":        
            #new gui to ask Name of Character
            try:
                app.showSubWindow(button)               
            except: 
                print("wtf")                

    def add_new_char():
        selection = app.getEntry("new_Hero")
        storage(dir_list, selection)
        print(selection)
        app.stop()

    characters_names = []
    for directory in dir_list:
        characters_names.append(directory.name)

    #with gui("Select Hero") as app:        
    app = gui()
    photo = ImageTk.PhotoImage(Image.open(temp_image))
    app.addImageData("pic", photo, fmt="PhotoImage")
    app.addListBox("Hero", characters_names)
    app.selectListItemAtPos("Hero", 0)
    app.addButtons(["Ok", "Hidden", "New"], press)
    #Subwindow to add new Characters
    app.startSubWindow("New", modal=True)
    app.addEntry("new_Hero")
    app.addButton("Add", add_new_char)                
    app.stopSubWindow()    
    # link the buttons to the function called press
    app.go()
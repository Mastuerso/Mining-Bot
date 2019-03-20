from appJar import gui
from PIL import Image, ImageTk
import os

def populate_db(dir_list ,temp_image):

    #app = gui("Db")
    #app.addListBox("Heroes", dir_list)
    #app.go()

    
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
            app.stop()
        elif button == "Hidden":        
            storage(dir_list, "Hidden")
            print("Hidden")
            app.stop()
        elif button == "New":        
            #new gui to ask Name of Character        
            print("----------------New")
            try:
                app.showSubWindow(button)               
            except: 
                print("wtf")
                

    def add_new_char():
        selection = app.getEntry("new_Hero")
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
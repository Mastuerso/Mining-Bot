#import the library
from appJar import gui
import os

def getDirs(directory, enlist=False):    
    #print(directory)
    with os.scandir(directory) as contents:
        dirs = []
        dirls = []
        for content in contents:
            if not content.name.startswith('.') and os.path.isdir(content):
                #if directory enter and audit
                #print(content.name)
                dirs.append(content)
                dirls.append(content.name)
            elif not content.name.startswith('.') and os.path.isfile(content):
                print(content.name)
        if enlist:
            return dirs, dirls
        else:
            return dirs

def press(button):
    if button == "Ok":
        selection = app.getListBox("Hero")
        #print("Adding " + selection[0] + " data")
        storage(directories, selection[0])
    elif button == "Not Hero":        
        storage(directories, "Not Hero")
    app.stop()

def storage(parent, child):   
    if child == "Not Hero":
        #print("Adding to Not Hero")
        parenDir = os.path.commonpath(parent)
        #print(parenDir)
        noHero = os.path.join(parenDir, "Not Hero")
        #print(noHero)
        if not os.path.exists(noHero):
            #print("Dir doesn't exists")
            os.makedirs(noHero)
        thumbPath = noHero
    else:
        for target in parent:
            if target.name == child:
                #print(target)
                thumbPath = target
    # storage image in the selected path
    print(thumbPath)   

# Take regional screenshots
# Compare to database 
# Scan for new Entries
# If new entries
#   Sort new entries
# else
#   Pop up message: nothng new

directories, heroList = getDirs("PVP Data/Heroes", True)

# Slection GUI
with gui("Select Hero") as app:
    app.addListBox("Hero", heroList)
    # link the buttons to the function called press
    app.addButtons(["Ok", "Not Hero", "Cancel"], press)




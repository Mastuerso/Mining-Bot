#import the library
from appJar import gui
import os

def list_all_dirs(directory):
    dir_list = []
    with os.scandir(directory) as dir_batch:
        for single_dir in dir_batch:
            if not single_dir.name.startswith('.') and os.path.isdir(single_dir):
                dir_list.append(single_dir.name)
    return(dir_list)

dir_list = list_all_dirs("PVP Data/Heroes")
app = gui("Db Collection")
app.addListBox("Heroes", dir_list)
app.go()
    

"""
def press(button):
    if button == "Ok":
        selection = app.getListBox("Hero")
        #print("Adding " + selection[0] + " data")
        storage(directories, selection[0])
    elif button == "Hidden":        
        storage(directories, "Hidden_Hero")
    elif button == "New":
        app.showSubWindow("Add_Hero")
    app.stop()

def storage(parent, child):   
    if child == "Hidden_Hero":
        #print("Adding to Not Hero")
        parenDir = os.path.commonpath(parent)
        #print(parenDir)
        noHero = os.path.join(parenDir, "Hidden_Hero")
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

def add_new_char():
    selection = app.getEntry("new_Hero")
    print(selection)
    app.stop()   

# Take regional screenshots
# Compare to database 
# Scan for new Entries
# If new entries
#   Sort new entries
# else
#   Pop up message: nothng new

directories, heroList = getDirs("PVP Data/Heroes", True)

# Slection GUI
#with gui("Select Hero") as app:
app = gui("Hero Selection")
app.addListBox("Hero", heroList)
#Subwindow to add new Characters
app.startSubWindow("Add_Hero", modal=True, blocking=True)
app.addEntry("new_Hero")
app.addButton("Add", add_new_char)                
app.stopSubWindow()
# link the buttons to the function called press
app.addButtons(["Ok", "Hidden", "New"], press)
app.go()
"""



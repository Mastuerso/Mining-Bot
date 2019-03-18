#import the library
from appJar import gui
from PIL import Image, ImageTk

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass", pwd)
        app.stop()

#createa GUI variable called app
app = gui("Login Window", "400x300")
#app.setIcon("appJar/resources/icons/3d-cube.png")
#app.setTransparency(80)
#add & configuire widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
#
photo = ImageTk.PhotoImage(Image.open("logoTest.gif"))
app.addImageData("pic", photo, fmt="PhotoImage")
#Changing appearance
app.setFont(12)
#Adding entry boxes
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
#Placing the cursor
app.setFocus("Username")
#Buttons linking to the function called press
app.addButtons(["Submit", "Cancel"], press)
#start the GUI
app.go()

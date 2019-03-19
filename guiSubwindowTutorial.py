from appJar import gui

def launch(win):
    app.showSubWindow(win)

def print_value():
    print(app.getEntry("msg"))
    app.stop()


for i in range(0, 2):
    #print(i)
    app=gui()

    # these go in the main window
    app.addButtons(["one", "two"], launch)

    # this is a pop-up
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", "SubWindow One")
    app.addEntry("msg")
    app.addButton("Ok", print_value)
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("two")
    app.addLabel("l2", "SubWindow Two")
    app.addEntry("msg2")
    app.addButton("Oki", print_value)
    app.stopSubWindow()

    app.go()
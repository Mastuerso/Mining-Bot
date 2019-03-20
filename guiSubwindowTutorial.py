from appJar import gui
import os

def list_all_dirs(directory):
    dir_list = []
    with os.scandir(directory) as dir_batch:
        for single_dir in dir_batch:
            if not single_dir.name.startswith('.') and os.path.isdir(single_dir):
                dir_list.append(single_dir.name)
    return(dir_list)


def gui_implementation():
    
    def launch(win):
        app.showSubWindow(win)

    def print_value():
        print(app.getEntry("msg"))
        app.stop()

    dir_list = list_all_dirs("PVP Data/Heroes")

    #print(i)
    app=gui()

    app.addListBox("Heroes", dir_list)

    # these go in the main window
    app.addButtons(["one"], launch)

    # this is a pop-up
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", "SubWindow One")
    app.addEntry("msg")
    app.addButton("Ok", print_value)
    app.stopSubWindow()

    app.go()


gui_implementation()

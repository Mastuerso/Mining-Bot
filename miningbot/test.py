import gather

# Take regional screenshots
# Compare to database 
# Scan for new Entries
# If new entries
#   Sort new entries
# else
#   Pop up message: nothng new

#thumbs = gather.images("NoxLogo.PNG")
#print(len(thumbs))

dir_list = gather.list_items("./PVP Data/Heroes")
for mini_dir in dir_list:
    files_inside = gather.list_items(mini_dir, "f")
    for file_founded in files_inside:
        print(file_founded.name)



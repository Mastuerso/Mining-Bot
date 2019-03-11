import os
print (os.getcwd())
directory = "PVP Data/Heroes/Dummy"
if not os.path.exists(directory):
    os.makedirs(directory)
else:
    print("Dir already exists")
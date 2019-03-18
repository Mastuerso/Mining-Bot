import os
import argparse

#Auditing Function
def auditDir(directory, extension):    
    #print(directory)
    with os.scandir(directory) as contents:
        for content in contents:
            if not content.name.startswith('.') and os.path.isdir(content):
                #if directory enter and audit
                print(content.name)
                auditDir(content, extension)
            elif not content.name.startswith('.') and os.path.isfile(content):
                #if file to erase -- erase it   
                if content.name.endswith(extension):
                    print("DELETING..." + content.name)                    
                    os.remove(content)
                else:
                    print("----" + content.name)
                    
         
    

#Reading Args
parser = argparse.ArgumentParser\
    (description = 'Delete specific file types from Directory and subdirectory')
parser.add_argument('directory', help='Directory to Audit')
parser.add_argument('extension', help='file extension to search and remove')
args = parser.parse_args()
#print(args)
#print(args.directory)
#print(args.extension)

#Check if Dir exist
if(os.path.isdir(args.directory)):
    #Search for everything (audit)
    auditDir(args.directory, args.extension)
else:
    print("path not found in " + os.getcwd())
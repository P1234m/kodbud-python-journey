#Task 4: Automate File Renaming in a Folder
'''Explanation:
•
Write a script that renames files in a folder with a naming pattern like file_1.txt, file_2.txt
•
Use os module to access file names
Goal: Learn automation and file handling'''


import os
#give folder path
folder_path="C:\\Users\\Dell\\example"
#list of all the files in the given folder
files=os.listdir(folder_path)

files.sort()

#iterate through the files to rename them

for index,file in enumerate(files,start=1):
    _,ext=os.path.splitext(file)
    new_file=f"file_{index}{ext}"
    old_path=os.path.join(folder_path,file)
    new_path=os.path.join(folder_path,new_file)
    os.rename(old_path,new_path)  #renaming

    print(f"{file} renamed to {new_file}")
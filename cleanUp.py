import os 

for folderName, subFolders, fileName in os.walk('C:\\Users\\blee\\Desktop\\Junk'):
    os.chdir('C:\\Users\\blee\\Desktop\\Junk')
    for file in fileName:

        if file.endswith('.zip') :
            os.rmdir(file)
        elif file.endswith('.png'):
            os.rmdir(file)
        elif file.endswith('.lic'): 
            os.rmdir(file)
        elif file.endswith('log'):
            os.rmdir(file)
# This script is about copying RAW-images which are wanted for editing
# Can be used for other purposes as well, just need to change a few variables.
# This script was written on October 15th, close at 23:XX.
import os
import shutil

# Edit the following values for your needs:
rawDir = "C:/Users/Username/editableImages/raw"
rawFolderUsedForEditing = "editme"
rawSuffix = ".CR2"

editablePictures = []

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        editablePictures.append(file.split(".")[0])
        
newDir = os.chdir(rawDir)

for file in os.listdir(newDir):
    if os.path.isfile(file):
        fileName = file.split(".")[0]
        if fileName in editablePictures:
            realFileName = fileName + rawSuffix
            destination = rawDir + "/" + rawFolderUsedForEditing + "/" + realFileName
            shutil.copyfile(realFileName, destination)
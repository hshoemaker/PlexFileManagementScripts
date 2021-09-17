import os

from os import listdir
from os.path import isfile, join

# Add movies directory here
# This could be updated to ask the user to enter the directory,
#   but don't plan this to change much. So I'll keep it as a variable.
moviesDir = ""
movieCount = 0

print("Reading files.")
movieFiles = [f for f in listdir(moviesDir) if isfile(join(moviesDir, f))]

print("Generating directories and moving files.")
for file in movieFiles:
    # Supporting only .m4v and .mp4 files for now
    # I could split by "." to get the file type instead, 
    #   but this works fine for my purposes
    fileName = ".m4v"
    if (".mp4" in file):
        fileName = ".mp4"
    
    # Create the new directories
    newDirName = file.split(fileName)[0]
    newMovieDir = os.path.join(moviesDir, newDirName)
    os.mkdir(newMovieDir)

    # Move the files into their new directories of the same name
    oldFileName = os.path.join(moviesDir, file)
    newFileName = os.path.join(newMovieDir, file)
    os.replace(oldFileName, newFileName)

    # Increment count for 
    movieCount = movieCount + 1

print("Finished. Final count was " + str(movieCount))
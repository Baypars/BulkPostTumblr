import os, glob
os.chdir("images/")
for file in glob.glob("*.jpg"):
    print(file)

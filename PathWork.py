from pathlib import Path
#Check if a file/directory exists

#check if a directory code exists
Path("code").exists()


#check if a file hello.py exists
Path("code/hello.py").exists()

#Create a new directory
Path("code/submodule").mkdir()

#Move/rename a file or directory.
file =Path("code/hello.py")
file.replace("code/submodule/hello.py")

#Find the parent of a file/directory.
file =Path("code/submodule/hello.py")
file.parent
file.parent.parent

#Get the name of the file/directory.
file =Path("code/submodule/hello.py")
file.name
file.parent.name


#Find the folder a script is in
folder=Path(__file__).parent
print(folder)

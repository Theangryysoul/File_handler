import os
from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")

def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file:- ")
                fs.write(data)

            print(f"File created successfully")
        else:
            print("this file already exist")

    except Exception as err:
        print(f"An error occurred as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print(f"file read successfully")
        else:
            print("file doesn't exist")

    except Exception as err:
        print(f"An error occurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing name of file")
            print("press 2 for overwriting data of file")
            print("press 3 for appending some content in your file")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("New file name:- ")
                p2 = Path(name2)
                p.rename(p2)
            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write, this will overwrite data")
                    fs.write(data)
            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" "+ data)
    except Exception as err:
        print(f"an error occurred as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("file removes successfully ")

        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error occurred as{err} ")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("press tell your response:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()

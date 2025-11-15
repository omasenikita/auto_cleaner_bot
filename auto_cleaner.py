import os
import sys
import time
import schedule  # type: ignore

# Function: Watch and clean a directory by removing empty files
# Author: Nikita
def DirectoryWatcher(DirectoryName="Marvellous"):
    flag = os.path.isabs(DirectoryName)
    if not flag:
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("The path is invalid")
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")
        exit()

    print("Absolute path is : " + DirectoryName)

    TotalCount = 0
    EmptyCount = 0

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            TotalCount += 1
            full_path = os.path.join(FolderName, fname)
            if os.path.getsize(full_path) == 0:
                EmptyCount += 1
                print("File name is : " + fname)
                os.remove(full_path)

    timestamp = time.ctime()
    filename = "MarvellousLog%s.log" % timestamp
    filename = filename.replace(" ", "_").replace(":", "_")

    with open(filename, "w") as fobj:
        Border = "-" * 54
        fobj.write(Border + "\n")
        fobj.write("This is a log file of Marvellous Automation Script\n")
        fobj.write("This is a Directory Cleaner Script\n")
        fobj.write(Border + "\n\n")
        fobj.write(f"Total files scanned: {TotalCount}\n")
        fobj.write(f"Empty files removed: {EmptyCount}\n\n")
        fobj.write(Border + "\n")
        fobj.write("This log is created at \n" + timestamp + "\n")
        fobj.write(Border + "\n")

# Function: Entry point for command-line usage and scheduling
# Author: Nikita
def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.lower() == "--h":
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif arg.lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py NameOfDirectory")
            print("Please provide a valid absolute path")

        else:
            schedule.every(6).seconds.do(DirectoryWatcher, arg)
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

# Script trigger
# Author: Nikita
if __name__ == "__main__":
    main()
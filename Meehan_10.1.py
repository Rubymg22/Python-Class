import os


def main():
    directory = input("What is the directory you like the file to be saved to?")
    name = input("What is your name?")
    filename = input("What is your filename?")  + ".txt"
    address = input("What is your address?")
    phone_number = input("What is your phone number?")

    if os.path.isdir(directory):
        fileHandle = open(os.path.join(directory, filename),'w')
        fileHandle.write(name + ',' + address + ',' + phone_number)
        fileHandle.close()
        print("File contents: ")
        fileRead = open(os.path.join(directory, filename),'r')
        for line in fileRead:
            print(line)
        fileRead.close()

    else:
        print("Sorry that directory does not exist")


main()
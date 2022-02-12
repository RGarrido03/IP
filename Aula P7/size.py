import os

def ShowFilesSize(path):
    directory = os.listdir(path)

    for file in directory:
        print(os.stat(file).st_size)

def main():
    path = input("Please input the path: ")
    ShowFilesSize(path)

if __name__ == "__main__":
    main()

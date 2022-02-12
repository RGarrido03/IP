def loadFile(fname, lst):
    file = open(fname, "r")
    file.readline()     # Ignore the heading.
    
    for line in file:
        line_split = line.strip().split("\t")   # Split each line by tabs.
        t = int(line_split[0]), line_split[1], float(line_split[5]), float(line_split[6]), float(line_split[7]) # Define a new tuple wih those infos.
        lst.append(t)   # Add the tuple to the end of the list.
    
    return lst


def notaFinal(reg):
    average = round(((reg[2] + reg[3] + reg[4])/3), 1)
    return average


def printPauta(lst, filename):
    fileobj = open(filename, "w")
    
    # Print the heading on both the shell and the file.
    print("Número", "Nome".center(50), "Nota")
    print("Número", "Nome".center(50), "Nota", file = fileobj)
    
    for t in lst:
        line = f"{t[0]:6.0f}{t[1].center(52)}{notaFinal(t):>4}"
        print(line)
        print(line, file = fileobj)
    
    print("The grading list was saved as 'pauta.txt' on the same folder as this Python script.")

    fileobj.close()


def main():
    lst = []
    # Read the files. (PAY ATTENTION BITCHES: The next three lines require you to have those three files on the same directory as this file.)
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # Sort the list.
    lst.sort()
    
    # Print the grading list.
    printPauta(lst, "pauta.txt")


# Call the main function.
if __name__ == "__main__":
    main()

from tkinter import filedialog

def main():
    name = filedialog.askopenfilename(title="Choose File")  # Choose the file.
    total = fileSum(name)
    print("Sum:", total)


def fileSum(filename):
    fileobj = open(filename, "r")   # Open the file.
    sum = 0                         # Initialize the variable.
    
    for a in fileobj:
        sum += float(a[:-1])        # Sum every number in the file.
    
    fileobj.close()                 # Close the file.
    return sum                      # Return the sum.


if __name__ == "__main__":
    main()


from bisect import bisect_left, bisect_right

# Exercise 7
def wordList(filename):
    fileobj = open(filename, 'r', encoding="UTF-8")
    lst = [line.strip() for line in fileobj]

    ea_index = bisect_left(lst, "ea")
    eb_index = bisect_left(lst, "eb")
    print(f"There are {eb_index-ea_index} words that start with 'ea'.")

    tb_index = bisect_left(lst, "tb")
    tc_index = bisect_left(lst, "tc")
    print(f"There are {tc_index-tb_index} words that start with 'tb'.")

    t_index = bisect_right(lst, "tb")
    print(f"The letter that comes after 'b', on a word that starts with a 't', is '{lst[t_index][1]}'.")

    fileobj.close()



# Exercise 8
def prefixSearch(filename):
    fileobj = open(filename, 'r', encoding="UTF-8")
    lst = [line.strip() for line in fileobj]

    letters_available = True
    prefix = ""

    new_letter = input("Input the first letter: ")
    letters = []

    while letters_available:
        prefix += new_letter
        if len(letters) > 1:
            print(f"The current prefix is {prefix}.")

        letters = letterSearch(lst, prefix)   # Check the function letterSearch, below this one.
        if len(letters) > 1:
            if prefix not in lst:
                print("Letters available:", letters, end="\n\n")
                new_letter = input("Input the letter: ")

            else:
                confirmation = input(f"The word {prefix} exists. Do you want to continue? (yes or no): ")
                if confirmation == "yes":
                    print("Letters available:", letters, end="\n\n")
                    new_letter = input("Input the letter: ")
                else:
                    print(f"The word is {prefix}.")
                    letters_available = False

        elif len(letters) == 1:
            if prefix not in lst: new_letter = letters[0]
            else:
                confirmation = input(f"The word {prefix} exists. Do you want to continue? (yes or no): ")
                if confirmation == "yes": new_letter = letters[0]

                else:
                    print(f"The word is {prefix}.")
                    letters_available = False

        else:
            print(f"No more letters are available or the word was auto-completed. The word is {prefix}.")
            letters_available = False
    
    fileobj.close()



def letterSearch(lst, prefix):
    letters = []
    a_index = bisect_left(lst, prefix+"a")   # Note: "a_index" isn't tied to alphabet's "a".

    for b in "abcdefghijklmnopqrstuvwxyz":   # Note: "b_index" isn't tied to alphabet's "b".
        b_index = bisect_left(lst, prefix+b)
        if b_index > a_index:
            a_index = b_index
            letters += chr(ord(b)-1)   # I added chr(ord(b)-1) instead of b because, with b, it would add the letter that comes next (i.e. "p" instead of "o").

    # Do the verification for "z", since using chr(ord(b)-1) makes the "z" letter not being verified. 
    a_index = bisect_left(lst, prefix+"y")
    b_index = bisect_left(lst, prefix+"z")
    if b_index > a_index: letters += b

    return letters
 


def main():
    opt = input("Choose the exercise you'd like to run (7 or 8): ")    # Since this script has two exercises built-in, prompt the user to choose which one to run.
    print()

    if opt == "7": wordList("wordlist.txt")
    elif opt == "8": prefixSearch("wordlist.txt")
    else: main()                                                            # In case the user inputs something different from 7 or 8, run this again.

main()

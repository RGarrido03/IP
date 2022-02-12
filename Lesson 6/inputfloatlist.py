def inputFloatList():
    print("Input the numbers in each line. End the loop by input a blank line.")
    lst = []
    number = []

    while(number != [""]):
        lst += number
        number = input("")

        if number != "":
            if float(number).is_integer():
                number = [int(number)]
            else:
                number = [float(number)]
        else:
            number = [""]
    
    return(lst)

def countLower(lst, v):
    count = 0

    for a in lst:
        if a < v:
            count += 1
    
    return count

def minmax(lst):
    max = lst[0]
    min = lst[0]

    for a in lst:
        if a > max:
            max = a
        elif a < min:
            min = a
    
    average = (min + max)/2

    return average

lst = inputFloatList()
average = minmax(lst)
count = countLower(lst, average)

print(f"The list is {lst}.")
print(f"The average between the lower and the highest number is {average}.")
print(f"There are {count} elements that are lower than the average.")
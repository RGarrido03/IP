def return_index (list):
    maximum = list[0]

    for number in list:
        if maximum < number:
            maximum = number
    
    count = -1
    for number in list:
        count += 1
        if number == maximum:
            return count

def repeatNumTimes (number):
    lst = []

    for a in range(1, number + 1):
        for b in range(a):
            lst.append(a)
    
    return lst

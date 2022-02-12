# Rúben Tavares Garrido
# 107927

def mediana(lst):
    length = len(lst)
    sorted_lst = sorted(lst)

    if length%2 != 0:
        return sorted_lst[length//2]
    
    else:
        average = lambda x,y: (x+y)/2
        average(sorted_lst[length//2 - 1], sorted_lst[length//2])
        return average

def main():
    lst = [1,2,6,2,1,5,6,4]
    print(mediana(lst))

main()
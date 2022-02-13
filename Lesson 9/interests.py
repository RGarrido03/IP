def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = {(first,second):(interests[first] & interests[second])                                    # (first name, second name):(common interests)
                        for first in interests.keys()
                        for second in interests.keys()
                            if list(interests.keys()).index(second) > list(interests.keys()).index(first)}      # This removes the duplicate pairs (i.e. (x,y) and (y,x))
    print(commoninterests)

    print()
    print("b) Maximum number of common interests:")
    maxCI = max(len(value) for value in commoninterests.values())
    print(maxCI)

    print()
    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [key for key, value in commoninterests.items() if len(value)==maxCI]
    print(maxmatches)

    print()
    print("d) Pairs with low similarity:")
    lowJaccard = [key for key, value in commoninterests.items()
                  if len(value) / (len(interests.get(key[0])) + len(interests.get(key[1])) - len(value)) < 0.25]
    
    print(lowJaccard)


# Start program:
main()


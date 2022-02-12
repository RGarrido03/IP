def primesUpTo(n):
    numbers = {x for x in range(2,n+1)}
    new_numbers = {x for x in range(2,n+1)}

    for number in numbers:
        for x in range(2, n): new_numbers.discard(number*x)
    
    return new_numbers

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

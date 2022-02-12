def countdown(N):
    for x in range(N):
        N -= 1
        print(N)

N = int(input("Qual o número a decrescer? "))
print(countdown(N))
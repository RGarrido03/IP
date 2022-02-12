def mdc(a,b):
    r = a % b
    assert r >= 0

    if r == 0:
        return b
    
    else:
        return b // r

a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))

print(mdc(a,b))
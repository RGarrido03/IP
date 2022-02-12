def intersects(a1,b1,a2,b2):
    assert a1 <= b1
    assert a2 <= b2
    if b1 < a2 or b2 < a1:
        return False
    else:
        return True

a1 = int(input("Qual o valor de a1? "))
b1 = int(input("Qual o valor de b1? "))
a2 = int(input("Qual o valor de a2? "))
b2 = int(input("Qual o valor de b2? "))

print(intersects(a1,b1,a2,b2))

def hms2sec(h, m, s):
    sec = h*3600 + m*60 + s
    return sec

h = int(input("h? "))
m = int(input("m? "))
s = int(input("s? "))

print(hms2sec(h,m,s))
def sec2hms(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = (sec % 3600) % 60
    return h, m, s

sec = int(input("Quantos segundos? "))

print(sec2hms(sec))
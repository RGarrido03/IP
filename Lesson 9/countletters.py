from sys import argv

def countLetters(filename):
    fileobj = open(filename, 'r', encoding="UTF-8")
    dic = {}
    for line in fileobj:
        line_lower = line.strip().lower()

        for c in line_lower:
            if c not in dic and c.isalpha():
                dic[c] = 1
            elif c.isalpha():
                dic[c] += 1
    
    return sorted(dic.items(), key=lambda c:c[1], reverse=True)


def main():
    filename = argv[1]
    for key, value in countLetters(filename):
        print(key, value)

main()
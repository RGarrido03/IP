import sys
sys.path.insert(0, "C:/Users/ruben_ausni4w/OneDrive - Universidade de Aveiro/LEBM - 1º semestre/Introdução à Programação/Aula P6")
from matches import allmatches

WIN,DRAW,DEFEAT,GS,GC,POINTS = 0,1,2,3,4,5

def getTeams():
    print("Input the teams in each line. When finished, input an empty line, period.")
    lst = []
    name = input("")
    while name != "":
        lst.append(name)
        name = input("")
    return lst

teams = getTeams()
matchList = allmatches(teams)

def getResults(matchList):
    dic = {}
    for match in matchList:
        goals_a = int(input(f"In {match[0]} x {match[1]}, how many goals did {match[0]} score? "))
        goals_b = int(input(f"In {match[0]} x {match[1]}, how many goals did {match[1]} score? "))
        dic[match] = (goals_a, goals_b)
    return dic

results = getResults(matchList)

def table(results):
    dic = {}
    for match, score in results.items():
        for team in match:
            if team not in dic:
                dic[team] = [
                    1 if score[0] > score[1] else 0,
                    1 if score[0] == score[1] else 0,
                    1 if score[0] < score[1] else 0,
                    score[0],
                    score[1],
                    3 if score[0] > score[1] else (1 if score[0] == score[1] else 0)
                ]
            else:
                if score[0] > score[1]: dic[team][WIN] += 1
                if score[0] == score[1]: dic[team][DRAW] += 1
                if score[0] < score[1]: dic[team][DEFEAT] += 1
                dic[team][GS] += score[0]
                dic[team][GC] += score[1]
                if score[0] > score[1]: dic[team][POINTS] += 3
                elif score[0] == score[1]: dic[team][POINTS] += 1
    
    return dic

table_dic = table(results)
print()

def printTable(table):
    print("Name | W | D | D | GS | GC | P")
    print("-----|---|---|---|----|----|--")
    for name, values in table.items():
        print(f"{name:>4s} | {values[WIN]} | {values[DRAW]} | {values[DEFEAT]} | {values[GS]:2d} | {values[GC]:2d} | {values[POINTS]}")

printTable(table_dic)

def printChampion(table):
    maximum = 0
    gs_gc_difference = 0
    for name, values in table.items():
        if values[POINTS] > maximum:
            champion = name
            gs_gc_difference = values[GS] - values[GC]
            maximum = values[POINTS]
        elif values[POINTS] == maximum and (values[GS] - values[GC]) > gs_gc_difference:
            champion = name
            gs_gc_difference = values[GS] - values[GC]
    
    print(f"The champion is {champion}!")

print()
printChampion(table_dic)
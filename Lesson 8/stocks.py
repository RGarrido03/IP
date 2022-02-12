
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
	lst = loadStockFile("nasdaq.csv")
	# Show just first and last tuples:
	print("first:", lst[1])
	print("last:", lst[-1])
	print()
	
	print("a) totVol=", totalVolume(lst))
	print()

	print("b) maxVal=", maxValorization(lst))
	print()

	stocksDic = stocksByDateByName(lst)
	print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
	print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])
	print()

	port = {'NFLX': 100, 'CSCO': 80}
	print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
	print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
	lst = []
	with open(filename) as f:
		for line in f:
			parts = line.strip().split('\t')
			name = parts[NAME]
			date = parts[DATE]
			tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
				float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
			lst.append(tup)
	return lst

def totalVolume(lst):
	totVol = {}
	for tuple in lst:
		if tuple[NAME] not in totVol: totVol[tuple[NAME]] = tuple[VOLUME]
		else: totVol[tuple[NAME]] += tuple[VOLUME]
	
	return totVol

def maxValorization(lst):
	vMax = {}
	for tuple in lst:
		valorization = (tuple[MAX]/tuple[MIN])*100 - 100
		if tuple[DATE] not in vMax: vMax[tuple[DATE]] = (tuple[NAME], valorization)
		elif valorization > vMax.get(tuple[DATE])[1]: vMax[tuple[DATE]] = (tuple[NAME], valorization)

	return vMax

def stocksByDateByName(lst):
	dic = {}
	for tupl in lst:
		if tupl[DATE] not in dic:
			dic[tupl[DATE]] = {tupl[NAME] : (tupl[OPEN], tupl[MAX], tupl[MIN], tupl[CLOSE], tupl[VOLUME])}
		else: dic[tupl[DATE]].update({tupl[NAME] : (tupl[OPEN], tupl[MAX], tupl[MIN], tupl[CLOSE], tupl[VOLUME])})
	
	return dic

def portfolioValue(stocks, portfolio, date):
	assert date in stocks
	val = 0.0
	for item in portfolio.items(): val += item[1] * stocks[date][item[0]][3]-stocks[date][item[0]][0]

	return val

if __name__ == "__main__":
	main()
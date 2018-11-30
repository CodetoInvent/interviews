

def round_prices(prices, target):
	prices = map(lambda x: map(int, str(x).split('.')), prices)
	prices = sorted(prices, key=lambda x: x[1], reverse=True)
	
	total = sum([i[0] for i in prices])

	fill = target - total

	for i in range(fill): 
		prices[i][0] += 1

	return map(lambda x: x[0], prices)



print round_prices([0.70, 2.80, 4.90], 8)
# assert round_prices([0.70, 2.80, 4.90]) == [0, 3, 5]
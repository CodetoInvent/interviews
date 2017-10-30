
def sell_stocks(prices):
  profit = 0
  for i in range(1, len(prices)):
    difference = prices[i] - prices[i-1]
    if difference > 0: profit += difference

    return profit

print sell_stocks([1, 2])
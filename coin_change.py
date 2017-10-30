# Minumum number of coins to change a certain amount
#    0 1 2 3 4 5 6 7 8 9 10
#  1 0 1 2 3 4 5 6 7 8 9 10
#  2 0 1 1 2 2 3 3 4 4 5 5
#  5 0 1 1 2 2 1 2 2 3
# 10 0

def coin_change(coins, target)
  result = [[0] * (target+1) for i in range(len(coins)+1)]

  for row in range(1, len(coins)+1):
    for column in range(1, target+1):
      result[row][column] = min(

      )

coins = [1, 2, 5, 10]
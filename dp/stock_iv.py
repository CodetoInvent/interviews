# Say you have an array for which the ith element
# is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time.


# algorithm:
# i: transactions table
# j: day
# max(
#     # if we don't do any transaction
#     transactions[i][j-1],
#     # one less transaction until a day before + transaction on current day
#     transactions[i-1][j-1] + stocks[j] - stocks[j-1]
#   )
#
# algorithm:
#   maximum of:
#     - not transacting (the profit from the day before)
#     - the max profit from one less transaction + selling on current day

def max_profit(prices, k):

  transactions = [[0] * len(prices) for i in range(k+1)]

  for transaction in range(1, k+1):
    for day in range(1, len(prices)):
      not_transacting = transactions[transaction][day-1]
      selling_current_day = max(
        [
          prices[day] - prices[m] + transactions[transaction-1][m]
          for m in range(day)
        ]
      )
      transactions[transaction][day] = max(
        not_transacting,
        selling_current_day
      )
  return transactions



print max_profit([2, 3, 5, 1, 7], 3)
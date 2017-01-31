# https://www.hackerrank.com/challenges/ctci-coin-change

coins = [2, 3, 5, 6]
money = 10

memo = {}
def coin_change(coins, money, index):
    if money == 0: return 1
    if index >= len(coins): return 0

    key = '{}-{}'.format(money, index)
    if key in memo: return memo[key]

    amount_with_coins = 0
    ways = 0

    while amount_with_coins <= money:
        remaining = money - amount_with_coins
        ways += coin_change(coins, remaining, index+1)
        amount_with_coins += coins[index]

    memo[key] = ways
    return ways


print coin_change(coins, money, 0)


# without memo
def make_change(coins, money, index):
    if money == 0: return 1
    if index >= len(coins): return 0

    money_so_far = 0
    count = 0

    while money_so_far <= money:
        remaining = money - money_so_far
        count += make_change(coins, remaining, index + 1)
        money_so_far += coins[index]

    return count

print make_change(coins, money, 0)



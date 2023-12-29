from typing import List

# // writing buruteforce logic, below runs in O(n^2)
def maxProfit(prices: List[int]) -> int:
    profit = 0
    for ind, p in enumerate(prices):
        sell_ind = ind + 1
        while sell_ind < len(prices):
            if prices[sell_ind] - prices[ind] > profit:
                profit = prices[sell_ind] - prices[ind]
            sell_ind += 1
    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,5,4,3,1]))


# // two pointer, O(n)
def maxProfit2(prices: List[int]) -> int:
    profit = 0
    buy_ind, sell_ind = 0, 1
    while sell_ind < len(prices):
        if prices[buy_ind] >= prices[sell_ind]:
            buy_ind = sell_ind
        else:
            profit = max(prices[sell_ind] - prices[buy_ind], profit)
        sell_ind += 1
    return profit

print(maxProfit2([7,1,5,3,6,4]))
print(maxProfit2([7,6,5,4,3,1]))

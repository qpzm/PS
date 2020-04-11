def maxProfit(prices):
    buy, sell, profit = prices[0], -1, 0
    for price in prices[1:]:
        if sell == -1:
            if price <= buy:
                buy = price
            else:
                sell = price
        else:
            if price >= sell:
                sell = price
            else: # buy < price < sell
                profit += sell - buy
                buy, sell = price, -1

    if sell != -1:
        profit += sell - buy

    return profit

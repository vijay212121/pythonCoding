def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = sell_day = 0
    temp_buy_day = 0

    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            temp_buy_day = i
        elif price - min_price > max_profit:
            max_profit = price - min_price
            buy_day = temp_buy_day
            sell_day = i

    return max_profit, buy_day, sell_day

print(maxProfit([7, 1, 5, 3, 6, 4]))
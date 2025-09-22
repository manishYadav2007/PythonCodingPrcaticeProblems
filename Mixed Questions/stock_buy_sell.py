
"""
    The function calculates the maximum profit that can be obtained by buying and selling stocks based
    on the given prices.
    
    :param prices: The `prices` list represents the stock prices on different days. In the provided code
    snippet, the `get_stock_buy_sell` function calculates the maximum profit that can be obtained by
    buying and selling the stock on different days based on the given prices
    :return: The function `get_stock_buy_sell` calculates the maximum profit that can be obtained by
    buying and selling stocks based on the given prices. It returns the total profit that can be
    achieved.
    """

def get_stock_buy_sell(prices):
    total_profit = 0
    
    if len(prices) < 2:
        return 0 
    
    for each_item in range(len(prices) - 1):
        if prices[each_item + 1] > prices[each_item]:
            total_profit += prices[each_item + 1] - prices[each_item]
    return total_profit 
        

# prices = [100, 180, 260, 310, 40, 535, 695]
prices = [4, 2, 2, 2, 4]

result = get_stock_buy_sell(prices)
print(result)

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit            



    '''
        sells=[]
        new_prices=[]
        if prices.index(min(prices)) == len(prices)-1:
            for i in range(len(prices)-1):
                new_prices.append(prices[i])
            buy = min(new_prices)  
        else:  
            buy =min(prices)
        try:    
            for i in range(prices.index(buy)+1,len(prices)):
                diff = prices[i] -buy
                sells.append(diff)
            
            return max(sells)    

        except:
            if sum(sells) <= 0:
                return 0    '''

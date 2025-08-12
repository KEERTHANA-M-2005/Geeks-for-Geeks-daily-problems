# In a candy store, there are different types of candies available and prices[i] represent the price of  ith types of candies. You are now provided with an attractive offer.
# For every candy you buy from the store, you can get up to k other different candies for free. Find the minimum and maximum amount of money needed to buy all the candies.
# Note: In both cases, you must take the maximum number of free candies possible during each purchase.


def minMaxCandy(prices, k):
    prices.sort()
    n = len(prices)
    X = (n+k) // (k+1)
    
    min_cost = sum(prices[:X])
    
    max_cost = sum(prices[-X:])
    
    return min_cost, max_cost


Chocolates = int(input("How many variety of chocolates? "))
prices = []
for i in range(Chocolates):
    elem = int(input(f"Cost of chocolate {i+1}: "))
    prices.append(elem)
    
k = int(input("how many chocolates are free per 1 chocolates"))

result = minMaxCandy(prices, k)

print(f"The minimum and maximum cost you need to invest to get {k+1} chocolates is {result}")



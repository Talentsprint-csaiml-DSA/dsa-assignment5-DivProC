def min_coins(coins, target_amount):
    store = [target_amount+1 for i in range(target_amount+1)]
    store[0] = 0

    for amount in range(1,target_amount+1):
        for coin in coins:
            if amount - coin >= 0:
                store[amount] = min(store[amount], 1+ store[amount -coin])
    
    return store[target_amount] if store[target_amount] != target_amount + 1 else -1

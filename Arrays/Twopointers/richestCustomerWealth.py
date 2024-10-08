def richestCustomer(accounts):
    richest = 0
    for i in range(len(accounts)):
        currentRichest = 0
        for j in range(len(accounts[i])):
            currentRichest += accounts[i][j]
        if currentRichest > richest:
            richest = currentRichest

    return richest

accounts = [[1,2,3],[3,2,4],[4,5,6]]
richest = richestCustomer(accounts)
print(richest)
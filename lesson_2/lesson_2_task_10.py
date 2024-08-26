
def bank(X, Y):
    deposit = X 
    for _ in range(Y):
        deposit = deposit * 1.1
    return round(deposit)

print(bank(10000, 6))

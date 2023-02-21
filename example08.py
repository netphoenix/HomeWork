amount = int(input("Введите число: "))

coins = [25, 10, 5, 1]
num_coins = [0] * len(coins)

for i in range(len(coins)):
    num_coins[i] = amount // coins[i]
    amount %= coins[i]
    print(f"Монета {coins[i]} {num_coins[i]}")

def solve():
    heads = 8
    legs = 32

    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            print(f"Chickens: {chickens}, Rabbits: {rabbits}")
            return

solve()
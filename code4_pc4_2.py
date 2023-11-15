for k in range(9):
    if (k + 1) % 2 == 0:
        continue

    for y in range(9):

        print(f"{k + 1} * {y + 1} = {(k + 1) * (y + 1)}")
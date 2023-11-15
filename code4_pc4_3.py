for k in range(9):
    if (k + 1) % 2 == 0:
        continue

    for y in range(9):
        ans = (k + 1) * (y + 1)
        if ans > 50:
            break

        print(f"{k + 1} * {y + 1} = {ans}")
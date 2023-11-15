for k in range(9):
    if (k + 1) % 2 == 0:
        continue

    for y in range(9):
        print(f"{k + 1} * {y + 1} = {(k + 1) * (y + 1)}")


for i in range(1, 10):
    if i % 2 == 0:
        continue
    for j in range(1, 10):
        print(f"")
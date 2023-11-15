count = 1
ans = True

print("カレーを召し上がて")

while ans == True:
    print(f"{count}皿のカレーを食べました")
    key = input("おかわりはいかがですか？（y/n) >>")

    if key == "y":
        count += 1
    else:
        ans = False

print("ごちそうさまでした")
ages = [28, 50, "ひみつ", 20, 78, 25, 22, 10, "無回答", 33]
samples =list()  # サンプルデータを格納するリスト

for data in ages:
    if not isinstance(data, int):  # 整数でないデータはスキップ
        continue
    if data < 20 or data >= 30:  # 目的の条件に合致しないデータはスキップ
        continue
    samples.append(data)

print(samples)
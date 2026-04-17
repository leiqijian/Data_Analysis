
import pandas as pd

s = pd.Series(data = [i * 10 for i in range(5)], index = [i for i in 'ABCDE'])
print(f"Series对象的全部内容: {s}")
print("-----")

print(f"Series对象的索引: {s.index}")
print("-----")

print(f"Series对象的值: {s.values}")
print("-----")

print(f"通过索引下标获得索引为c的数据: {s['C']}")
print("-----")

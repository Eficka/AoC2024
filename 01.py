import pandas as pd

# 1

data_input = pd.read_csv("input01.txt", sep=r"\s+", header=None)
data_input[0] = data_input[0].sort_values(ignore_index=True)
data_input[1] = data_input[1].sort_values(ignore_index=True)
data_input[2] = (data_input[0] - data_input[1]).abs()
result = data_input[2].sum()
print(result)

# 2

data_input_02 = pd.read_csv("input01.txt", sep=r"\s+", header=None)
count_same = data_input_02[1].value_counts()
similarity = 0
for row in data_input_02[0]:
    similarity += (count_same.get(row, 0) * row)
print(similarity)
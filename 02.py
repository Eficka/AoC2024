def is_ok(row: list[int]) -> bool:
    flag = True
    for i in range(len(row) - 1):
        if 1 <= abs(row[i] - row[i+1]) <=3:
            if i == 0:
                continue
            elif (row[i-1] < row[i] < row[i+1]):
                continue
            elif (row[i-1] > row[i] > row[i+1]):
                continue
            else:
                flag = False
                break # fail
        else:
            flag = False
            break # fail
    return flag

count = 0
count_damp = 0

with open("input02.txt", mode="r", encoding="utf-8") as input:
    for line in input:
        line_list = line.split()
        line_list = list(map(int, line_list))
        if is_ok(line_list):
            count += 1
        else:
            for i in range(len(line_list)):
                if is_ok(line_list[:i] + line_list[i+1:]):
                    count_damp += 1
                    break

print(count)
print(count_damp + count)

        
    
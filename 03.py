import re 

def exec_mul(text: str) -> int:
    list_mul: list[str] = re.findall(regex, text)
    sum_mul = 0
    for mul in list_mul:
        str_mul: str = mul.replace("mul(", "").replace(")", "")
        num_str: list[str] = str_mul.split(",")
        sum_mul += int(num_str[0]) * int(num_str[1])
    return sum_mul

regex = r"mul\(\d{1,3},\d{1,3}\)"
regex_ignore = r"(?s)(?<=don't\(\)).*?(?=do\(\))"

with open("input03.txt", mode="r", encoding="utf-8") as input:
    text: str = input.read().replace("\n", "")


print(exec_mul(text=text)) # 1

text_2 = re.sub(regex_ignore, "", text) # delete parts between don't and do 
print(exec_mul(text=text_2)) # 2

data = input().split()

def cal(a, b, operator):

    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    else:
        return a * b

result_list = []

for i in range(len(data)):
    if data[i] != '+' and data[i] != '-' and data[i] != '*':
        result_list.append(int(data[i]))

    else:
        b = result_list.pop()
        a = result_list.pop()
        result_list.append(cal(a, b, data[i]))

print(result_list[0])
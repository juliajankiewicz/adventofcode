with open('advent3.txt') as f:
    lines = f.readlines()
    lines_list = []

    for element in lines:
        lines_list.append(element.replace("\n",""))

numbers_1 = ""
numbers_0 = ""

for line in lines_list:
    for i in range(len(line)):
        if line[i] == "1":
            numbers_1.append(line)
        elif line[i] == "0":
            numbers_0.append(line)

print(numbers_0)    

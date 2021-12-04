with open('advent1input.txt') as f:
    lines = f.readlines()
    a = lines
    lines_list = []
    larger_measurements = 0

    for element in a:
        lines_list.append(element.replace("\n",""))

for i in range(len(lines_list)-1):
    if len(lines_list)-1 == i:
        j = 0
    else:
        a = int(lines_list[i])
        b = int(lines_list[i+1])
        if b > a:
            larger_measurements = larger_measurements + 1
print(larger_measurements)
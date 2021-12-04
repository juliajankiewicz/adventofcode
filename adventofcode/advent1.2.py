with open('advent1input.txt') as f:
    lines = f.readlines()
    a = lines
    lines_list = []
    larger_measurements = 0

    for element in a:
        lines_list.append(element.replace("\n",""))

for i in range(len(lines_list)-1):
    if i >= len(lines_list)-3:
        j = 0
    else:
        a = int(lines_list[i])
        b = int(lines_list[i+1])
        c = int(lines_list[i+2])

        d = int(lines_list[i+1])
        e = int(lines_list[i+2])
        f = int(lines_list[i+3])

        a1 = a + b + c
        b1 = d + e + f


        if b1 > a1:
            larger_measurements = larger_measurements + 1
print(larger_measurements)
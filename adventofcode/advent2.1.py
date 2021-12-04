with open('advent2.txt') as f:
    lines = f.readlines()
    lines_list = []

    for element in lines:
        lines_list.append(element.replace("\n",""))

horizontal = 0
depth = 0


for i in range(len(lines_list)):
    splitted_line = lines_list[i].split(" ")
    if splitted_line[0] == "forward":
        horizontal = horizontal + int(splitted_line[1])
    if splitted_line[0] == "down":
        depth = depth + int(splitted_line[1])
    if splitted_line[0] == "up":
        depth = depth - int(splitted_line[1])
print(horizontal * depth)


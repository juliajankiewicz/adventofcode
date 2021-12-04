with open('advent3.txt') as f:
    lines = f.readlines()
    lines_list = []

    for element in lines:
        lines_list.append(element.replace("\n",""))

#adding to a specific index ONLY when the number is 1; then when the number of an index is >500, the number is 1
gamma_list = []
gamma_rate0 = ""
gamma_rate1 = 0

trash = 0
count = 0


for line in lines_list:
    for i in range(len(line)):
        if count == 0:
            gamma_list.append(0)
        if line[i] == "1":
            gamma_list[i] = gamma_list[i] + 1
        else:
            trash = 0
    
    count+=1

for k in range(len(gamma_list)):
    if gamma_list[k] > len(lines_list)/2 :
        gamma_rate0 = gamma_rate0 + "1"
    else:
        gamma_rate0 = gamma_rate0 + "0"

reversed_gamma = gamma_rate0[::-1]
for i in range(len(reversed_gamma)):
    if reversed_gamma[i] == "1":
        gamma_rate1 = gamma_rate1 + 2 ** i 
    else:
        trash = 0

epsilon_rate0 = gamma_rate0
for i in range(len(epsilon_rate0)-1):
    if epsilon_rate0[i] == "1":
        epsilon_rate0 = epsilon_rate0[:i] + '0' + epsilon_rate0[i+1:]
    else:
        epsilon_rate0 = epsilon_rate0[:i] + '1' + epsilon_rate0[i+1:]

if epsilon_rate0[len(epsilon_rate0)-1] == "1":
    epsilon_rate0=epsilon_rate0[:len(epsilon_rate0)-1]+'0'
else:
    epsilon_rate0=epsilon_rate0[:len(epsilon_rate0)-1]+'1'

epsilon_rate1 = 0
reversed_epsilon = epsilon_rate0[::-1]
for i in range(len(reversed_epsilon)):
    if reversed_epsilon[i] == "1":
        epsilon_rate1 = epsilon_rate1 + 2 ** i
    else:
        trash = 0

print(gamma_rate1*epsilon_rate1)



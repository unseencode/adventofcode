with open('../inputs/day1-data') as file:
    inputList = list(map(int, file.readlines()))
count = 0
for idx, line in enumerate(inputList):
    if(idx != 0 and inputList[idx] > inputList[idx-1]):
        count = count + 1
print(count)
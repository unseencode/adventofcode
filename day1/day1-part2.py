with open('day1-data') as file:
    inputList = list(map(int, file.readlines()))
max = inputList.__len__() - 3
count = 0
for idx, line in enumerate(inputList):
    current = inputList[idx] + inputList[idx - 1] + inputList[idx - 2]
    previous = inputList[idx - 1] + inputList[idx - 2] + inputList[idx - 3]
    if(current > previous):
        count = count + 1
print(count)
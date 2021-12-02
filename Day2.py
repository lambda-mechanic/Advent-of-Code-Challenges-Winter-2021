# Day 2 Part 1 Advent of Code Solution, Liam Chiasson
# Position Variables
horiz = 0
depth = 0
# Other Variables
inputs = []
count = 0
temp = ""

f = open("input_d2.txt", "r")
while(f.closed != True):
    inputs.append(f.readline())
    inputs[count] = inputs[count].strip("\n") # remove new line characters and whitespace
    temp = inputs[count]
    if(inputs[count] != ""): # If last number hasn't already passed
        if(temp[0] == 'f'): # goes forward
            horiz += int(temp[-1])
        if(temp[0] == 'u'): # goes up
            depth -= int(temp[-1])
        elif(temp[0] == 'd'): # goes down
            depth += int(temp[-1])
        count+=1
    else:
        f.close()
    print(count)

print(depth * horiz)
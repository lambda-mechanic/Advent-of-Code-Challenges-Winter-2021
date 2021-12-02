# Day 1 Part 2 Advent of Code Solution, Liam Chiasson

# (1) Read input file and copy into depths list
depths = []
f = open("input_d1.txt", "r")
count = 0
while(f.closed != True):
    depths.append(f.readline())
    if depths[count] == "":
        f.close()
        depths.pop()
    count+=1

depths = list(map(int, depths)) #Convert depths from str to int using list(map())

increased_depths = 0 #number of increases from one depth to the next
for x in range (len(depths) - 3): # To account for depths[x+3]
    if(x != len(depths) - 2): # At x == len(depths) - 2, we have no more groups of three left to compare
        sum_one = depths[x] + depths[x+1] + depths[x+2]
        sum_two = depths[x+1] + depths[x+2] + depths[x+3]
        if(sum_two > sum_one): #if increase occured, add 1 to increased_depths
            increased_depths+=1
    else:
        break
print(increased_depths)
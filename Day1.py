# Day 1 Part 1 Advent of Code Solution, Liam Chiasson

depths = []
f = open("input_d1.txt", "r")
count = 0
while(f.closed != True):
    depths.append(f.readline())
    if depths[count] == "":
        f.close()
        depths.pop()
    count+=1

depths = list(map(int, depths))
increased_depths = 0
for x in range (len(depths) - 1):
    if(depths[x+1] > depths[x]):
        increased_depths+=1
print(increased_depths)
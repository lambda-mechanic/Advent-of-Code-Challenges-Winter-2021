# Day 3 part 1 Advent of Code Solution, Liam

# Variables
gamma_rate = []
b = []
f = open("input_d3.txt", "r")
zero_tracker = [] # track number of zeros in each of 12 positions/columns
one_tracker = [] # track number of ones  in each of 12 positions/columns
iteration = 0 # iterate through all 12 000 bits as strings from input

# Initialize tracker lists with 12 ints, each starts at zero
for x in range(12): 
    zero_tracker.append(0)
    one_tracker.append(0)

# Append list b[] with all 12 000 bits as strings from input
for x in range(1000): 
    for y in range(12):
        b.append(f.read(1)) # read and append one bit at a time
    if(x != 999): 
        b.append(f.read(1)) # take newline char
        b.pop() # remove newline char
        
# Find gamma rate
for x in range(1000):
    for y in range (12): # This loop combs through b[] bit by bit, but does so in chunks of 12 in order to map each bit to a column (0 - 11) for the tracker lists
        # Check whether each bit is a one or zero, and increase either zero_tracker or one_tracker accordingly
        if (b[iteration] == "0"):
            zero_tracker[y] += 1
        elif(b[iteration] == "1"):
            one_tracker[y] +=1
        iteration+=1
for x in range(12):
    if (zero_tracker[x] > one_tracker[x]):
        gamma_rate.append("0")
    else:
        gamma_rate.append("1")

# Convert gamma_rate list to string with join() method
gamma_string = ""
gamma_string = gamma_string.join(gamma_rate)
gamma_int = int(gamma_string, 2) # argument 2 converts from binary to decimal

# Find Epsilon rate
epsilon_rate = []
for x in range(12):
    if (gamma_rate[x] == "1"):
        epsilon_rate.append("0")
    elif (gamma_rate[x] == "0"):
        epsilon_rate.append("1")

epsilon_string = ""
epsilon_string = epsilon_string.join(epsilon_rate)
epsilon_int = int(epsilon_string, 2)
# Print power consumption
print(epsilon_int * gamma_int)
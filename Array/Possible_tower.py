# // Description
# You are given a row of Lego Blocks consisting of n blocks. All the blocks given have a square base whose side length is known. You need to stack the blocks over each other and create a vertical tower. Block-1 can go over Block-2 only if sideLength(Block-2)=>sideLength(Block-1).
# From the row of Lego blocks, you on only pick up either the leftmost or rightmost block.
# Print "Possible" if it is possible to stack all n cubes this way or else print "Impossible"./*

import ast
input_str = input()
sides = ast.literal_eval(input_str)

tower=[]

while sides: #while sides is not empty
    if sides[0]>=sides[-1]:
        tower.append(int(sides[0]))
        sides.pop()
    else:
        tower.append(int(sides[-1]))
        sides.pop(-1)

#now we check if all the elements are in descending order in tower
flag=1
for i in range(len(tower)-2):
    if tower[i]<tower[i+1]:
        flag=0
        break
if(flag==1):
    print('Possible')
else:
    print('Impossible')
    
#you can try the below solution as well
'''
l=len(sides)
diff = [(sides[i]-sides[i+1]) for i in range(l-1)]
i = 0 
while (i<l-1 and diff[i]>=0) : i += 1 
while (i<l-1 and diff[i]<=0) : i += 1
if (i==l-1) : print("Possible") 
else : print("Impossible")

#to understand the code, try printing out all intermediate variables.
'''
lines=[]
with open('yob2016.txt') as f:
    lines = f.readlines()
#print(lines[0])
#String = lines[0]
#print(String)
#print(String[0])

counterE=0
for x in range(len(lines)):
    string = lines[x]
    first = string[0]
    if(first == 'E'):
        counterE += 1
print(counterE)
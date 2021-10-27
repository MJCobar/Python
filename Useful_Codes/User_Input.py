Name = input("Please Enter Name for Search: ")
#print(Name)

lines2016=[]
with open('yob2016.txt') as f:
    lines2016 = f.readlines()
    
#lines1986=[]
#with open('yob1986.txt') as k:
    #lines1986 = k.readlines()
    
counterName2016=[]
counter2016=[]
counterName1986=[]
counter1986=[]
for x in range(len(lines2016)):
    string2016 = lines2016[x]
    #string1986 = lines1986[x]
    first2016 = string2016.split(',')
    #first1986 = string1986.split(',')
    counter2016.append(int(first2016[2]))
    #counter1986.append(int(first1986[2]))
    if(first2016[0] == Name):
        #print(first2016[0],first2016[2])
        counterName2016.append(int(first2016[2]))
    #if(first1986[0] == Name):
        #print(first1986[0],first1986[2])
        #counterName1986.append(int(first1986[2]))

#print(counterName2016)
#print(counter2016)
totName2016 = sum(counter2016)
NameSum2016 = sum(counterName2016)
perName2016 = NameSum2016/totName2016*100
print(NameSum2016)
print(totName2016)
#print(perName2016)

#print(counterName1986)
#print(counter1986)
#totName1986 = sum(counter1986)
#NameSum1986 = sum(counterName1986)
#perName1986 = NameSum1986/totName1986*100
#print(NameSum1986)
#print(totName1986)
#print(perName1986)

#delPer = perName2016 - perName1986
#print(delPer)
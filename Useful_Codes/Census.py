import csv

age = []
sex = []
CenPop2010 = []
CenEst2016 = []

with open('nc-est2016-agesex-res.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    
    for row in csvReader:
        sex.append(row[0])
        age.append(row[1])
        CenPop2010.append(row[2])
        CenEst2016.append(row[10])        
#print(age)
#print(sex)
#print(CenPop2010)
#print(CenEst2016)

#print(sex[103:205])
#print(len(sex[103:205]))
MalesLarger =[]
for x in range(len(age[103:205])):
    male = int(CenPop2010[103+x])
    female = int(CenPop2010[205+x])
    male_age = int(age[103+x])
    if(male > female):
        MalesLarger.append(male_age)
        
PopDecrease =[]
for x in range(len(sex[1:103])):
    pop2010 = int(CenPop2010[1+x])
    pop2016 = int(CenEst2016[1+x])
    pop_age = int(age[1+x])
    if(pop2010 > pop2016):
        PopDecrease.append(pop_age)

MalePop2010 = []
MaleAge = []
for x in range(len(CenPop2010[103:204])):
    malepop2010 = int(CenPop2010[103+x])
    maleage = int(age[103+x])
    MalePop2010.append(malepop2010)
    MaleAge.append(maleage)
#print(MaleAge)
MalesLargest = max(MalePop2010)
#print(MalesLargest)

for x in range(len(MaleAge)):
    ma = MaleAge[x]
    mp = MalePop2010[x]
    if(mp == MalesLargest):
        MNeeded = ma
        
FemalePop2010 = []
FemaleAge = []
for x in range(len(CenPop2010[205:305])):
    femalepop2010 = int(CenPop2010[205+x])
    femaleage = int(age[205+x])
    FemalePop2010.append(femalepop2010)
    FemaleAge.append(femaleage)
#print(MaleAge)
FemalesLargest = max(FemalePop2010)
#print(FemalesLargest)

for x in range(len(FemaleAge)):
    fma = FemaleAge[x]
    fmp = FemalePop2010[x]
    if(fmp == FemalesLargest):
        FNeeded = fma

print('2010 - 2016 US Census Data Trends - By Age and Gender')
print('----------------------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------------------')
print('Males outnumber females in 2010 for these ages: ',MalesLarger)
print('--------------------------------------------------------------')
print('The age for the largest population of males in 2010 is {} with a population of {}'.format(MNeeded,MalesLargest))
print('The age for the largest population of females in 2010 is {} with a population of {}'.format(FNeeded,FemalesLargest))
print('--------------------------------------------------------------')
print('The ages for which the total population decreased between 2010 and 2016: ',PopDecrease)
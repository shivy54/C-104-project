import csv
from collections import Counter

file = open("file.csv",newline="")
reader = csv.reader(file)
newData = list(reader)

newData.pop(0)


WeightData = []
for i in range(len(newData)):
    weight = newData[i][2]
    WeightData.append(float(weight))

num = len(WeightData)



def mean(data,len):
    total = 0
    for i in data:
        total = total + i
    mean = total/len
    print("The mean/average is " + str(mean))

def median(data,num):
    data.sort()
    if num % 2 == 0 :
        median1 = (data[num//2])
        median2 = (data[num//2 -1])
        median = (median1 + median2)/2
        
    #3,5,6,4,7,3,2
    else:
        median = data[num//2]
        
    print("The median is "+ str(median))

def mode(Weightdata,num):
    data = Counter(Weightdata)
    dataRange = {"100-110":0,"111-120":0,"121-130":0,"131-140":0,"141-150":0,"151-160":0}

    for weight,occurence in data.items():
        if 100<float(weight)<110:
            dataRange["100-110"]+=occurence
        elif 111<float(weight)<120:
            dataRange["111-120"]+=occurence
        elif 121<float(weight)<130:
            dataRange["121-130"]+=occurence
        elif 131<float(weight)<140:
            dataRange["131-140"]+=occurence
        elif 141<float(weight)<150:
            dataRange["141-150"]+=occurence
        elif 151<float(weight)<160:
            dataRange["151-160"]+=occurence
    #print(dataRange)    

    modeRange,modeOccurence = 0,0
    for range,occurence in dataRange.items():
        if occurence>modeOccurence:
            modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode = float((modeRange[0]+modeRange[1])/2)
    print("The mode of the data is "+str(mode))
print("1:Mean")
print("2:Median")
print("3:Mode")
print("4:All")
fun = input("What do you want to calulate? ")
if fun == "1":
    mean(WeightData,num)
elif fun == "2":
    median(WeightData,num)
elif fun == "3":
    mode(WeightData,num)
elif fun == "4":
    mean(WeightData,num)
    median(WeightData,num)
    mode(WeightData,num)
else:
    print("Please choose one of the given numbers")
    exit()
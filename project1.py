import csv
import sys
import math
terms = []
dataObjectCount = 0
testData = []
trainingData = []
with open('fruit_data_with_colors.txt','r') as tsv:

	for line in tsv : 
		if dataObjectCount % 5 == 0 :
	
			if dataObjectCount != 0 :
				testData.append(line.strip().split('\t'))
		else :
			trainingData.append(line.strip().split('\t'))
		dataObjectCount = dataObjectCount + 1

print("Test Data " + str(testData))
print("\n\n\n\n")
print("Training Data " + str(trainingData))
print "\n\n\n\n"


trainingFeatures = []
testFeatures = []
trainingLabels = []
for line in trainingData :
	dataObject = []
	dataObject.append(float(line[5]))
	dataObject.append(float(line[6]))
	trainingLabels.append(line[0]) 
	trainingFeatures.append(dataObject)
for line in testData:
     dataObject=[]
     dataObject.append(float(line[5]))
     dataObject.append(float(line[6]))
     testFeatures.append(dataObject)



for i,testdataitem in enumerate(testData):
          mindistance=10000
          print "testdata=",testdataitem
          for j,tdataitem in enumerate(trainingData):
               distance=math.sqrt(sum([(a-b)**2 for a,b in zip(testFeatures[i],trainingFeatures[j])]))
               if(distance <= mindistance):
                   mindistance=distance
                   neighbor=j
          print "index of nearest training data=",neighbor
          print "distance=",mindistance
          print"prediction label=",trainingLabels[neighbor]
          print"\n\n\n"
          
          



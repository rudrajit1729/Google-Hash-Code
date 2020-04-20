# Solution to the practice round of Google Hash Code 2020
# Author - Rudrajit Choudhuri

def generate(MAX, inpList):#generates best solution
    finalIndexList = []    # stores the best solution index
    finalValueList = []    # stores the best solution values
    currentIndexList = []  # stores current solution index
    currentValueList = []  # stores current solution values

    SIZE = len(inpList)
    maxScore = 0  # stores maximum score achieved throughout the solution
    startIndex = SIZE  # stores index from where solution generation starts
    sum = 0

    #We start from last element of the input array
    #We stop when first element of currentIndex becomes 0 i.e. solution generated

    while ((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

        startIndex = startIndex - 1

        for i in range(startIndex, -1, -1): #Traverse from end to start to start of the inpList

            currentValue = inpList[i]
            temp = sum + currentValue

            if (temp == MAX): #If temp is equal to target that implies perfect solution found
                sum = temp
                currentIndexList.append(i)  #Add current type of pizza to the solution
                currentValueList.append(currentValue)  # Add current Pizza value to the solution
                break

            elif (temp > MAX):  # If the temporary sum is greter than target
                continue  # Try next value

            elif (temp < MAX):  # If the temporary sum is lesser than target
                sum = temp
                currentIndexList.append(i)  #Add current type of pizza to the solution
                currentValueList.append(currentValue)  # Add current Pizza value to the solution
                continue  # Try next value

        if (maxScore < sum):  #Curerently generated solution is best
            maxScore = sum  # Save its value

            finalIndexList = []
            finalValueList = []

            for index in currentIndexList:
                finalIndexList.append(index)  # Save the currently best solution indexes
            for val in currentValueList:
                finalValueList.append(val)  # Save the currently best solution values

        if (maxScore == MAX):  # If current solution is the perfect solution
            break  # Stop generating more solutions

        if (len(currentValueList) != 0):
            lastVal = currentValueList.pop()  # Remove the last element from current values
            sum = sum - lastVal  # Subtract it from sum

        if (len(currentIndexList) != 0):
            endIndex = currentIndexList.pop()  # Remove the last element from current indexes
            startIndex = endIndex  #We make it the starting index for next iteration

        if (len(currentIndexList) == 0 and (startIndex == 0)):  # If solution generating is almost finished
            break  # Stop the process

    print("SCORE = " + str(maxScore))  # Print the score of the best solution

    return finalIndexList[::-1]  # Return indexes list of the best solution


def Fileprocessor(fileName):

    #Print data to console
    print("")
    print("-----------------------")
    print(fileName)
    print("-----------------------")

    #Access the file
    inpFile = open(inputDirectory + fileName + ".in", "rt")

    #Read the file
    line1 = inpFile.readline()
    line2 = inpFile.readline()
    inpFile.close()

    #print input data
    print("INPUT")
    print(line1)
    print(line2)

    #Assign the parameters
    MAX, NUM = list(map(int,line1.split()))

    #Creating the pizza list
    inpList = list(map(int,line2.split()))
    outList = generate(MAX, inpList) # Generate best solution

    #Print output data and create output file
    print("")
    print("OUTPUT")
    print(len(outList))

    result = ""
    for i in outList:
        result = result + str(i) + " "
    print(result)

    outFile = open(outputDirectory + fileName + ".out", "w")
    outFile.write(str(len(outList)) + "\n")
    outFile.write(result)
    outFile.close()

files = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  # File names
inputDirectory =  "Input/"  # Location of input files
outputDirectory = "Output/" # Location of output files

for file in files:
    Fileprocessor(file)



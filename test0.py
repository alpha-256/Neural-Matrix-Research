
#create 64x64 square
x = [[0 for _ in range(8)] for _ in range(8)]

def printNet():
    for subArray in x:
        strArray = []
        for index in subArray:
            #convert integer to string
            toString = str(index)

            #Format string
            formatedString = "{:>2}".format(toString)

            strArray.append(formatedString)

        joinedText = "".join(strArray)
        #Join text together
        print(joinedText)

def createDefaultWeb(x):
    for xPos in range(len(x)):
        if xPos == 7:
            pass
        elif xPos < 7:
            xPos += 1
            for yPos in range(len(x)):
                if yPos == 7:
                    pass
                elif yPos < 7:
                    yPos += 1
                    x[xPos][yPos] = "\\"
                else:
                    pass
        else:
            pass
createDefaultWeb(x)
printNet()

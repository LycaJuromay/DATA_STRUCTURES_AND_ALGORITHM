import matplotlib.pyplot as plt

print("List of Problems :")
print("#1 - x^2 + 7x + 2")
print("#2 - 3x + 2")
print("#3 - x^2")
print("#4 - x^3")
print("#5 - x^5")
print("#6 - x^3 + 2x^2 +  x + 10")
print("#7 - x^4 - 3x^3 + 2x^2 - x + 11")
print("#8 - sin(x)")
print("#9 - cos(x)")
print("#10 - x^5 + 4x^4 + x^3 - 2x^2 + 100")
print("#11 - Plot All Problem")
print()
option = input("Enter the number of problem to plot: ")

def prob1(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append((value * value) + (7 * value) + 2)#formula to solve problem
    with open('OP1.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob1()

if option=="1": 
    def plotDisplay():
        plt.plot(prob1(), "p" ,label="Problem 1")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob2(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append((3 * value) + 2)#formula to solve problem
    with open('OP2.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob2()

if option=="2": 
    def plotDisplay():
        plt.plot(prob2(), "g-" ,label="Problem 2")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob3(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append(value * value)#formula to solve problem
    with open('OP3.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob3()

if option=="3": 
    def plotDisplay():
        plt.plot(prob3(), "r" ,label="Problem 3")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob4(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append(value * value * value)#formula to solve problem
    with open('OP4.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob4()

if option=="4": 
    def plotDisplay():
        plt.plot(prob4(), "b" ,label="Problem 4")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob5(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append(value * value * value * value * value)#formula to solve problem
    with open('OP5.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob5()

if option=="5": 
    def plotDisplay():
        plt.plot(prob5(), "y" ,label="Problem 5")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob6(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append((value * value * value)+(2 * (value * value)) + value + 10 )#formula to solve problem
    with open('OP6.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob6()

if option=="6": 
    def plotDisplay():
        plt.plot(prob6(), "v" ,label="Problem 6")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob7(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append((value * value * value * value)-(3 * (value * value * value)) + (2*(value * value)) - value + 11 )#formula to solve problem
    with open('OP7.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob7()

if option=="7": 
    def plotDisplay():
        plt.plot(prob7(), "y" ,label="Problem 7")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob8(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append(0.01745240644 * value)#formula to solve problem
    with open('OP8.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob8()

if option=="8": 
    def plotDisplay():
        plt.plot(prob8(), "o" ,label="Problem 8")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

def prob9(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append(0.99984769516* value)#formula to solve problem
    with open('OP9.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob9()

if option=="9": 
    def plotDisplay():
        plt.plot(prob9(), "y" ,label="Problem 9")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()


def prob10(): 
    answer = []
    InputFile = open('SB.txt','r')#read numbers on txt file
    for x in InputFile.readlines():
        value = int(x)#convert to int
        answer.append((value * value * value * value * value)+(4 * (value * value * value * value)) + (value * value  * value) - (2 * (value * value)) + 100 )#formula to solve problem
    with open('OP10.txt', 'w') as output:#save the answer on txt file
        for ans in answer:
            output.write(str(ans) + '\n')#convert into strings
    return answer
prob10()

if option=="10": 
    def plotDisplay():
        plt.plot(prob10(), "y" ,label="Problem 10")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()

if option=="11":
    def plotDisplay():
        plt.plot(prob1(),"m", label = "Problem 1")
        plt.plot(prob2(),"r", label = "Problem 2")
        plt.plot(prob3(),"g", label = "Problem 3")
        plt.plot(prob4(),"y", label = "Problem 4")
        plt.plot(prob5(),"g-", label = "Problem 5")
        plt.plot(prob6(),"m", label = "Problem 6")
        plt.plot(prob7(),"r", label = "Problem 7")
        plt.plot(prob8(),"g", label = "Problem 8")
        plt.plot(prob9(),"g-", label = "Problem 9")
        plt.plot(prob10(),"y", label = "Problem 10")
        plt.xlabel("Value of X")
        plt.ylabel("Answer")
        plt.show()
    plotDisplay()
    

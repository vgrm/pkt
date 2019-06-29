# L1 Python uzduotis Valdas Germanauskas IFF-6/14
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=11&page=show_problem&problem=888

import math
fileName = "data.txt"


class Guess:
    # test condition object
    def __init__(self, guess, black, white):
        self.guess = guess
        self.black = black
        self.white = white


class Code:
    def __init__(self, guessLength):
        self.combinations = []
        self.guessLength = guessLength

    # generates all possible combinations
    def generateCombinations(self):
        start = 0
        for power in range(self.guessLength):
            start += math.pow(10, power)
        end = math.pow(10, self.guessLength)

        for x in range(int(start), int(end)):
            flag = True
            s = list(str(x))
            for symbol in s:
                if(symbol == "0"):
                    flag = False
            if(flag == False):
                continue
            self.combinations.append(s)

        return self.combinations

    # prints number of possible secret codes
    def evaluate(self, guessCode):
        possibleCodes = 0
        # check every combination againts tested one
        # get number or black and white pegs for each combination
        for i in range(self.countCombinations()):
            black = self.checkBlack(guessCode, self.combinations[i])
            white = self.checkWhite(guessCode, self.combinations[i]) - black
            # if number of black and white pegs overlap with test condition
            # possible secret code count increases
            if(black == int(guessCode.black) and white == int(guessCode.white)):
                possibleCodes += 1
        #print(guessCode.guess, guessCode.black, guessCode.white, possibleCodes)
        print(possibleCodes)

    # returns number of black pegs (correct color and correct position)
    def checkBlack(self, guessCode, correctCode):
        black = 0
        for x in range(self.guessLength):
            if(guessCode.guess[x] == correctCode[x]):
                black += 1
        return black

    # returns number of white pegs (correct color wrong position)
    def checkWhite(self, guessCode, correctCode):
        white = 0
        tempCorrect = guessCode.guess.copy()

        for i in range(self.guessLength):
            for j in range(self.guessLength):
                if(tempCorrect[j] == correctCode[i]):
                    white += 1
                    tempCorrect[j] = 0
                    j = self.guessLength+1
                    break
        return white

    # returns number of all combinations
    def countCombinations(self):
        defaultString = "0"*self.guessLength
        count = 0
        for x in self.combinations:
            if(x != defaultString):
                count += 1

        return count


class Executor:
    def __init__(self):
        self.count = 0  # number of test cases
        self.guessList = []  # test cases list
        self.readData()  # read test data from file

        # for each test case conduct tests
        for i in range(self.count):
            self.code = Code(len(self.guessList[i].guess))
            self.code.generateCombinations()
            self.code.evaluate(self.guessList[i])

    # construct object from line string
    def parseLine(self, line):
        self.guess = line.split()
        return Guess(list(self.guess[0]), self.guess[1], self.guess[2])

    # read test data
    def readData(self):
        file = open(fileName, "r")
        self.count = int(file.readline())
        for x in range(self.count):
            line = file.readline()
            self.guessList.append(self.parseLine(line))


# execute program
execute = Executor()

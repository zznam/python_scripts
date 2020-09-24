"""
Correct Path
    Have the function CorrectPath(str) read the str parameter being passed,
    which will represent the movements made in a 5x5 grid of cells starting from the top left position.
    The characters in the input string will be entirely composed of: r, l, u, d, ?.
    Each of the characters stand for the direction to take within the grid,
    for example: r = right, l = left, u = up, d = down.
    Your goal is to determine what characters the question marks should be in order
    for a path to be created to go from the top left of the grid all the way to the bottom right
    without touching previously travelled on cells in the grid.

    For example: if str is "r?d?drdd" then your program should output
    the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right.
    For this input, your program should therefore return the string "rrdrdrdd".
    There will only ever be one correct path
    and there will always be at least one question mark within the input string.
    Examples
    Input: "???rrurdr?"
    Output: dddrrurdrd
    Input: "drdr??rrddd?"
    Output: drdruurrdddd
"""
import time
start_time = time.time()

def getOpposite(char):
    if (char == "u"):
        return "d"
    if (char == "d"):
        return "u"
    if (char == "r"):
        return "l"
    if (char == "l"):
        return "r"
    return ""


class Cell:
    def __init__(self, r=0, c=0):
        self.row = r
        self.col = c

    def getData(self):
        return ("({0},{1})".format(self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return self.row != other.row or self.col != other.col


def countMark(pathList):
    count = 0
    for e in pathList:
        if (e == "?"):
            count += 1
    return count


def checkCorrectPath(pathList):
    curCol = 0
    curRow = 0
    travelledCells = []
    travelledCells.append(Cell(0, 0))
    for i in pathList:
        if (i == "?"):
            # print(" ".join(x.getData() for x in travelledCells))
            return False
        if (i == "u"):
            curRow -= 1
        if (i == "d"):
            curRow += 1
        if curRow > 4:
            return False
        if (i == "l"):
            curCol -= 1
        if (i == "r"):
            curCol += 1
        if curCol > 4:
            return False
        cell = Cell(curRow, curCol)
        if(cell in travelledCells):
            return False
        travelledCells.append(cell)
    # print(" ".join(x.getData() for x in travelledCells))
    # print(travelledCells[-1].getData())
    if (travelledCells[-1] == Cell(4, 4)):
        return True
    return False

def checkTempPathCorrect(pathList):
    curCol = 0
    curRow = 0
    travelledCells = []
    travelledCells.append(Cell(0, 0))
    for i in pathList:
        if (i == "?"):
            # print(" ".join(x.getData() for x in travelledCells))
            return True
        if (i == "u"):
            curRow -= 1
        if (i == "d"):
            curRow += 1
        if curRow > 4 or curRow < 0:
            return False
        if (i == "l"):
            curCol -= 1
        if (i == "r"):
            curCol += 1
        if curCol > 4 or curCol < 0:
            return False
        cell = Cell(curRow, curCol)
        if(cell in travelledCells):
            return False
        travelledCells.append(cell)
    # print(" ".join(x.getData() for x in travelledCells))
    # print(travelledCells[-1].getData())
    if (travelledCells[-1] == Cell(4, 4)):
        return True
    return False


ALL_MOVES = ["u", "r", "l", "d"]


def findCorrectList(pathList):
    length = len(pathList)
    for i in range(length):
        if (pathList[i] == "?"):
            tempList = pathList.copy()
            excludeMoves = []
            if (i == 0):
                if (tempList[1] != "?"):
                    excludeMoves.append(getOpposite(tempList[1]))
            else:
                if (tempList[i-1] != "?"):
                    excludeMoves.append(getOpposite(tempList[i-1]))
                if (i != length - 1 and tempList[i+1] != "?"):
                    excludeMoves.append(getOpposite(tempList[i+1]))
            for e in set(ALL_MOVES) - set(excludeMoves):
                tempList[i] = e
                # print(str(i)+": " + "".join(tempList))
                ret = findCorrectList(tempList)
                if (checkCorrectPath(ret)):
                    return ret
    return pathList


def CorrectPath(string):
    pathList = list(string)
    pathList = findCorrectList(pathList)

    return "".join(pathList)


# keep this function call here
print(CorrectPath("???rrurdr?"))  # dddrrurdrd
print(CorrectPath("drdr??rrddd?"))  # drdruurrdddd
# print(checkCorrectPath("drdruurrdddd"))  # drdruurrdddd
# print(checkCorrectPath("dddrrurdrd"))  # drdruurrdddd
# print(CorrectPath(input()))
print("--- %s seconds ---" % (time.time() - start_time))


# importing numpy
import numpy as np
from sys import stdout
from time import sleep
from pathlib import Path


class Point:
    name: str
    coord = np.array([0.0, 0.0, 0.0])

    def __init__(self, name):
        self.name = name

    def isEqual(self, otherPoint):
        return np.array_equal(self.coord, otherPoint.coord)

    def getNumInput(self, name):
        num = 0
        isNumber = False
        while not isNumber:
            num = input(name + " = ")
            try:
                num = float(num)
                isNumber = True
            except Exception as e:
                print("Invalid number! Please input again")
        return num

    def setCoord(self, x, y, z):
        self.coord = np.array([x, y, z])

    def input(self):
        print("Enter coordinates of " + self.name + ":")
        x = self.getNumInput("x")
        y = self.getNumInput("y")
        z = self.getNumInput("z")
        self.setCoord(x, y, z)

    def toString(self):
        return (self.name + "(" + str(self.coord[0]) + ", " +
                str(self.coord[1]) + ", " + str(self.coord[2]) + ")")


class Line:
    name: str
    # one containted point
    point: Point("")
    # direction vector
    dVector: np.array

    def __init__(self, point1, point2):
        self.name = point1.name + point2.name
        self.point = point1
        self.dVector = point2.coord - point1.coord

    def distanceWithLine(self, line):
        # P is a point in line CD, Q is in a point in line AB
        pqVec = line.point.coord - self.point.coord
        # cross product of two direction vectors
        crossVec = np.cross(self.dVector, line.dVector)
        # check if two lines are parallel/coinciding
        if (np.count_nonzero(crossVec) == 0):
            # parallel/coinciding
            crossVec2 = np.cross(self.dVector, pqVec)
            numerator = np.linalg.norm(crossVec2)
            denominator = np.linalg.norm(self.dVector)
            return numerator / denominator
        # skew  lines
        numerator = np.linalg.norm(np.dot(crossVec, pqVec))
        denominator = np.linalg.norm(crossVec)
        return numerator / denominator


def distanceByFourPts(pointA, pointB, pointC, pointD):
    # return distance between line AB and line CD
    if (pointA.isEqual(pointB) or pointC.isEqual(pointD)):
        print("Dupicated points, could not made a line...")
    else:
        lineAB = Line(pointA, pointB)
        lineCD = Line(pointC, pointD)
        print("The distance between line", lineAB.name, "and", lineCD.name,
              "is", lineAB.distanceWithLine(lineCD))
    print("_____________________")


def readFileAndCal():
    # read test case files and calculate
    fileList = ["testcase_1.txt", "testcase_2.txt", "testcase_3.txt"]
    for fileName in fileList:
        try:
            fileName = "./" + fileName
            path = Path(__file__).parent / fileName
            print("File Name: " + fileName)
            f = open(path, "r")
            input = f.read()
            arrName = ["A", "B", "C", "D"]
            arrPts = []
            i = 0
            for line in input.splitlines():
                coord = line.split(" ")
                point = Point(arrName[i])
                point.setCoord(float(coord[0]), float(coord[1]),
                               float(coord[2]))
                print(point.toString())
                arrPts.append(point)
                i = i + 1

            distanceByFourPts(arrPts[0], arrPts[1], arrPts[2], arrPts[3])
        except Exception as e:
            print("Invalid input" + " (" + str(e) + ")")


def calFromInput():
    # let user input then calculate the distance
    isLine = False
    while (not isLine):
        pointA = Point("A")
        pointA.input()

        pointB = Point("B")
        pointB.input()


        if (pointA.isEqual(pointB)):
            print(
                "Dupicated points, could not made a line. Please input again")
        else:
            isLine = True
    isLine = False
    while (not isLine):
        pointC = Point("C")
        pointC.input()

        pointD = Point("D")
        pointD.input()

        if (pointC.isEqual(pointD)):
            print(
                "Dupicated points, could not made a line. Please input again")
        else:
            isLine = True
    print(pointA.toString())
    print(pointB.toString())
    print(pointC.toString())
    print(pointD.toString())
    distanceByFourPts(pointA, pointB, pointC, pointD)


text1 = "Welcome Emoclew!\nThis script to find distance between 2 distinguish straight lines"\
            "\nnamed AB and CD which are built from 4 arbitrary points.\n"
for i in range(0, len(text1)):
    stdout.write("%s" % text1[i])
    sleep(0.01)

isRightChoice = False
while (not isRightChoice):
    text2 = "Please type:\n[1] To get input from keyboard\n[2] To get input from a testcase file\n[3] To exit"
    for i in range(0, len(text2)):
        stdout.write("%s" % text2[i])
        sleep(0.01)
    stdout.write("\n")  # move the cursor to the next line
    choice = input()
    if (choice == "1"):
        isRightChoice = True
        calFromInput()
    elif (choice == "2"):
        isRightChoice = True
        readFileAndCal()
    elif (choice == "3"):
        isRightChoice = True
        print("Exiting...")

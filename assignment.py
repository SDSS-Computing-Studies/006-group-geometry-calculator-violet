#!python3
# Volume Calculator
# Feel free to rename your variables
import math
measurements = []
shape = 0
lists = ["Triangle prism", "Rectangular prism", "Cone", "Sphere", "Cylinder"]
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("-----------Graphic Calculator----------")
    print("          Made by Sanghyun Yang         ")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:

    print("Welcom to my grapic calculator.")
    print("My calculator provide 5 calculation, sphere, cylinder, traiangle and rectangle prism, and cone.")
    print("Once you are asked to answer shape, available order command is")
    print("'Sphere', 'Cylinder', 'Triangle prism', 'Rectangular prism', and 'Cone'")
    print("\n")
    print("If you want to quit this program, type 'Quit', when you are asked to answer shape")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    if shape == "Triangular prism":
        volume = 0.5 * measurements[0] * measurements[1] *measurements [2]
    elif shape == "Rectangular prism":
        volume = measurements[0] * measurements[1] *measurements [2]
    elif shape == "Cone":
        volume = (1/3) * (measurements[0] ** 2) * measurements[1] * math.pi
    elif shape == "Cylinder":
        volume = (measurements[0] ** 2) * measurements[1] * math.pi
    elif shape == "Sphere":
        volume = (4/3) * math.pi * (measurements[0] ** 3)
    elif shape == "Quit":
        volume = "Not exist"
        quit
    return volume

def getInputs(shape):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    if shape == "Triangular prism":
        print("What is length?: ", end='')
        measurements.append(float(input()))
        print("What is width?: ", end='')
        measurements.append(float(input()))
        print("What is height?: ", end='')
        measurements.append(float(input()))
    elif shape == "Rectangular prism":
        print("What is length?: ", end='')
        measurements.append(float(input()))
        print("What is width?: ", end='')
        measurements.append(float(input()))
        print("What is height?: ", end='')
        measurements.append(float(input()))
    elif shape == "Cone":
        print("what is radius?: ", end='')
        measurements.append(float(input()))
        print("What is height?: ", end='')
        measurements.append(float(input()))
    elif shape == "Cylinder":
        print("What is radius?: ", end='')
        measurements.append(float(input()))
        print("What is height?: ", end='')
        measurements.append(float(input()))
    elif shape == "Sphere":
        print("What is radius?: ", end='')
        measurements.append(float(input()))
    elif shape == "Quit":
        quit
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    shape = 0
    while shape != "Quit":
        shape = input("What is shape?: ")
        if shape == "Quit":
            print("You choose to end this program")
            quit
        elif shape != "Quit":
            if shape in lists:
                getInputs(shape)
                vol = str(getParams(shape))
                sha = str(shape) 
                print("The volume of " + sha + " is " + vol + ".")
            else:
                print("You entered undefined shape or command. Try again. Do you want to see instruction again?")
                print("Type Y or N")
                ans = input()
                if ans == "Y":
                    instructions()
                else:
                    asdhakjhk = 0
main()

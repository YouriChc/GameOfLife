import sys, getopt
from tkinter import *
import copy

master = Tk()
w = None
generation = []
listGeneration = []
numberOfGeneration = 1

# Main programm
def gameOfLife(width, height, speed):
    global generation
    global listGeneration
    global w

    generation = [[0 for x in range(width)] for y in range(height)]

    middleX = int(width / 2)
    middleY = int(height / 2)
    generation[middleX][middleY] = 1
    generation[middleX][middleY + 1] = 1
    generation[middleX + 1][middleY -1] = 1
    generation[middleX + 1][middleY] = 1
    generation[middleX + 2][middleY] = 1
    listGeneration = copy.deepcopy(generation)
    
    w = Canvas(master, width=width, height=height)

    while True:
        master.after(speed, evolve())
        w.pack()
        master.update_idletasks()
        master.update()
    master.mainloop()

# Evolution of generation
def evolve():
    global generation
    global listGeneration
    global numberOfGeneration

    sizeY = len(generation[0])
    
    for index in range(len(generation)):
        for i in range(sizeY):
            numberOfAlive = 0
            if index + 1 < len(generation):
                if listGeneration[index + 1][i] == 1:
                    numberOfAlive = numberOfAlive + 1
                if i + 1 < sizeY:
                    if listGeneration[index + 1][i + 1] == 1:
                        numberOfAlive = numberOfAlive + 1
                if i - 1 >= 0:
                    if listGeneration[index + 1][i - 1] == 1:
                        numberOfAlive = numberOfAlive + 1

            if index - 1 >= 0:
                if listGeneration[index - 1][i] == 1:
                    numberOfAlive = numberOfAlive + 1
                if i + 1 < sizeY:
                    if listGeneration[index - 1][i + 1] == 1:
                        numberOfAlive = numberOfAlive + 1
                if i - 1 >= 0:
                    if listGeneration[index - 1][i - 1] == 1:
                        numberOfAlive = numberOfAlive + 1

            if i + 1 < sizeY:
                if listGeneration[index][i + 1] == 1:
                    numberOfAlive = numberOfAlive + 1
            if i - 1 >= 0:
                if listGeneration[index][i - 1] == 1:
                    numberOfAlive = numberOfAlive + 1
            
            
            if listGeneration[index][i] == 1:
                if numberOfAlive < 2 or numberOfAlive > 3:
                    generation[index][i] = 0
            else:
                if numberOfAlive == 3:
                    generation[index][i] = 1
    listGeneration = copy.deepcopy(generation)
    numberOfGeneration = numberOfGeneration + 1
    drawSquare()

# Draw squares with the given generation
def drawSquare():
    global w
    global generation

    sizeY = len(listGeneration[0])
    w.delete("all")
    for index in range(len(listGeneration)):
        for i in range(sizeY):
            if listGeneration[index][i] == 1:
                w.create_rectangle(i, index, i + 1, index + 1, fill="black")
    w.create_text(8, 8, fill="darkblue", font="Times 8", text=numberOfGeneration)

# Launch arguments
def main(argv):
    width = ''
    height = ''
    speed = ''
    try:
        opts, args = getopt.getopt(argv,"Hw:h:s:",["width=","height=","speed="])
    except getopt.GetoptError:
        print('Bad parameters ! Run command with -H option for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-H':
            print('Choose the width and the height of the table with -w and -h\n')
            print('And choose the rule to generate with -r\n')
            print('The final command should be: gameOfLife.py -w <width> -h <height> -s <speed>\n')
            sys.exit()
        elif opt in ("-w", "--width"):
            try:
                width = int(arg)
            except ValueError:
                print('-w: Option width need to be an int')
                return
        elif opt in ("-h", "--height"):
            try:
                height = int(arg)
            except ValueError:
                print('-w: Option height need to be an int')
                return
        elif opt in ("-s", "--speed"):
            try:
                speed = int(arg)
            except ValueError:
                print('-s: Option speed need to be an int')
                return
    if width != '' and height != '' and speed != '':
        gameOfLife(width, height, speed)
    else:
        print('Run command with -H option for help')

if __name__ == "__main__":
    main(sys.argv[1:])
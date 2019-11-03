from graphics import *
import random
import string


def controlPanel():
    # Create control panel
    # create window
    cp = GraphWin('Welcome to:', 400, 400)
    # set background color to light grey
    cp.setCoords(0, 0, 400, 400)
    cp.setBackground('light grey')
    # Make the title with gold font in a black box
    titlebox = Rectangle(Point(0, 370), Point(400, 400))
    titlebox.setFill('black')
    titlebox.draw(cp)
    title = Text(Point(200, 385), "GUESS MASTER 2.0")
    title.setStyle("bold")
    title.setFill('gold')
    title.setSize(18)
    title.draw(cp)
    # Make a gold 'new game' button with black font
    newbox = Rectangle(Point(70, 290), Point(130, 320))
    newbox.setFill('gold')
    newbox.draw(cp)
    new = Text(Point(100, 305), "NEW")
    new.setStyle("bold")
    new.draw(cp)
    # Make a black 'quit game' button with gold font
    quitbox = Rectangle(Point(270, 290), Point(330, 320))
    quitbox.setFill('black')
    quitbox.draw(cp)
    quit1 = Text(Point(300, 305), "QUIT")
    quit1.setFill('gold')
    quit1.setStyle("bold")
    quit1.draw(cp)
    # Display game description
    desbox = Rectangle(Point(60, 240), Point(340, 110))
    desbox.setFill('white')
    desbox.draw(cp)
    des1 = Text(Point(200, 200), 'This is a game where your score is')
    des2 = Text(Point(200, 175), 'based on the number of 4-6 letter')
    des3 = Text(Point(200, 150), 'words you can guess within 10 tries.')
    des1.draw(cp)
    des2.draw(cp)
    des3.draw(cp)
    # Display instructions
    inst = Text(Point(200, 60), 'Click NEW to start a game...')
    inst.setSize(18)
    inst.draw(cp)
    return newbox, quitbox, cp


def gamePanel():
    # Create Window
    gp = GraphWin('Save the Block P', 400, 450)
    gp.setCoords(0, 0, 400, 450)
    # Set Background color to gold
    gp.setBackground('gold')
    # Display score text
    score = Text(Point(200, 428), "SCORE:\t")
    score.draw(gp)
    # Make the keyboard
    # for loop to make circles
    # Create a list of ALL keyboard letter buttons
    circle = []
    # row 1
    for place1 in range(0, 13 * 14, 14):
        circle1 = Circle(Point(32 + (2 * place1), 50), 14)
        circle1.draw(gp)
        circle1.setFill('black')
        # add to list
        circle.append(circle1)
    # row 2
    for place2 in range(0, 13 * 14, 14):
        circle2 = Circle(Point(32 + (2 * place2), 20), 14)
        circle2.draw(gp)
        circle2.setFill('black')
        # add to list
        circle.append(circle2)
    # print the alphabet
    # list of letters
    letter = list(string.ascii_uppercase)
    # loops for the letter buttons
    # row 1
    for i in range(0, 26):
        alph = Text((circle[i].getCenter()), letter[i])
        alph.draw(gp)
        alph.setFill('white')
    # Make the Purdue blocks
    # Bottom layer of P (to be exposed)
    under1 = Polygon(Point(130, 90), Point(135, 130), Point(200, 130), Point(195, 90))
    under1.setFill('white')
    under1.draw(gp)
    under2 = Polygon(Point(145, 130), Point(150, 180), Point(195, 180), Point(190, 130))
    under2.setFill('white')
    under2.draw(gp)
    under3 = Polygon(Point(150, 180), Point(155, 230), Point(200, 230), Point(195, 180))
    under3.setFill('white')
    under3.draw(gp)
    under4 = Polygon(Point(155, 230), Point(160, 280), Point(205, 280), Point(200, 230))
    under4.setFill('white')
    under4.draw(gp)
    under5 = Polygon(Point(160, 280), Point(165, 330), Point(210, 330), Point(205, 280))
    under5.setFill('white')
    under5.draw(gp)
    under6 = Polygon(Point(205, 280), Point(210, 330), Point(250, 330), Point(245, 280))
    under6.setFill('white')
    under6.draw(gp)
    under7 = Polygon(Point(245, 280), Point(250, 330), Point(290, 330), Point(285, 280))
    under7.setFill('white')
    under7.draw(gp)
    under8 = Polygon(Point(240, 230), Point(245, 280), Point(285, 280), Point(280, 230))
    under8.setFill('white')
    under8.draw(gp)
    under9 = Polygon(Point(235, 180), Point(240, 230), Point(280, 230), Point(275, 180))
    under9.setFill('white')
    under9.draw(gp)
    under10 = Polygon(Point(200, 230), Point(195, 180), Point(235, 180), Point(240, 230))
    under10.setFill('white')
    under10.draw(gp)
    # Top exposed layer of P
    # Create list of blocks
    block = []
    block1 = Polygon(Point(130, 90), Point(135, 130), Point(200, 130), Point(195, 90))
    block1.setFill('black')
    block1.draw(gp)
    block.append(block1)
    block2 = Polygon(Point(145, 130), Point(150, 180), Point(195, 180), Point(190, 130))
    block2.setFill('black')
    block2.draw(gp)
    block.append(block2)
    block3 = Polygon(Point(150, 180), Point(155, 230), Point(200, 230), Point(195, 180))
    block3.setFill('black')
    block3.draw(gp)
    block.append(block3)
    block4 = Polygon(Point(155, 230), Point(160, 280), Point(205, 280), Point(200, 230))
    block4.setFill('black')
    block4.draw(gp)
    block.append(block4)
    block5 = Polygon(Point(160, 280), Point(165, 330), Point(210, 330), Point(205, 280))
    block5.setFill('black')
    block5.draw(gp)
    block.append(block5)
    block6 = Polygon(Point(205, 280), Point(210, 330), Point(250, 330), Point(245, 280))
    block6.setFill('black')
    block6.draw(gp)
    block.append(block6)
    block7 = Polygon(Point(245, 280), Point(250, 330), Point(290, 330), Point(285, 280))
    block7.setFill('black')
    block7.draw(gp)
    block.append(block7)
    block8 = Polygon(Point(240, 230), Point(245, 280), Point(285, 280), Point(280, 230))
    block8.setFill('black')
    block8.draw(gp)
    block.append(block8)
    block9 = Polygon(Point(235, 180), Point(240, 230), Point(280, 230), Point(275, 180))
    block9.setFill('black')
    block9.draw(gp)
    block.append(block9)
    block10 = Polygon(Point(200, 230), Point(195, 180), Point(235, 180), Point(240, 230))
    block10.setFill('black')
    block10.draw(gp)
    block.append(block10)
    # pick a random word
    # Open and read words from file
    file = open('words.txt', 'r')
    # Create list of words
    line = file.readlines()
    # Pick a random word
    word = random.choice(line)
    word = word.strip()
    # Close the file
    file.close()
    # Rectangles representing the characters in the secret word
    length = len(word)
    blankList = []
    print(word)
    for x in range(0, (length) * 50, 50):
        if length == 4:
            blank = Rectangle(Point(x + 100, 350), Point(x + 150, 400))
            blank.setFill('gold')
            blank.draw(gp)
            blankList.append(blank)
        elif length == 5:
            blank = Rectangle(Point(x + 80, 350), Point(x + 130, 400))
            blank.setFill('gold')
            blank.draw(gp)
            blankList.append(blank)
        elif length == 6:
            blank = Rectangle(Point(x + 50, 350), Point(x + 100, 400))
            blank.setFill('gold')
            blank.draw(gp)
            blankList.append(blank)
    # Return graphics objects
    return circle, block, word, gp, blankList

from panels import *
from graphics import *


def drop(polygon):
    pass


def new_game(cp, newbox, quitbox, total_score=0):
    newbox_x, newbox_y = (newbox.getP1().getX(), newbox.getP2().getX()), (newbox.getP1().getY(), newbox.getP2().getY())
    quitbox_x, quitbox_y = (quitbox.getP1().getX(), quitbox.getP2().getX()), (quitbox.getP1().getY(), quitbox.getP2().getY())

    circle, block, word, gp, blankList = gamePanel()
    Text(Point(250, 428), total_score).draw(gp)

    attempt = 0
    p_list = ['-'] * len(word)
    score = 10
    while True:  # THE  MEAT
        gp_click = gp.checkMouse()
        cp_click = cp.checkMouse()
        if attempt > 9:
            msg = Text(Point(200, 225), 'YOU LOSE - TRY AGAIN')
            msg.setStyle('bold')
            msg.setSize(18)
            msg.setTextColor('red')
            msg.draw(gp)
            if gp.getMouse():
                gp.close()
            break

        if cp_click: # The Control Panel
            cp_x, cp_y = cp_click.getX(), cp_click.getY()
            print(cp_x, cp_y)
            if newbox_x[0] < cp_x < newbox_x[1] and newbox_y[0] < cp_y < newbox_y[1]:
                gp.close()
                new_game(cp, newbox, quitbox)
                break
            if quitbox_x[0] < cp_x < quitbox_x[1] and quitbox_y[0] < cp_y < quitbox_y[1]:
                gp.close()
                cp.close()
                break

        if gp_click:  # The Game Instance
            gp_x, gp_y = gp_click.getX(), gp_click.getY()
            print(gp_x, gp_y)
            for i in range(len(circle)):
                c_x, c_y = (circle[i].getP1().getX(), circle[i].getP2().getX()), (
                    circle[i].getP1().getY(), circle[i].getP2().getY())
                if c_x[0] < gp_x < c_x[1] and c_y[0] < gp_y < c_y[1]:
                    char_guess = list(string.ascii_uppercase)[i]
                    circle[i].setFill('gold')
                    # drop()  # TODO: add animation
                    print(word)
                    if char_guess in word:
                        for j in range(len(word)):
                            if char_guess == word[j]:
                                p_list[j] = char_guess
                                Text(blankList[j].getCenter(), char_guess).draw(gp)
                    else:
                        score -= 1
                        block[attempt].setFill('white')
                        attempt += 1
                    if ''.join(p_list) == word:
                        msg = Text(Point(200, 225), 'YOU WIN - BOILER UP!\n Click for Next Round')
                        msg.setStyle('bold')
                        msg.setSize(18)
                        msg.setTextColor('gray')
                        msg.draw(gp)

                        total_score += score
                        if gp.getMouse():
                            gp.close()
                            new_game(cp, newbox, quitbox, total_score)


def main():
    newbox, quitbox, cp = controlPanel()
    newbox_x, newbox_y = (newbox.getP1().getX(), newbox.getP2().getX()), (newbox.getP1().getY(), newbox.getP2().getY())
    quitbox_x, quitbox_y = (quitbox.getP1().getX(), quitbox.getP2().getX()), (quitbox.getP1().getY(), quitbox.getP2().getY())

    while True:
        cp_click = cp.checkMouse()
        if cp_click:
            cp_x, cp_y = cp_click.getX(), cp_click.getY()
            # new game
            if newbox_x[0] < cp_x < newbox_x[1] and newbox_y[0] < cp_y < newbox_y[1]:
                new_game(cp, newbox, quitbox)

            # quit
            if quitbox_x[0] < cp_x < quitbox_x[1] and quitbox_y[0] < cp_y < quitbox_y[1]:
                cp.quit()
                break



main()

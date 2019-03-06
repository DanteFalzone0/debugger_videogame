"""
Copyright (C) 2019 Dante Falzone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
                                                 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pygame, sys                               #  _____     _____     _  ____     _        ____             ___________      #
from pygame.locals import *                      # |  __ \   |____ \   | |/ __ \   | |___   /  _ \           |  _________|     #
                                                 # | |  \ \   ____} |  | ' /  \ \  |  ___| |  /_\ |          | |_____          #
fpsClock = pygame.time.Clock()                   # | |   | | / __   |  |  /    | | | |     |  ____|          |  _____|         #
                                                 # | |__/ / | {__}  |  | /     | | |  L_   |  \_/ /          | |            _  #
import random                                    # |_____/   \____/\_\ |_|     |_|  \___|   \____/           |_|           |_| #
import os, re                                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pix(xpos, ypos, r, g, b):  # Set a `pixel' at (x, y) that's actually 64 pixels.
    x = xpos * 8
    y = ypos * 8
    pygame.draw.rect(SURF, (r, g, b), (x, y, 8, 8))


def prize(x, y, r, g, b):  # Create the prize object.
    pygame.draw.rect(SURF, (r, g, b), (x, y, 8, 8))


def horiz(start_x, end_x, y, r, g, b):  # Draw a horizontal line across the screen.
    for x in range (end_x - start_x):
        pix(x, y, r, g, b)
                                                                           #    o o o
                                                                           #  o       o
def bubble(xpos, ypos):  # Background bubbles, because bubbles are fun.    #  o   .   o
    x = xpos // 8                                                          #  o       o
    y = ypos // 8                                                          #    o o o

    pix((x - 2), (y + 1), 10, 50, 12)
    pix((x - 2), (y + 0), 10, 50, 12)
    pix((x - 2), (y - 1), 10, 50, 12)

    pix((x - 1), (y - 2), 10, 50, 12)
    pix((x + 0), (y - 2), 10, 50, 12)
    pix((x + 1), (y - 2), 10, 50, 12)

    pix((x + 2), (y + 1), 10, 50, 12)
    pix((x + 2), (y + 0), 10, 50, 12)
    pix((x + 2), (y - 1), 10, 50, 12)

    pix((x - 1), (y + 2), 10, 50, 12)
    pix((x + 0), (y + 2), 10, 50, 12)
    pix((x + 1), (y + 2), 10, 50, 12)



def beep(freq, time):  # Make a beeping noise.
    os.system('play -n synth %s sin %s' % (time / 1000, freq))


def get_scores():
    scoresheet = open("scores.txt") # High scores are stored here
    scores = scoresheet.read()
    easy = re.search('EASY{(.+)}', scores)
    medi = re.search('MEDI{(.+)}', scores)
    diff = re.search('DIFF{(.+)}', scores)
    impo = re.search('IMPO{(.+)}', scores)
    easynum = int(easy.group(1), 2)  # Argument `, 2' tells the program to interpret as base-2, since scores are stored in binary
    medinum = int(medi.group(1), 2)
    diffnum = int(diff.group(1), 2)
    imponum = int(impo.group(1), 2)
    easyhigh[0] = easynum
    mediumhigh[0] = medinum
    hardhigh[0] = diffnum
    imposhigh[0] = imponum


def collect_stats(sgroup):
    statsheet = open("gamestats.txt")  # Statistics on the game's usage are stored here
    stats = statsheet.read()
    easy = re.search('Number of easy games: (.+)', stats)
    medi = re.search('Number of medium games: (.+)', stats)
    diff = re.search('Number of hard games: (.+)', stats)
    impo = re.search('Number of impossible games: (.+)', stats)
    easynum = int(easy.group(1))
    medinum = int(medi.group(1))
    diffnum = int(diff.group(1))
    imponum = int(impo.group(1))


    def update_impo():
        newnum = imponum + 1
        newstats = open("gamestats.txt", "w+")
        newstats.write("Number of easy games: " + str(easynum) + "\n" +
                       "Number of medium games: " + str(medinum) +"\n" +
                       "Number of hard games: " + str(diffnum) + "\n" +
                       "Number of impossible games: " + str(newnum))


    def update_diff():
        newnum = diffnum + 1
        newstats = open("gamestats.txt", "w+")
        newstats.write("Number of easy games: " + str(easynum) + "\n" +
                       "Number of medium games: " + str(medinum) +"\n" +
                       "Number of hard games: " + str(newnum) + "\n" +
                       "Number of impossible games: " + str(imponum))


    def update_medi():
        newnum = medinum + 1
        newstats = open("gamestats.txt", "w+")
        newstats.write("Number of easy games: " + str(easynum) + "\n" +
                       "Number of medium games: " + str(newnum) +"\n" +
                       "Number of hard games: " + str(diffnum) + "\n" +
                       "Number of impossible games: " + str(imponum))


    def update_easy():
        newnum = easynum + 1
        newstats = open("gamestats.txt", "w+")
        newstats.write("Number of easy games: " + str(newnum) + "\n" +
                       "Number of medium games: " + str(medinum) +"\n" +
                       "Number of hard games: " + str(diffnum) + "\n" +
                       "Number of impossible games: " + str(imponum))


    if sgroup == "impossible":
        update_impo()
    if sgroup == "difficult":
        update_diff()
    if sgroup == "medium":
        update_medi()
    if sgroup == "easy":
        update_easy()


def update_scores_easy():  # Function to update the highscore for the `easy' difficulty level
    scoresheet = open("scores.txt", "w+")  # Argument `+w' necessary to overwrite the contents of the file
    scoresheet.write("EASY{" + str("{0:08b}".format(score[0])) +  # Converts the decimal ints to binary
                     "}\nMEDI{" + str("{0:08b}".format(mediumhigh[0])) +
                     "}\nDIFF{" + str("{0:08b}".format(hardhigh[0])) +
                     "}\nIMPO{" + str("{0:08b}".format(imposhigh[0])) + "}")


def update_scores_medium():  # Function to update the highscore for the `medium' difficulty level
    scoresheet = open("scores.txt", "w+")
    scoresheet.write("EASY{" + str("{0:08b}".format(easyhigh[0])) +
                     "}\nMEDI{" + str("{0:08b}".format(score[0])) +
                     "}\nDIFF{" + str("{0:08b}".format(hardhigh[0])) +
                     "}\nIMPO{" + str("{0:08b}".format(imposhigh[0])) + "}")


def update_scores_hard():  # Function to update the highscore for the `difficult' difficulty level
    scoresheet = open("scores.txt", "w+")
    scoresheet.write("EASY{" + str("{0:08b}".format(easyhigh[0])) +
                     "}\nMEDI{" + str("{0:08b}".format(mediumhigh[0])) +
                     "}\nDIFF{" + str("{0:08b}".format(score[0])) +
                     "}\nIMPO{" + str("{0:08b}".format(imposhigh[0])) + "}")


def update_scores_impossible():  # Function to update the highscore for the `impossible' difficulty level
    scoresheet = open("scores.txt", "w+")
    scoresheet.write("EASY{" + str("{0:08b}".format(easyhigh[0])) +
                     "}\nMEDI{" + str("{0:08b}".format(mediumhigh[0])) +
                     "}\nDIFF{" + str("{0:08b}".format(hardhigh[0])) +
                     "}\nIMPO{" + str("{0:08b}".format(score[0])) + "}")


titlebool = [1]  # Tells which screen to display; 4 for death, 3 for scoreboard,
                 # 2 for difficulty selection, 1 for title scrren, 0 for game.

SURF = pygame.display.set_mode((648, 400))  # Set the surface (here I used the Golden Ratio)

titlescreen = pygame.image.load('title')  # Due to having jacked up my png when I tried to make this in Pinta,
def avatar():                             # I made my graphics using the following website: http://pixelartmaker.com/
    if cycle == 0 or cycle == 1:
        avatar = pygame.image.load('frame0')
    if cycle == 2 or cycle ==3:
        avatar = pygame.image.load('frame1')
    if cycle == 4 or cycle == 5:
        avatar = pygame.image.load('frame2')
    return avatar


def xavatar():
    if cycle == 1 or cycle == 2:
        xavatar = pygame.image.load('xframe0')
    if cycle == 3 or cycle == 4:
        xavatar = pygame.image.load('xframe1')
    if cycle == 5 or cycle == 0:
        xavatar = pygame.image.load('xframe2')
    return xavatar


difficulty = 1000000000 # Higher num = lower difficulty; must start absurdly high so as to minimize chance of score error bugs on start

pygame.font.init()
myfont = pygame.font.SysFont("$HACKERMAN", 36)  # Initialize the font (dependency: $HACKERMAN font; available as FOSS on FontStruct)
smallerfont = pygame.font.SysFont("$HACKERMAN", 24)


titlex = 20
titley = 100

cycle = 0

avatarx = 300  # Coordinates where the player's avatar starts.
avatary = 100

avatar_speed = 7  # Amount that the avatar's position can change per screen refresh while player is moving.

xavatarx = -40  # Coordinates where the enemy starts. It is placed so as to be impossible to spawn where the player is.
xavatary = -40

score = [0]

prizex = 400
prizey = 20

easyhigh = [0]  # High scores
mediumhigh = [0]
hardhigh = [0]
imposhigh = [0]
get_scores()


bubble0x = 0
bubble0y = 30

bubble1x = 470
bubble1y = 100

bubble2x = 250
bubble2y = 270

overall_time = 0  # Amount of time that has passed since the beginning of the game.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()  # Callback for ingame keypresses

    pygame.display.set_caption('DEBUGGER by Dante Falzone')

    SURF.fill((0, 0, 0))


    if score[0] >= 256:
        print('\x1b[0;31;40m' + 'Buffer Overflow Error: value too large to store in unsigned byte' + '\x1b[0m')
        break


    if titlebool[0] == 3:
        get_scores()
        header = myfont.render("HIGHSCORES", 3, (255, 255, 255))
        easyscore =   "Easy       |  " + str(easyhigh[0])
        mediumscore = "Medium     |  " + str(mediumhigh[0])
        hardscore =   "Difficult  |  " + str(hardhigh[0])
        imposscore =  "Impossible |  " + str(imposhigh[0])
        SURF.blit(header, (20, 20))
        easy = myfont.render(easyscore, 3, (255, 255, 255))
        medium = myfont.render(mediumscore, 3, (255, 255, 255))
        hard = myfont.render(hardscore, 3, (255, 255, 255))
        impossible = myfont.render(imposscore, 3, (255, 255, 255))
        SURF.blit(easy, (20, 100))
        SURF.blit(medium, (20, 140))
        SURF.blit(hard, (20, 180))
        SURF.blit(impossible, (20, 220))
        goback = myfont.render("Press H to continue, Q to quit to title", 3, (0, 255, 80))
        SURF.blit(goback, (20, 300))
        if keys[K_h]:
            titlebool[0] = 0  # Go back to the game
        if keys[K_q]:
            avatarx = 300
            avatary = 100
            overall_time = 0
            score[0] = 0
            difficulty = 1000000000  # Again, it is necessary to set the difficulty var very high to minimize the chance of score bugs
            titlebool[0] = 1         # happening while in title screen.

    putprizenum = random.randint(0, difficulty)  # 1 in x chance of the prize moving each frame, where x is the difficulty var.
    if putprizenum == difficulty and titlebool[0] == 0:
        prizex = random.randint(0, 600)
        prizey = random.randint(0, 300)

    if difficulty == 256:
        if int(round(prizex)) in range (int(round(avatarx)), int(round(avatarx + 75))):
            if int(round(prizey)) in range (int(round(avatary)), int(round(avatary + 75))):
                score[0] += 1              # This block detects if the avatar collides with the prize. If it does, it updates
                get_scores()               # the score and teleports the prize to a random location on the screen, then makes
                if score[0] > easyhigh[0]: # a beep to indicate a score change.
                    update_scores_easy()
                prizex = random.randint(0, 600)
                prizey = random.randint(0, 300)
                beep(800, 110)


    if difficulty == 64:
        if int(round(prizex)) in range (int(round(avatarx)), int(round(avatarx + 75))):
            if int(round(prizey)) in range (int(round(avatary)), int(round(avatary + 75))):
                score[0] += 1
                get_scores()
                if score[0] > mediumhigh[0]:
                    update_scores_medium()
                prizex = random.randint(0, 600)
                prizey = random.randint(0, 300)
                beep(800, 110)


    if difficulty == 16:
        if int(round(prizex)) in range (int(round(avatarx)), int(round(avatarx + 75))):
            if int(round(prizey)) in range (int(round(avatary)), int(round(avatary + 75))):
                score[0] += 1
                get_scores()
                if score[0] > hardhigh[0]:
                    update_scores_hard()
                prizex = random.randint(0, 600)
                prizey = random.randint(0, 300)
                beep(800, 110)


    if difficulty == 4:
        if int(round(prizex)) in range (int(round(avatarx - 5)), int(round(avatarx + 80))):
            if int(round(prizey)) in range (int(round(avatary - 5)), int(round(avatary + 80))):
                prizex = random.randint(0, 600)
                prizey = random.randint(0, 300)
        if int(round(prizex)) in range (int(round(avatarx)), int(round(avatarx + 75))):
            if int(round(prizey)) in range (int(round(avatary)), int(round(avatary + 75))):
                score[0] += 1
                get_scores()
                if score[0] > imposhigh[0]:
                    update_scores_impossible()
                prizex = random.randint(0, 600)
                prizey = random.randint(0, 300)
                beep(800, 110)


    if titlebool[0] == 4: # Death screen
        death_image = pygame.image.load('Death_screen')
        SURF.blit(death_image, (70, 70))
        score_string = "Score: " + str(score[0])
        label = myfont.render(score_string, 2, (255, 5, 0))
        SURF.blit(label, (210, 215))
        avatarx = 300
        avatary = 100
        if keys[K_w]:
            titlebool[0] = 1
            score[0] = 0
            overall_time = 0


    if titlebool[0] == 2:  # Screen for selecting difficulty level
        x = 0
        y = 0
        z = 0
        if cycle == 0:
            x = 255
            y = 25
            z = 25
        if cycle == 1:
            x = 255
            y = 150
            z = 0
        if cycle == 2:
            x = 255
            y = 255
            z = 0
        if cycle == 3:
            x = 0
            y = 255
            z = 25
        if cycle == 4:
            x = 0
            y = 150
            z = 255
        if cycle == 5:
            x = 150
            y = 0
            z = 200
        label0 = myfont.render("CHOOSE YOUR DIFFICULTY LEVEL BY", 3, (255, 255, 255))
        label1 = myfont.render("PRESSING THE CORRESPONDING NUMBER KEY:", 3, (255, 255, 255))
        SURF.blit(label0, (30, 20))
        SURF.blit(label1, (30, 60))
        choice0 = myfont.render("[1] easy-peasy", 3, (20, 20, 255))
        choice1 = myfont.render("[2] medium", 3, (255, 255, 20))
        choice2 = myfont.render("[3] difficult", 3, (255, 5, 0))
        choice3 = myfont.render("[4] impossible", 3, (x, y, z))
        SURF.blit(choice0, (30, 100))
        SURF.blit(choice1, (30, 140))
        SURF.blit(choice2, (30, 180))
        SURF.blit(choice3, (30, 220))
        if keys[K_1]:
            collect_stats("easy")
            difficulty = 256
            titlebool[0] = 0
        if keys[K_2]:
            collect_stats("medium")
            difficulty = 64
            titlebool[0] = 0
        if keys[K_3]:
            collect_stats("difficult")
            difficulty = 16
            titlebool[0] = 0
        if keys[K_4]:
            collect_stats("impossible")
            difficulty = 4
            titlebool[0] = 0

    if titlebool[0] == 1:
        SURF.blit(titlescreen, (titlex, titley))
        label = myfont.render("DEBUGGER: TRY TO CATCH THE BUG", 24, (255, 5, 0))
        if cycle == 0 or cycle == 1 or cycle ==2 or cycle ==3 or cycle ==4:
            SURF.blit(label, (90, 20))
        if keys[K_x]:
            titlebool[0] = 2


    if titlebool[0] == 0:
        overall_time += 1

        bubble(bubble0x, bubble0y)
        bubble(bubble1x, bubble1y)
        bubble(bubble2x, bubble2y)

        if overall_time == 299:
            xavatarx = -40
            xavatary = -40

        if overall_time >= 300:  # If the game has been going on for over 15 seconds
            SURF.blit(xavatar(), (xavatarx, xavatary))  # Draws the enemy.
            xavatarx = (((difficulty - 1) * xavatarx) + (avatarx + 0)) / difficulty  # Enemy chases you at a speed derived from difficulty.
            xavatary = (((difficulty - 1) * xavatary) + (avatary + 0)) / difficulty

        if int(round(avatarx + 37)) in range (int(round(xavatarx - 30)), int(round(xavatarx + 95))):
            if int(round(avatary + 37)) in range (int(round(xavatary - 30)), int(round(xavatary + 90))):
                beep(612, 90)
                beep(600, 90)
                beep(568, 800)
                titlebool[0] = 4
                xavatarx = -40
                xavatary = -40


        SURF.blit(avatar(), (avatarx, avatary))  # Draws the avatar as the bottommost layer.

        if cycle == 0 or cycle == 1 or cycle == 2:  # This block draws and animates the prize in time with the cycle clock.
            prize(prizex, prizey, 255, 5, 0)
        if cycle == 3 or cycle == 4 or cycle ==5:
            prize((prizex - 8), prizey, 255, 5, 0)
            prize((prizex + 8), prizey, 255, 5, 0)
            prize(prizex, (prizey - 8), 255, 5, 0)
            prize(prizex, (prizey + 8), 255, 5, 0)

        horiz(0, 100, 40, 255, 0, 0)  # Draws the score bar on top of whatever comes before this block.
        horiz(0, 100, 41, 0, 0, 0)
        horiz(0, 100, 42, 10, 10, 10)
        horiz(0, 100, 43, 0, 0, 0)
        horiz(0, 100, 44, 10, 10, 10)
        horiz(0, 100, 45, 0, 0, 0)
        horiz(0, 100, 46, 10, 10, 10)
        horiz(0, 100, 47, 0, 0, 0)
        horiz(0, 100, 48, 10, 10, 10)
        horiz(0, 100, 49, 0, 0, 0)
        horiz(0, 100, 50, 10, 10, 10)

        score_string = "Score: " + str(score[0]) + " | Arrow keys to move, X to pause & see highscores"
        label = smallerfont.render(score_string, 2, (0, 255, 80))
        SURF.blit(label, (6, 348))

        if keys[K_x]:
            titlebool[0] = 3


    if keys[K_LEFT]:
        avatarx -= avatar_speed
    if keys[K_RIGHT]:
        avatarx += avatar_speed
    if keys[K_UP]:
        avatary -= avatar_speed
    if keys[K_DOWN]:
        avatary += avatar_speed

    if avatarx >= 668:  # Send the avatar to the other side of the screen if it crosses the edge.
        avatarx = -59
    if avatarx <= -60:
        avatarx = 667
    if avatary >= 400:
        avatary = -59
    if avatary <= -60:
        avatary = 399

    if cycle == 5:
        cycle = 0
    if cycle < 5:
        cycle += 1

    bubble0x += 1
    bubble1x += 1
    bubble2x += 1

    if bubble0x >= 668:
        bubble0x = -60
        bubble0y = random.randint(30, 350)

    if bubble1x >= 668:
        bubble1x = -60
        bubble1y = random.randint(30, 350)

    if bubble2x >= 668:
        bubble2x = -60
        bubble2y = random.randint(30, 350)

    pygame.display.update()
    fpsClock.tick(20)

import pygame
import random
import math

pygame.init()

clock = pygame.time.Clock()

length = 700
height = 700
screen = pygame.display.set_mode((height, length))

WHITE = (255, 255, 255)
lives = 5

player = pygame.image.load("character.png")
player = pygame.transform.scale(player, (20, 20))
roundcount = 0
recursion = 0
otherrecursion = 0

circles = pygame.image.load("hitcircle.png")
circles = pygame.transform.scale(circles, (20, 20))

background = pygame.image.load("background.jpeg").convert()
background = pygame.transform.scale(background, (700, 700))

heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (50 , 50))
my_font = pygame.font.SysFont("Comic Sans MS", 20)
circlevel = 5
randlist1 = []

max = 500
for i in range(max):
    randlist1.append([random.randrange(0, 700, random.randint(1, 30)), -10])

randlistx = []
randlisty = []
randlistx1 = []
randlisty1 = []

for i in range(0, 700, 50):
    randlistx.append([i, 0])
    randlisty.append([0, i])
    randlistx1.append([i, 700])
    randlisty1.append([700, i])

randlistdiag1 = []
randlistdiag2 = []

for i in range(0, 700, 50):
    randlistdiag1.append([i + 700, i - 700])
    randlistdiag2.append([-i, i - 700])

triangle = []
triangle1 = []

for i in range(0, 700, 50):
    triangle.append([i, -abs(2 * i - 700)])
    triangle1.append([i, abs(2 * i - 700) + 700])

playerx = 350
playery = 450
wave = 1
theclock = 0
count = 0
iterations = 0
theiteration = False
thesecondclock = 61
ishit = False
thethirdclock = 0


def game_over(win):
    global randlist1
    global randlistx
    global randlisty
    global randlistx1
    global randlisty1
    global randlistdiag1
    global randlistdiag2
    global triangle
    global triangle1
    global lives
    global thesecondclock
    global count
    global wave
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    randlist1 = []

                    max = 500
                    for i in range(max):
                        randlist1.append([random.randrange(0, 700, random.randint(1, 30)), 0])

                    randlistx = []
                    randlisty = []
                    randlistx1 = []
                    randlisty1 = []

                    for i in range(0, 700, 50):
                        randlistx.append([i, 0])
                        randlisty.append([0, i])
                        randlistx1.append([i, 700])
                        randlisty1.append([700, i])

                    randlistdiag1 = []
                    randlistdiag2 = []

                    for i in range(0, 700, 50):
                        randlistdiag1.append([i + 700, i - 700])
                        randlistdiag2.append([-i, i - 700])

                    triangle = []
                    triangle1 = []

                    for i in range(0, 700, 50):
                        triangle.append([i, -abs(2 * i - 700)])
                        triangle1.append([i, abs(2 * i - 700) + 700])

                    lives = 3
                    thesecondclock = 61
                    count = 0
                    wave = 1
                    main_menu()
        if win:
            rendersurface = my_font.render("You win! Click space to restart", False, (0, 0, 0))
            screen.fill((215, 94, 242))
        else:
            rendersurface = my_font.render("Game over! Click space to restart", False, (0, 0, 0))
            screen.fill((227, 91, 82))

        screen.blit(rendersurface, (200, 350))
        pygame.display.flip()
    pygame.quit()

def main_menu():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                main()

        rendersurface = my_font.render("Click any key to start", False, (0, 0, 0))
        screen.fill((52, 140, 235))

        screen.blit(rendersurface, (250, 350))
        pygame.display.flip()
    pygame.quit()

def level_cleared():
    running = True
    while running:
        global count
        global wave
        global theclock

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count = 0
                    wave += 1
                    theclock = 0
                    gamereset()
        rendersurface = my_font.render("Round cleared! Press space to continue", False, (0, 0, 0))
        screen.fill((255, 255, 255))

        screen.blit(rendersurface, (150, 350))
        pygame.display.flip()
    pygame.quit()


def final_round():
    global playerx, ishit, thesecondclock, theiteration, thethirdclock
    global playery
    global theclock
    global recursion
    global randlistx
    global randlisty
    global randlistx1
    global randlisty1
    global lives
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if playery < 0:
                playery = 0
            else:
                playery -= 3

        if keys[pygame.K_DOWN]:
            if playery > 680:
                playery = 680
            else:
                playery += 3

        if keys[pygame.K_LEFT]:
            if playerx < 0:
                playerx = 0
            else:
                playerx -= 3

        if keys[pygame.K_RIGHT]:
            if playerx > 680:
                playerx = 680
            else:
                playerx += 3


        if 8000 < theclock < 10000:
            while recursion == 0:
                recursion = 1
                randlistx = []
                randlisty = []
                randlistx1 = []
                randlisty1 = []

                for i in range(0, 700, 50):
                    randlistx.append([i, 0])
                    randlisty.append([0, i])
                    randlistx1.append([i, 700])
                    randlisty1.append([700, i])
                main()

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        for i in range(0, lives):
            screen.blit(heart, (i * 50, 0))

        if lives == 0:
            game_over(False)

        if theiteration and 60 < thesecondclock:
            lives -= 1
            thesecondclock = 0
            ishit = True
            thethirdclock = 0
            theiteration = False

        if ishit:
            thesecondclock += 1
            thethirdclock += 1
            if 0 < thethirdclock < 5 or 10 < thethirdclock < 15 or 20 < thethirdclock < 25 or 30 < thethirdclock < 35 or 40 < thethirdclock < 45 or 50 < thethirdclock < 55 or 60 < thethirdclock < 65:
                screen.blit(player, [-100, -100])
            else:
                screen.blit(player, [playerx, playery])
        else:
            screen.blit(player, [playerx, playery])
        if theclock > 3500:
            for i in range(len(randlistx)):
                randlistx[i][1] += circlevel
                randlisty[i][0] += circlevel
                randlistx1[i][1] -= circlevel
                randlisty1[i][0] -= circlevel
                screen.blit(circles, randlistx[i])
                screen.blit(circles, randlisty[i])
                screen.blit(circles, randlistx1[i])
                screen.blit(circles, randlisty1[i])
                hitone = math.sqrt((abs((randlisty[i][1] - playery) ** 2 + (randlisty[i][0] - playerx) ** 2)))
                hittwo = math.sqrt((abs((randlistx[i][1] - playery) ** 2 + (randlistx[i][0] - playerx) ** 2)))
                hitthree = math.sqrt((abs((randlistx1[i][1] - playery) ** 2 + (randlistx1[i][0] - playerx) ** 2)))
                hitfour = math.sqrt((abs((randlisty1[i][1] - playery) ** 2 + (randlisty1[i][0] - playerx) ** 2)))
                if hitone <= 5 or hittwo <= 5 or hitthree <= 5 or hitfour <= 5:
                    if thesecondclock > 60:
                        theiteration = True
        pygame.display.flip()
        theclock += clock.tick(60)
    pygame.quit()


def final_round2():
    global playerx, thesecondclock, thethirdclock, theiteration, ishit
    global playery
    global theclock
    global recursion
    global randlistdiag1
    global randlistdiag2
    global lives
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if playery < 0:
                playery = 0
            else:
                playery -= 3

        if keys[pygame.K_DOWN]:
            if playery > 680:
                playery = 680
            else:
                playery += 3

        if keys[pygame.K_LEFT]:
            if playerx < 0:
                playerx = 0
            else:
                playerx -= 3

        if keys[pygame.K_RIGHT]:
            if playerx > 680:
                playerx = 680
            else:
                playerx += 3

        if 8000 < theclock < 10000:
            while recursion == 0:
                recursion = 1
                randlistdiag1 = []
                randlistdiag2 = []

                for i in range(0, 700, 50):
                    randlistdiag1.append([i + 700, i - 700])
                    randlistdiag2.append([-i, i - 700])
                main()

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        if lives <= 0:
            game_over(False)

        if theiteration and 60 < thesecondclock:
            lives -= 1
            thesecondclock = 0
            ishit = True
            thethirdclock = 0
            theiteration = False

        if ishit:
            thesecondclock += 1
            thethirdclock += 1
            if 0 < thethirdclock < 5 or 10 < thethirdclock < 15 or 20 < thethirdclock < 25 or 30 < thethirdclock < 35 or 40 < thethirdclock < 45 or 50 < thethirdclock < 55 or 60 < thethirdclock < 65:
                screen.blit(player, [-100, -100])
            else:
                screen.blit(player, [playerx, playery])
        else:
            screen.blit(player, [playerx, playery])

        for i in range(0, lives):
            screen.blit(heart, (i * 50, 0))

        if theclock > 3500:
            for i in range(len(randlistdiag1)):
                randlistdiag1[i][0] -= circlevel
                randlistdiag2[i][0] += circlevel
                randlistdiag1[i][1] += circlevel
                randlistdiag2[i][1] += circlevel
                screen.blit(circles, randlistdiag1[i])
                screen.blit(circles, randlistdiag2[i])
                if math.sqrt((abs((randlistdiag1[i][1] - playery) ** 2 + (randlistdiag1[i][0] - playerx) ** 2)))<= 10:
                    if thesecondclock > 60:
                        theiteration = True
                if math.sqrt((abs((randlistdiag2[i][1] - playery) ** 2 + (randlistdiag2[i][0] - playerx) ** 2))) <= 10:
                    if thesecondclock > 60:
                        theiteration = True

        theclock += clock.tick(60)
        pygame.display.flip()
    pygame.quit()


def final_round3():
    global playerx, theiteration, thesecondclock, ishit, thethirdclock
    global playery
    global theclock
    global recursion
    global triangle
    global lives
    global triangle1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if playery < 0:
                playery = 0
            else:
                playery -= 3

        if keys[pygame.K_DOWN]:
            if playery > 680:
                playery = 680
            else:
                playery += 3

        if keys[pygame.K_LEFT]:
            if playerx < 0:
                playerx = 0
            else:
                playerx -= 3

        if keys[pygame.K_RIGHT]:
            if playerx > 680:
                playerx = 680
            else:
                playerx += 3

        if lives <= 0:
            game_over(False)

        if theiteration and 60 < thesecondclock:
            lives -= 1
            thesecondclock = 0
            ishit = True
            thethirdclock = 0
            theiteration = False

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        if ishit:
            thesecondclock += 1
            thethirdclock += 1
            if 0 < thethirdclock < 5 or 10 < thethirdclock < 15 or 20 < thethirdclock < 25 or 30 < thethirdclock < 35 or 40 < thethirdclock < 45 or 50 < thethirdclock < 55 or 60 < thethirdclock < 65:
                screen.blit(player, [-100, -100])
            else:
                screen.blit(player, [playerx, playery])
        else:
            screen.blit(player, [playerx, playery])
        if 8000 < theclock < 10000:
            while recursion == 0:
                recursion += 1
                recursion = 1
                triangle = []
                triangle1 = []
                for i in range(0, 700, 50):
                    triangle.append([i, -abs(2 * i - 700)])
                    triangle1.append([i, abs(2 * i - 700) + 700])
                main()

        for i in range(0, lives):
            screen.blit(heart, (i * 50, 0))

        if theclock > 3500:
            for i in range(len(triangle)):
                triangle[i][1] += 10
                triangle1[i][1] -= 10
                screen.blit(circles, triangle[i])
                screen.blit(circles, triangle1[i])
                if math.sqrt((abs((triangle[i][1] - playery) ** 2 + (triangle[i][0] - playerx) ** 2))) <= 10:
                    if thesecondclock > 60:
                        theiteration = True
                if math.sqrt((abs((triangle1[i][1] - playery) ** 2 + (triangle1[i][0] - playerx) ** 2))) <= 10:
                    if thesecondclock > 60:
                        theiteration = True
        pygame.display.flip()
        theclock += clock.tick(60)
    pygame.quit()

def gamereset():
    global iterations
    for i in range(0, max):
        randlist1[i][1] = 0
    iterations += 1

    pygame.display.flip()
    main()


def main():
    global recursion
    global otherrecursion
    global playerx
    global playery
    global wave
    global theclock
    global count
    global iterations
    global roundcount
    global lives
    global theiteration
    global thesecondclock
    global ishit
    global thethirdclock
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if playery < 0:
                playery = 0
            else:
                playery -= 3

        if keys[pygame.K_DOWN]:
            if playery > 680:
                playery = 680
            else:
                playery += 3

        if keys[pygame.K_LEFT]:
            if playerx < 0:
                playerx = 0
            else:
                playerx -= 3

        if keys[pygame.K_RIGHT]:
            if playerx > 680:
                playerx = 680
            else:
                playerx += 3

        if theclock % 2 == 0:
            count += 1

        if lives <= 0:
            game_over(False)

        if theiteration and 60 < thesecondclock:
            lives -= 1
            thesecondclock = 0
            thethirdclock = 0
            ishit = True
            theiteration = False

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        for i in range(0, lives):
            screen.blit(heart, (i * 50, 0))

        if ishit:
            thesecondclock += 1
            thethirdclock += 1
            if 0 < thethirdclock < 5 or 10 < thethirdclock < 15 or 20 < thethirdclock < 25 or 30 < thethirdclock < 35 or 40 < thethirdclock < 45 or 50 < thethirdclock < 55 or 60 < thethirdclock < 65:
                screen.blit(player, [-100, -100])
            else:
                screen.blit(player,[playerx, playery])
        else:
            screen.blit(player,[playerx, playery])

        if count < max and wave < 4:
            for i in range(0, count):
                randlist1[i][1] += wave * 1.5
                screen.blit(circles, randlist1[i])

                if math.sqrt((abs((randlist1[i][1] - playery) ** 2 + (randlist1[i][0] - playerx) ** 2))) <= 10:
                    if thesecondclock > 60:
                        theiteration = True

        elif wave == 4:
            if roundcount < 5:
                roundcount += 1
                recursion = 0
                theclock = 0
                seed = random.randint(1, 3)
                if seed == 1:
                    final_round()
                elif seed == 2:
                    final_round2()
                elif seed == 3:
                    final_round3()
            else:
                game_over(True)
        elif wave < 4:
            level_cleared()

        pygame.display.update()
        theclock += clock.tick(60)
    pygame.quit()

main_menu()

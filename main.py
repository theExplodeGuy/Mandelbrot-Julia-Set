from pygame.locals import *
import pygame

scale = 100
iterations = 50
pygame.init()

size = width, height = 400, 400
screen = pygame.display.set_mode(size)
xaxis = width / 2
yaxis = height / 2
screen.fill((255, 255, 255))


def mandelbrot(zoom):
    for iy in range(height):
        for ix in range(width):

            z = 0 + 0j
            c = complex(float(ix - xaxis) / (scale * zoom), float(iy - yaxis) / (scale * zoom))

            for i in range(iterations):
                z = z ** 2 + c
                if abs(z) > 2:
                    v = (1000 * i) / iterations
                    if v > 510:
                        color = (255, 255, v % 255)
                    elif v > 255:
                        color = (255, v % 255, 0)
                    else:
                        color = (v % 255, 0, 0)
                    break
                else:
                    color = (0, 0, 0)

            screen.set_at((ix, iy), color)


def julia(zoom):
    for iy in range(int(height)):
        for ix in range(int(width)):

            c = complex(-0.8, 0.156)
            z = complex(float(ix - xaxis) / (scale * zoom), float(iy - yaxis) / (scale * zoom))

            for i in range(iterations):
                z = z ** 2 + c
                if abs(z) > 2:
                    v = (1000 * i) / iterations
                    if v > 510:
                        color = (255, 255, v % 255)
                    elif v > 255:
                        color = (255, v % 255, 0)
                    else:
                        color = (v % 255, 0, 0)
                    break
                else:
                    color = (0, 0, 0)

            screen.set_at((ix, iy), color)


def main():
    zoom = 1
    j = True
    julia(zoom)
    pygame.display.update()

    while True:
        global xaxis, yaxis, height, width, scale
        event = pygame.event.poll()

        if (event.type == QUIT or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
            break
        if event.type == KEYDOWN and event.key == K_j:
            j = True
            julia(zoom)
            pygame.display.update()
        if event.type == KEYDOWN and event.key == K_m:
            j = False
            mandelbrot(zoom)
            pygame.display.update()
        if event.type == KEYDOWN and event.key == K_1:
            zoom *= 1.2
        if event.type == KEYDOWN and event.key == K_2:
            zoom *= 0.8
        if event.type == pygame.MOUSEBUTTONUP:
            oldzoom = zoom
            pos = pygame.mouse.get_pos()
            posx = pos[0]
            posy = pos[1]
            # translates function so that the point where the user clicked
            # is in the center of the viewport
            xaxis = (xaxis + (posx - width / 2) / 5)
            yaxis = (yaxis + (posy - height / 2) / 5)

            xaxis = (zoom * (posx / width + xaxis) / oldzoom - posx / width)
            yaxis = (zoom * (posy / height + yaxis) / oldzoom - posy / height)

            if j:
                julia(zoom)
                pygame.display.update()
            else:
                mandelbrot(zoom)
                pygame.display.update()


if __name__ == "__main__":
    main()

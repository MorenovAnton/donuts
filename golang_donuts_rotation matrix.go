package main

func main() {
	var (
		WIDTH                      int = 1920
		HEIGHT                     int = 1080
		x_start, y_start               = 0, 0
		x_separator, y_separator       = 10, 20
		rows                       int = HEIGHT / y_separator
		columns                    int = WIDTH / x_separator
		screen_size                int = rows * columns
		A, B                           = 0, 0
		theta_spacing, phi_spacing     = 10, 1
		x_offset, y_offset             = columns / 2, rows / 2
		A, B                           = 0, 0
		theta_spacing, phi_spacing     = 10, 1
		chars                          = ".,-~:;=!*#$@"
	)

}

/*
import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0








screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

# def text_display(letter, x_start, y_start):
#     text = font.render(str(letter), True, white)
#     display_surface.blit(text, (x_start, y_start))


run = True
while run:

    screen.fill((black))

    z = [0] * screen_size  # Donut. Fills donut space
    b = [' '] * screen_size  # Background. Fills empty space

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00004  # for faster rotation change to bigger value
        B += 0.00002  # for faster rotation change to bigger value
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator


    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
*/

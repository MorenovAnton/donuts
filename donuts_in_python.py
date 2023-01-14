import pygame
import math
import colorsys

# pygame.init() is used to initialize the Pygame library.
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0
# WIDTH and HEIGHT are used to set the size of the screen.
WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0
# x_separator and y_separator are used to set the space between each character in the donut.
x_separator = 10
y_separator = 20
# rows and columns are used to calculate the total number of characters that will be used to display the donut.
rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns
# x_offset and y_offset are used to center the donut on the screen.
x_offset = columns / 2
y_offset = rows / 2
# A and B are used to control the rotation of the donut.
A, B = 0, 0  # rotating animation

# theta_spacing and phi_spacing are used to control the resolution of the donut.
theta_spacing = 10
# for faster rotation change to 2, 3 or more, but first change 86, 87 lines as commented
phi_spacing = 1
# chars is a string of characters that will be used to display the donut.
chars = ".,-~:;=!*#$@"  # luminance index
# screen is used to create the screen on which the donut will be displayed.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# display_surface is used to create the surface on which the donut will be displayed.
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# used to set the title of the window that is created by the Pygame library
pygame.display.set_caption('Donut')
# is used to create a font object that can be used to render text in Pygame. The pygame.The first argument passed to the function
# is the font name. In this case, it is 'Arial'. The second argument is the font size, in this case, it's 18. The third
# argument is the font style, in this case, it's 'bold'.
font = pygame.font.SysFont('Arial', 18, bold=True)

def hsv2rgb(h, s, v):
    # hsv2rgb function to color the characters of the donut.
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    # text_display function is used to display the characters of the donut on the screen.
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

# def text_display(letter, x_start, y_start):
#     text = font.render(str(letter), True, white)
#     display_surface.blit(text, (x_start, y_start))


run = True
while run:
    # screen.fill((black)) is used to fill the entire screen with the color black.
    screen.fill((black))
    # z = [0] * screen_size creates a list of zeroes with a length of screen_size.
    # b = [' '] * screen_size creates a list of empty spaces with a length of screen_size.
    # z list is used to fill the donut space, and b list is used to fill the empty space.
    # The z list is used to keep track of the depth of each pixel of the donut.
    # The b list is used to store the characters that will be used to display the donut on the screen.
    # These lists are used later on in the program to calculate the positions of the characters on the screen, creating the
    # illusion of a 3D rotating donut.
    z = [0] * screen_size  # Donut. Fills donut space
    b = [' '] * screen_size  # Background. Fills empty space

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            # i, j, A, B are the variables that are used to control the rotation of the donut.
            # The trigonometric functions are used to calculate the positions of the characters on the screen, creating the illusion of a 3D rotating donut.
            # These values are used to calculate the x, y and z coordinates of each character on the screen.
            # By using trigonometric functions we can calculate the positions of the characters on the screen based on the rotation of the donut.
            # Эта часть нужна для подсчета глубины
            d = math.cos(j)
            c = math.sin(i)
            h = d + 2
            e = math.sin(A)

            f = math.sin(j)
            g = math.cos(A)
            # This formula is used to calculate the depth of each character on the screen. The depth of a character is determined by its position
            # in the 3D space, a character that is farther away from the screen will have a greater depth value.
            # The formula calculates the depth of each character by dividing 1 by the value of (c * h * e + f * g + 5).
            # c * h * e is used to control the rotation of the donut on the y-axis.
            # f * g is used to control the rotation of the donut on the x-axis.
            # 5 is a constant value that is added to the equation, it is used to adjust the overall depth of the donut.
            # By using this formula, the program can calculate the depth of each character on the screen, creating the illusion of a 3D rotating donut.
            D = 1 / (c * h * e + f * g + 5)
            # The variables l, m, n, and t are used in the calculation of the 3D x and y coordinates
            # of each character on the screen AFTER ROTATION
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            # This code is calculating the x and y coordinates of each character on the screen and also the luminance index of each character.
            # This x variable represents the 3D x-coordinate after rotation.This y variable represents the 3D y-coordinate after rotation.
            # This N variable represents the luminance index of each character.
            # is not an explicit rotation matrix. It is a combination of calculations that are used to calculate the 3D x and y coordinates
            # of each character on the screen after rotation.
            # The value of 40 in the x coordinate formula is used to adjust the size of the donut on the x-axis. This value is multiplied
            # by the depth of the character on the screen (D) and the result of the calculation (l * h * m - t * n) to determine the
            # final x coordinate of the character on the screen. By changing the value of 40, you can make the donut appear larger or
            # smaller on the x-axis.
            # The value of 20 in the y coordinate formula is used to adjust the size of the donut on the y-axis. This value is multiplied
            # by the depth of the character on the screen (D) and the result of the calculation (l * h * n + t * m) to determine the
            # final y coordinate of the character on the screen. By changing the value of 20, you can make the donut appear
            # larger or smaller on the y-axis.
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            # If the coordinates fit
            # The variable D is used to calculate the depth of each character on the screen.
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

# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import pygame
import time

print("Step 02_lists ==> 03_erase_canvas")
    

pygame.init() #  start pygame



# Abb hum kcuh varibale ke under screen dray kerdei ge 
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CANVAS_CELL_SIZE = 40
ERASER_SIZE = 20#


# color
BLUE_COLOR = (0, 0, 255)
WHITE_COLOR = (255, 255, 255)
PINK_COLOR = (255, 0, 255)



# Abb hum screen ko draw kerne ke liye pygame ka use kerte hain
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT)) # screen ka size define kerna
pygame.display.set_caption("Enter effect in pygame") # screen ka title define kerna

grid = [] # grid ko define kerna
 
for row in range(0,CANVAS_HEIGHT,CANVAS_CELL_SIZE): # y axis ke liye loop chalana
    for col in range(0,CANVAS_WIDTH,CANVAS_CELL_SIZE): # x axis ke liye loop chalana
        rect = pygame.Rect(col, row, CANVAS_CELL_SIZE, CANVAS_CELL_SIZE)
        grid.append(rect)

eraser = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE) # eraser ko define kerna

running = True # running ko true set kerna
while running: # jab tak running true hai tab tak loop chalayenge
    screen.fill(WHITE_COLOR) # screen ko blue color se fill kerna
    for rect in grid:
        pygame.draw.rect(screen, BLUE_COLOR, rect)
    mouse_x, mouse_y = pygame.mouse.get_pos() # mouse ki position ko get kerna
    eraser.topleft = (mouse_x , mouse_y) # eraser ki position ko set kerna

    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
    grid = new_grid
    pygame.draw.rect(screen, PINK_COLOR, eraser) # eraser ko draw kerna


    for event in pygame.event.get(): # event ko get kerna
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip() # screen ko update kerna
    time.sleep(0.05)

pygame.quit()


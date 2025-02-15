import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 720, 720
POINTS = [(int(WIDTH / 2), 0), (0, HEIGHT), (WIDTH, HEIGHT)]
window = pygame.display.set_mode((WIDTH, HEIGHT))
pixels = [[[0, 0, 0] for j in range(HEIGHT)] for j in range(WIDTH)]
pixel = []

def eventHandler():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    
def update(w, h, points):
    global pixel, pixels
    if pixel == []:
        pixel = [w // 2, h // 2]
    else:
        point = points[random.randint(0, 2)]
        pixel = [(point[0] + pixel[0]) // 2, (point[1] + pixel[1]) // 2]
        #print(pixel[0], pixel[1], point[0], point[1])
        pixels[pixel[0]][pixel[1]] = [255, 255, 255]
        
def draw(pixels):
    global window
    for i in range(WIDTH):
        for j in range(HEIGHT):
            window.set_at((i, j), pixels[i][j])
    
    pygame.display.flip()


while True:
    for i in range(100):
        eventHandler()
        update(WIDTH, HEIGHT, POINTS)
        if i == 0:
            draw(pixels)
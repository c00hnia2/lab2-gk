import pygame

import math
 
# Inicjalizacja Pygame
pygame.init()
 
# Ustawienia ekranu
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transforms")
 
GREEN = (0, 255, 0)  # Zielony
BLUE = (0, 0, 255)   # Niebieski
 
def draw_polygon(surface, transform_type):
    surface.fill(BLUE)
    num_of_vertices = 15
    radius = 150
    points = [
        (radius * math.cos(i * 2 * math.pi / num_of_vertices),
         radius * math.sin(i * 2 * math.pi / num_of_vertices))
        for i in range(num_of_vertices)
    ]
    transformed_points = []
    for x, y in points:
        if transform_type == 1:
            x, y = x * 0.5, y * 0.5
        elif transform_type == 2:
            angle = 0.5
            x, y = x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle)
        elif transform_type == 3:
            x, y = x * 0.5, y * 0.8
            x, y = -x, -y  # Obrót o 180 stopni
        elif transform_type == 4:
            x, y = x + y * 0.35, y
        elif transform_type == 5:
            x, y = x, y * 0.3 - 90
        elif transform_type == 6:
            x, y = x, y - x * 0.5
            x, y = -y, x  # Obrót o 90 stopni
        elif transform_type == 7:
            x, y = x * 0.5, y
            x, y = -x, -y  # Obrót o 180 stopni
        elif transform_type == 8:
            angle = math.radians(30)
            x, y = x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle)
            x, y = x, y * 0.3 + 200
        elif transform_type == 9:
            x, y = x + 100, y + x * 0.25
            x, y = -x, -y  # Obrót o 180 stopni
 
        transformed_points.append((x + WIDTH // 2, y + HEIGHT // 2))
    pygame.draw.polygon(surface, GREEN, transformed_points)
 
# Pętla gry
running = True
transform_type = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                transform_type = 0
            elif pygame.K_1 <= event.key <= pygame.K_9:
                transform_type = event.key - pygame.K_0
 
    draw_polygon(screen, transform_type)
    pygame.display.flip()
pygame.quit()
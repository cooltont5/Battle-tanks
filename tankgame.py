import pygame
pygame.init()
import math

running = True
screen = pygame.display.set_mode((1280,720))
screen_limit = (1265,705)
red_x = 100
red_y = 300
blue_x = 1000
blue_y = 300
red_angle = 0 
blue_angle = 0 
red_tank = pygame.image.load("redtank.png")
red_tank = pygame.transform.scale(red_tank,(30,30))
blue_tank = pygame.image.load("bluetank.png")
blue_tank = pygame.transform.scale(blue_tank,(30,30))
speed = 0.1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    red_rotated_tank = pygame.transform.rotate(red_tank,red_angle)
    red_rect = red_rotated_tank.get_rect(center = (red_x,red_y))
    screen.blit(red_rotated_tank,red_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        red_y -= math.cos(math.radians(red_angle - 45)) * speed
        red_y += math.sin(math.radians(red_angle - 45)) * speed
        red_x -= math.sin(math.radians(red_angle - 45)) * speed
        red_x -= math.cos(math.radians(red_angle - 45)) * speed
    if keys[pygame.K_w]:
        red_y += math.cos(math.radians(red_angle - 45)) * speed
        red_y -= math.sin(math.radians(red_angle - 45)) * speed
        red_x += math.sin(math.radians(red_angle - 45)) * speed
        red_x += math.cos(math.radians(red_angle - 45)) * speed
    if keys[pygame.K_d]:
        red_angle -= 0.1
    if keys[pygame.K_a]:
        red_angle += 0.1
    red_rotated_tank = pygame.transform.rotate(red_tank,red_angle)
    screen.blit(red_rotated_tank,red_rect)
    
    blue_rotated_tank = pygame.transform.rotate(blue_tank,blue_angle)
    blue_rect = blue_rotated_tank.get_rect(center = (blue_x,blue_y))
    screen.blit(blue_rotated_tank,blue_rect)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        blue_y -= math.cos(math.radians(blue_angle - 45)) * speed
        blue_y += math.sin(math.radians(blue_angle - 45)) * speed
        blue_x -= math.sin(math.radians(blue_angle - 45)) * speed
        blue_x -= math.cos(math.radians(blue_angle - 45)) * speed
    if keys[pygame.K_UP]:
        blue_y += math.cos(math.radians(blue_angle - 45)) * speed
        blue_y -= math.sin(math.radians(blue_angle - 45)) * speed
        blue_x += math.sin(math.radians(blue_angle - 45)) * speed
        blue_x += math.cos(math.radians(blue_angle - 45)) * speed
    if keys[pygame.K_RIGHT]:
        blue_angle -= 0.1
    if keys[pygame.K_LEFT]:
        blue_angle += 0.1
    blue_rotated_tank = pygame.transform.rotate(blue_tank,blue_angle)
    screen.blit(blue_rotated_tank,blue_rect)



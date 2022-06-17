import sys

import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
    def blitme(self):
        self.screen.blit(self.image,self.rect)

pygame.init()
bg_color=(0,0,230)
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("blue sky")
ship=Ship(screen)

while True:
    check_events()
    screen.fill(bg_color)
    ship.blitme()
    pygame.display.flip()
#!/usr/bin/env python3
import pygame

#定义飞船类
class Ship():
    #设置飞船初始位置
    def __init__(self, screen):
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    #在指定位置绘制飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)
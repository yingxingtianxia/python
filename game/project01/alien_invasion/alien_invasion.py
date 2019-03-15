#!/usr/bin/env python3
import sys
import pygame
from alien_invasion.settings import Settings

#初始化游戏并创建一个屏幕对象
def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width,
        ai_settings.screen_height
    ))
    pygame.display.set_caption("外星人入侵")


    #设置背景色
    bg_color = ai_settings.bg_color
    #开始游戏的主循环
    while True:
        #监视鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环都重新绘制屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
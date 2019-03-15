#!/usr/bin/env python3
import sys
import pygame

#检测键盘和鼠标事件
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
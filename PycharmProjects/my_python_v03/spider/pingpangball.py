#!/usr/bin/env python3
#__*__coding: utf8__*__
import pygame
from pygame.locals import *
from sys import exit
import random

basket_x = 0
basket_y = 600
ball_x = 10
ball_y = 10
screen_width = 1000
screen_height = 800
score = 0

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('接球')
basket = pygame.image.load('lanzi.jpg').convert()
basket_w, basket_h = basket.get.size()
ball = pygame.image.load('ball.jpg').convert()
ball_w , ball_h = ball.get.size()

def update_basket():
    global basket_x
    global basket_y
    basket_x, ignore = pygame.mouse.get_pos()
    basket_x = basket_x-basket_w/2

    screen.blit(basket, (basket_x, basket_y))

def update_ball():
    global ball_x
    global ball_y
    ball_y += 1
    if ball_y+ball_h>basket_y:
        ball_y = 0
        ball_x = random.randint(0, screen_width-ball_w)

    ball_x += random.randint(-1, 1)
    if ball_x <= 0:
        ball_x = 0
    if ball_x > screen_width-ball_w:
        ball_x = screen_width-ball_w

    screen.blit(ball, (ball_x, ball_y))

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message,1,(10, 10, 10))
    screen.blit(text, (0, 0))

def check_for_catch():
    global score
    if ball_y+ball_h ==basket_y and ball_x>basket_x and ball_x<basket_x+basket_w-ball_w:
        score += 1

    display('分数:'+str(score))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))
    update_ball()
    update_basket()
    check_for_catch()
    pygame.display.update()
    clock.tick(1000)
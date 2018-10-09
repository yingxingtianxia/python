#!/usr/bin/env python3
# -*-coding: utf8-*-
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_limit = 3

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (120, 0, 0)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speed_scale = 1.1
        self.speed_score = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 5

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.speed_score)
        print(self.alien_points)

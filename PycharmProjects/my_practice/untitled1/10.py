#!/usr/bin/env python3
# -*-coding: utf8-*-
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)

print('...')
import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    zombies = [Zombie() for i in range(4)]
    game_world.add_objects(zombies, 1)
    for zombie in zombies:
        game_world.add_collision_pair('zombie:ball', zombie, None)
        game_world.add_collision_pair('boy:zombie', None, zombie)

     #땅바닥 추가







    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)
    game_world.add_collision_pair('boy:zombie', boy, None)

    #바닥에 공 배치
    global balls
    balls = [Ball(random.randint(200, 1600),60 ,0) for i in range(10)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)


def update():
    game_world.update()
    game_world.handle_collision()
    #boy, ball간의 충돌을 체크한다.

    # for ball in balls.copy():
    #     if game_world.collide(boy, ball):
    #         print('COLLISION boy : ball')



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass


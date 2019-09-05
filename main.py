

import pygame


import model
import engine
import config


if __name__ ==  '__main__':
    W = model.cWorld(config.WORLD_SIZE_X, config.WORLD_SIZE_Y)

   #W.PrintInhabitants()
    #W.PrintWorldPlane()
    #W.PrintSensorsXY(0,0)
    #print (W.inhabitants[0].move[0])
    #W.inhabitants[0].move[0]()
    #W.PrintInhabitants()
    #W.inhabitants[0].move[1]()
    #W.PrintInhabitants()

    pygame.init()

    clock = pygame.time.Clock()

    sc = pygame.display.set_mode((config.WORLD_SIZE_X * config.DISCRETENESS, config.WORLD_SIZE_Y * config.DISCRETENESS))
    x=0
    while 1:
        sc.fill((50,50,50))

        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()

        for i in W.inhabitants:
            if i.type == config.TYPE_GRASS:
                pygame.draw.circle(sc, config.GRASS_COLOR, (i.x * config.DISCRETENESS + int(config.DISCRETENESS / 2),
                                                               i.y * config.DISCRETENESS + int(
                                                                   config.DISCRETENESS / 2)), config.DISCRETENESS)
            if i.type == config.TYPE_PREDATOR:
                pygame.draw.circle(sc, config.PREDATOR_COLOR, (i.x * config.DISCRETENESS + int(config.DISCRETENESS / 2),
                                                               i.y * config.DISCRETENESS + int(
                                                                   config.DISCRETENESS / 2)), int(config.DISCRETENESS/2))
            if i.type == config.TYPE_HERBIVORES:
                pygame.draw.circle(sc, config.HERBIVORES_COLOR, (i.x * config.DISCRETENESS + int(config.DISCRETENESS / 2),
                                                               i.y * config.DISCRETENESS + int(
                                                                   config.DISCRETENESS / 2)), int(config.DISCRETENESS/2))


        pygame.display.update()
        W.Step()
        W.PrintInhabitants()
        #exit()
        clock.tick(config.FPS)
        #pygame.time.delay(100)


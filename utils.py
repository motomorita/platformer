import pygame
import engine

acorn0 = pygame.image.load('images/acorn.png')

def makeAcorn(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y,36,44)
    entityAnimation = engine.Animation([acorn0])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'collectable'
    return entity

trap0 = pygame.image.load('images/spike.png')

def makeTrap(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y,28,52)
    entityAnimation = engine.Animation([trap0])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'dangerous'
    return entity

    
idle0 = pygame.image.load('images/idle1/idle1_0.png')
idle1 = pygame.image.load('images/idle1/idle1_1.png')
idle2 = pygame.image.load('images/idle1/idle1_2.png')
idle3 = pygame.image.load('images/idle1/idle1_3.png')
idle4 = pygame.image.load('images/idle1/idle1_4.png')
idle5 = pygame.image.load('images/idle1/idle1_5.png')

walking0 = pygame.image.load('images/movement/movement_0.png')
walking1 = pygame.image.load('images/movement/movement_1.png')
walking2 = pygame.image.load('images/movement/movement_2.png')
walking3 = pygame.image.load('images/movement/movement_3.png')
walking4 = pygame.image.load('images/movement/movement_4.png')
walking5 = pygame.image.load('images/movement/movement_5.png')
walking6 = pygame.image.load('images/movement/movement_6.png')
walking7 = pygame.image.load('images/movement/movement_7.png')

def makePlayer(x, y, h, w):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, h, w)
    entityIdleAnimation = engine.Animation([idle0, idle1, idle2, idle3, idle4, idle5])
    entityWalkingAnimation = engine.Animation([walking0, walking1, walking2, walking3, walking4, walking5, walking6, walking7])
    entity.animations.add('idle', entityIdleAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    entity.type = 'player'
    return entity
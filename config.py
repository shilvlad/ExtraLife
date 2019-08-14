#Размер мира
WORLD_SIZE_X = 100
WORLD_SIZE_Y = 100

# Дискретность мира
DISCRETENESS = 1

# Количство кадров в секунду
FPS = 60

# Цвета объектов
PREDATOR_COLOR = (255,0,0)
HERBIVORES_COLOR = (64, 128, 255)
GRASS_COLOR = (0, 255, 0)

#Типы обитателей
TYPE_PREDATOR = 1
TYPE_HERBIVORES = 2
TYPE_GRASS = 3

# Начальные объемы населения
POWER_GRASS = 3000
POWER_PREDATOR = 1000
POWER_HERBIVORES = 1000


# Координаты дальнего горизонта
FAR_HORIZON = [
    ( - 2,  - 0),
    ( - 2,  - 1),
    ( - 1,  - 2),
    ( - 0,  - 2),
    ( + 1,  - 2),
    ( + 2,  - 1),
    ( + 2,  - 0),
    ( + 2,  + 1),
    ( + 1,  + 2),
    ( + 0,  + 2),
    ( - 1,  + 2),
    ( - 2,  + 1),
]
NEAR_HORIZON = [
    ( - 1,  - 0),
    ( - 1,  - 1),
    ( - 0,  - 1),
    ( + 1,  - 1),
    ( + 1,  + 0),
    ( + 1,  + 1),
    ( + 0,  + 1),
    ( - 1,  + 1),

]





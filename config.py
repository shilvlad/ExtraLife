#Размер мира
WORLD_SIZE_X = 20
WORLD_SIZE_Y = 20

# Дискретность мира
DISCRETENESS = 35

# Количство кадров в секунду
FPS = 1

# Цвета объектов
PREDATOR_COLOR = (255,0,0)
HERBIVORES_COLOR = (64, 128, 255)
GRASS_COLOR = (0, 255, 0)

#Типы обитателей
TYPE_PREDATOR = 1
TYPE_HERBIVORES = 2
TYPE_GRASS = 3

# Начальные объемы населения
POWER_GRASS = 0
POWER_PREDATOR = 4
POWER_HERBIVORES = 4


# Максимальные жизни
MAX_GRASS_LIFE = 15 # Deprecated
MAX_HERBIVORE_LIFE=100
MAX_PREDATOR_LIFE = 100


# Максимальный возраст
MAX_GRASS_AGE = 15
MAX_HERBIVORE_AGE=100
MAX_PREDATOR_AGE = 100


# Продуктивный возраст
MAX_PRODUCTIVITY_AGE = 80
MIN_PRODUCTIVITY_AGE = 20

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





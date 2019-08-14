import random, time
import config, params


def time_of_function(function):
    def wrapped(*args):
        start_time = time.clock()
        res = function(*args)
        print(time.clock() - start_time)
        return res
    return wrapped



class cWorld:
    """docstring"""

    @time_of_function
    def __init__(self, width, height):
        """Constructor"""
        self.width = width
        self.height = height
        self.inhabitants = []
        self.PopulateWorld()

    # Добавить обитателя

    def AddInhabitant(self, type):
        # Добавление хищников
        if type == config.TYPE_PREDATOR:
            x = random.randrange(0, self.width / config.DISCRETENESS, 1)
            y = random.randrange(0, self.height / config.DISCRETENESS, 1)
            if self.InhabitantNotExists(x,y, config.TYPE_PREDATOR) and self.InhabitantNotExists(x,y, config.TYPE_HERBIVORES):
                #print ('Adding Predator')
                self.inhabitants.append(cInhabitant(type, x, y))
                return True
            else:
                return False

        # Добавление травоядных
        if type == config.TYPE_HERBIVORES:
            x = random.randrange(0, self.width / config.DISCRETENESS, 1)
            y = random.randrange(0, self.height / config.DISCRETENESS, 1)
            if self.InhabitantNotExists(x,y, config.TYPE_PREDATOR) and self.InhabitantNotExists(x,y, config.TYPE_HERBIVORES):
                #print('Adding Herbivores')
                self.inhabitants.append(cInhabitant(type, x, y))
                return True
            else:
                return False

        # Добавление травы
        if type == config.TYPE_GRASS:
            x = random.randrange(0, self.width / config.DISCRETENESS, 1)
            y = random.randrange(0, self.height / config.DISCRETENESS, 1)
            #print('Adding Grass')
            self.inhabitants.append(cInhabitant(type, x, y))
            return True

    # Заселение мира

    def PopulateWorld(self):
        for i in range(config.POWER_GRASS):
            self.AddInhabitant(config.TYPE_GRASS)

        for i in range(config.POWER_HERBIVORES):
            self.AddInhabitant(config.TYPE_HERBIVORES)

        for i in range(config.POWER_PREDATOR):
            self.AddInhabitant(config.TYPE_PREDATOR)

    # Сделать ход
    def Step(self):
        # Каждый обитатель (в зависимости от типа) принимает решение о действии
        pass

    # Отсутствует ли в заданной ячейке обитатели заданного типа
    def InhabitantNotExists(self, x, y, type):
        for n in self.inhabitants:
            if n.x == x and n.y == y and n.type == type:
                #print("Скотина здесь уже есть")
                return False
        return True

    # Тип обитателя по координатам
    def GetInhabitantType(self, x, y):
        for n in self.inhabitants:
            if n.x == x and n.y == y:
                return n.type


    # Сенсоры
    #
    # Дальний горизонт
    def GetFarHorizonSensors(self, x, y, index):
        if x + config.FAR_HORIZON[index][0] < 0:
            X = config.WORLD_SIZE_X + config.FAR_HORIZON[index][0]+1
        else:
            X = x + config.FAR_HORIZON[index][0]

        if y + config.FAR_HORIZON[index][1] < 0:
            Y = config.WORLD_SIZE_Y + config.FAR_HORIZON[index][1]+1
        else:
            Y = y + config.FAR_HORIZON[index][1]

        return self.GetInhabitantType( X, Y)

    def GetNearHorizonSensors(self, x, y, index):
        if x + config.NEAR_HORIZON[index][0] < 0:
            X = config.WORLD_SIZE_X + config.NEAR_HORIZON[index][0]+1
        else:
            X = x + config.NEAR_HORIZON[index][0]

        if y + config.NEAR_HORIZON[index][1] < 0:
            Y = config.WORLD_SIZE_Y + config.NEAR_HORIZON[index][1]+1
        else:
            Y = y + config.NEAR_HORIZON[index][1]

        return self.GetInhabitantType( X, Y)

    # Отладочные методы
    def PrintInhabitants(self):
        for n in self.inhabitants:
            print(n)


    def PrintSensorsXY(self, x, y):
        print('=========>>>')
        #print(config.FAR_HORIZON.__len__())
        for i in range(config.FAR_HORIZON.__len__()):
            print(config.FAR_HORIZON[i],'--', self.GetFarHorizonSensors( x, y, i))
        print('====>>>')
        for i in range(config.NEAR_HORIZON.__len__()):
            print(config.NEAR_HORIZON[i],'--', self.GetNearHorizonSensors( x, y, i))


    # Выводит для каждой координаты первого встречного обитателя
    def PrintWorldPlane(self):
        for x in range(config.WORLD_SIZE_X):
            for y in range(config.WORLD_SIZE_Y):
                print('x: ', x, 'y: ', y, self.GetInhabitantType(x, y))


class cInhabitant:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        #TODO ПОПРАВИТЬ ЖИЗНИ
        self.life = 100 # Жизненные силы
        self.age = 0 # Возраст

    def __str__(self):
        return str({
            'name': self.type,
            'x': self.x,
            'y': self.y,
            'life': self.life,
        })







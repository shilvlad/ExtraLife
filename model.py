import random, time
import config


def time_of_function(function):
    def wrapped(*args):
        start_time = time.clock()
        res = function(*args)
        print(time.clock() - start_time)
        return res
    return wrapped



class cWorld:



    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.inhabitants = []
        self.PopulateWorld()

    # Добавить обитателя задонного типа, с заданным кол-вом жизней и с заданными координатами. Если не заданы жизни или координаты, то случайным образом
    def AddInhabitant(self, type, life=100, x = -1, y = -1):
        # Добавление хищников
        if x == -1 and y == -1:
            x = random.randrange(0, self.width, 1)
            y = random.randrange(0, self.height, 1)

        if type == config.TYPE_PREDATOR:

            if self.InhabitantNotExists(x,y, config.TYPE_PREDATOR) and self.InhabitantNotExists(x,y, config.TYPE_HERBIVORES):
                #print ('Adding Predator')
                self.inhabitants.append(cInhabitant(type, x, y))
                return True
            else:
                return False

        # Добавление травоядных
        if type == config.TYPE_HERBIVORES:

            if self.InhabitantNotExists(x,y, config.TYPE_PREDATOR) and self.InhabitantNotExists(x,y, config.TYPE_HERBIVORES):
                #print('Adding Herbivores')
                self.inhabitants.append(cInhabitant(type, x, y))
                return True
            else:
                return False

        # Добавление травы
        if type == config.TYPE_GRASS:

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

        # Каждый обитатель просчитывается по возрасту и жизненым силам
        i = 0
        while i < self.inhabitants.__len__() and i >= 0:
            # Если травоядное, то:
            if self.inhabitants[i].type == config.TYPE_HERBIVORES:
                # Взрослеем от 0 до MAX_HERBIVORE_AGE. Смерть если больше MAX_HERBIVORE_AGE
                if self.inhabitants[i].age < config.MAX_HERBIVORE_AGE:
                    self.inhabitants[i].age += 1
                    if self.inhabitants[i].life > 0:
                        self.inhabitants[i].life -= 1
                    else:
                        print('Сдох с голоду: ', self.inhabitants[i])
                        del (self.inhabitants[i])
                        i = i - 1
                        continue
                else:
                    print('Сдох: ', self.inhabitants[i])
                    del (self.inhabitants[i])
                    i = i - 1
                    continue

            if self.inhabitants[i].type == config.TYPE_PREDATOR:

                # Взрослеем от 0 до MAX_PREDATOR_AGE. Смерть если больше MAX_HERBIVORE_AGE
                if self.inhabitants[i].age < config.MAX_PREDATOR_AGE:
                    self.inhabitants[i].age += 1
                    if self.inhabitants[i].life > 0:
                        self.inhabitants[i].life -= 1
                    else:
                        print('Сдох с голоду: ', self.inhabitants[i])
                        del (self.inhabitants[i])
                        i = i - 1
                        continue
                else:
                    print('Сдох: ', self.inhabitants[i])
                    del (self.inhabitants[i])
                    i = i - 1
                    continue

            if self.inhabitants[i].type == config.TYPE_GRASS:
                if self.inhabitants[i].age < config.MAX_GRASS_AGE:
                    self.inhabitants[i].age += 1
                else:
                    print('Пожузхла травка: ', self.inhabitants[i])
                    del (self.inhabitants[i])
                    i = i - 1
                    continue

            i += 1

        i = 0

        # Просчет действия. Еда, размножение, движение


        # Перемещаем оставшихся
        for i in range(self.inhabitants.__len__()):
            # Перемещение случайным образом
            if self.inhabitants[i].type != config.TYPE_GRASS:
                ri = random.randrange(0, 3, 1)
                self.inhabitants[i].move[ri]()


        # Добавляем траву

        #for i in range(config.POWER_GRASS):
            #self.AddInhabitant(config.TYPE_GRASS)


    # Returns list of Objects cInhabitant in [X, Y] as result if someone exists here
    def GetInhabitantXY(self, x,y):
        result = []
        for n in self.inhabitants:
            if n.x == x and n.y == y:
                result.append(n)
        return result

    # Отсутствует ли в заданной ячейке обитатели заданного типа
    def InhabitantNotExists(self, x, y, type):
        for n in self.inhabitants:
            if n.x == x and n.y == y and n.type == type:
                #print("Скотина здесь уже есть")
                return False
        return True

    # Присутствует ли в в заданной клетке обитатели заданного типа
    def InhabitantExists(self, x, y, type):
        for n in self.inhabitants:
            if n.x == x and n.y == y and n.type == type:
                #print("Скотина здесь уже есть")
                return True
        return False

    # Тип обитателя по координатам
    def GetInhabitantType(self, x, y):
        for n in self.inhabitants:
            if n.x == x and n.y == y:
                return n.type

    def GetInhabitantXYType(self, x, y, type):
        for n in self.inhabitants:
            if n.x == x and n.y == y and n.type==type:
                return n

    # Сенсоры
    #
    # Дальний горизонт
    def GetFarHorizonSensors(self, x, y, index):
        if x + config.FAR_HORIZON[index][0] < 0:
            X = x + config.FAR_HORIZON[index][0] + config.WORLD_SIZE_X
        elif x + config.FAR_HORIZON[index][0] >= config.WORLD_SIZE_X:
            X = x + config.FAR_HORIZON[index][0] - config.WORLD_SIZE_X
        else:
            X = x + config.FAR_HORIZON[index][0]



        if y + config.FAR_HORIZON[index][1] < 0:
            Y = y + config.FAR_HORIZON[index][1] + config.WORLD_SIZE_Y
        elif y + config.FAR_HORIZON[index][1] >= config.WORLD_SIZE_Y:
            Y = y + config.FAR_HORIZON[index][1] - config.WORLD_SIZE_Y
        else:
            Y = y + config.FAR_HORIZON[index][1]

        return self.GetInhabitantType( X, Y)

    # Ближний горизонт
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
    def __init__(self, type, x, y, l):
        self.type = type
        self.x = x
        self.y = y
        #TODO ПОПРАВИТЬ ЖИЗНИ
        self.life = 50 # Жизненные силы
        self.age = 0 # Возраст
        self.move = [self.MoveLeft, self.MoveRight, self.MoveUp, self.MoveDown]

    def __str__(self):
        return str({
            'name': self.type,
            'x': self.x,
            'y': self.y,
            'life': self.life,
            'age': self.age,
        })

    def MoveLeft(self):
        self.x = self.x-1
        if self.x < 0:
            self.x = self.x + config.WORLD_SIZE_X

    def MoveRight(self):
        self.x = self.x + 1
        if self.x >= config.WORLD_SIZE_X:
            self.x = self.x - config.WORLD_SIZE_X

    def MoveUp(self):
        self.y = self.y - 1
        if self.y < 0:
            self.y = self.y + config.WORLD_SIZE_Y

    def MoveDown(self):
        self.y = self.y + 1
        if self.y >= config.WORLD_SIZE_Y:
            self.y = self.y - config.WORLD_SIZE_Y








